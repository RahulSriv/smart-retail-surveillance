import cv2
from ultralytics import YOLO

# 1. Load the YOLOv8 model
model = YOLO('yolov8n.pt') # 'n' stands for Nano (lightest and fastest)

# 2. Load an image using OpenCV
img_path = "resources/output/extracted_frames/frame_0001.jpg"  # Replace with your image file name
img = cv2.imread(img_path)

# 3. Run object detection
results = model.predict(source=img, conf=0.5)
annotated_img = results[0].plot()
cv2.imwrite("resources/output/detected_output.jpg", annotated_img)
cv2.imshow("Image Detection", annotated_img)
cv2.waitKey(0)   # waits until any key is pressed
cv2.destroyAllWindows()

# 4. Print detected class names
for result in results:
    print("\n--- DETECTIONS ---")
    boxes = result.boxes
    for box in boxes:
        cls_id = int(box.cls[0])
        class_name = result.names[cls_id]
        confidence = float(box.conf[0])
        print(f"Detected: {class_name} ({confidence:.2f})")
