import os
import shutil
from PIL import Image
import google.generativeai as genai
from ultralytics import YOLO
from dotenv import load_dotenv
import re

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# Load YOLOv8 model
yolo_model = YOLO("yolov8n.pt")

# Output folders
os.makedirs("resources/flagged_frames", exist_ok=True)


# Get real YOLO detections
def run_yolo_on_frame(image_path):
    results = yolo_model.predict(source=image_path, conf=0.4, verbose=False)[0]
    detections = []
    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = results.names[cls_id]
        conf = float(box.conf[0])
        detections.append({"label": label, "confidence": conf})
    return detections


# Build Gemini prompt with actual detections
def build_prompt(detections):
    detection_info = "\n".join([f"- {d['label']} (confidence: {d['confidence']:.2f})" for d in detections])
    return f"""
You are analyzing a retail surveillance frame for suspicious activity.

YOLOv8 object detection found:
{detection_info}

The scene appears to be inside a store where individuals are interacting with shelves or items.

Please analyze the image and answer:
1. What do you observe in terms of human behavior?
2. Is any suspicious or shoplifting-like behavior visible?
3. Are there any behavioral patterns or body language that stand out?
"""


# Smarter suspicion check with negation handling
def is_suspicious(text):
    text = text.lower()
    negations = [
        r"no suspicious", r"not suspicious",
        r"no evidence of shoplifting", r"no indication of",
        r"nothing unusual", r"normal behavior"
    ]
    for pattern in negations:
        if re.search(pattern, text):
            return False
    keywords = ["shoplifting", "stealing", "concealing", "unusual", "suspicious"]
    return any(word in text for word in keywords)


# Process all frames
frame_dir = "resources/output/extracted_frames"
for frame_file in sorted(os.listdir(frame_dir)):
    frame_path = os.path.join(frame_dir, frame_file)
    print(f"\n🔍 Processing: {frame_file}")

    # Step 1: YOLOv8 Detection
    detections = run_yolo_on_frame(frame_path)
    print("YOLO Detected:", [d["label"] for d in detections])

    # Step 2: Prepare and run Gemini analysis
    prompt = build_prompt(detections)
    img = Image.open(frame_path)
    gemini_response = gemini_model.generate_content([prompt, img])
    gemini_text = gemini_response.text.strip()

    print("--- GEMINI ANALYSIS ---")
    print(gemini_text)

    # Step 3: Flag frame if suspicious
    if is_suspicious(gemini_text):
        print(f"⚠️ Suspicious activity flagged! Saving {frame_file}")
        shutil.copy(frame_path, f"resources/flagged_frames/{frame_file}")
    else:
        print("✅ Normal behavior.")
