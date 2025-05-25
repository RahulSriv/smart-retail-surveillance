import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the frame image
image_path = "resources/output/extracted_frames/frame_0005.jpg"
image = Image.open(image_path)

# Assume YOLO detection results
yolo_detections = [
    {"label": "person", "confidence": 0.90},
    {"label": "person", "confidence": 0.87}
]

# Construct enriched prompt
detection_info = "\n".join([f"- {d['label']} (confidence: {d['confidence']:.2f})" for d in yolo_detections])

prompt = f"""
You are analyzing a retail surveillance frame for suspicious activity.

YOLOv8 object detection found:
{detection_info}

The scene appears to be inside a store where individuals are interacting with shelves or items.

Please analyze the image and answer:
1. What do you observe in terms of human behavior?
2. Is any suspicious or shoplifting-like behavior visible?
3. Are there any behavioral patterns or body language that stand out?

Use the visual context and detection info to respond precisely.
"""

# Generate Gemini response
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content([prompt, image])

print("\n--- GEMINI ANALYSIS (Context-Aware) ---")
print(response.text)
