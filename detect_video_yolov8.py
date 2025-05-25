import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
video_path = "resources/input/sample.mp4"
cap = cv2.VideoCapture(video_path)

# save output to file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('resources/output/detected_output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    # print("Read first frame:", ret)

    if not ret:
        break

    results = model.predict(source=frame, conf=0.5, verbose=False)
    annotated_frame = results[0].plot()
    cv2.imshow("Video Detection", annotated_frame)
    out.write(annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

for box in results[0].boxes:
    cls_id = int(box.cls[0].item())
    conf = float(box.conf[0].item())
    name = model.names[cls_id]
    print(f"Detected: {name} ({conf:.2f})")
