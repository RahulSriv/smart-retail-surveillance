import cv2
import os

# Path to your annotated video (output from step 3)
video_path = "D:/Tutorials/smart-retail-surveillance/resources/input/sample.mp4"


# Folder where frames will be saved
output_folder = "D:/Tutorials/smart-retail-surveillance/resources/output/extracted_frames"
os.makedirs(output_folder, exist_ok=True)

# How often to save frames (every n-th frame)
frame_interval = 20  # adjust to save more or fewer frames

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ Error: Could not open video.")
    exit()
frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save frame every 'frame_interval' frames
    if frame_count % frame_interval == 0:
        filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        saved_count += 1

    frame_count += 1

cap.release()
print(f"Done! Total frames saved: {saved_count}")
