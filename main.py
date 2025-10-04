import cv2
from ultralytics import YOLO

print("program stating...")
model = YOLO("yolo11n-pose.pt")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ok, frame = cap.read()
    if not ok:
        break
    results = model.predict(frame, imgsz=512, conf=0.5, iou=0.5, verbose=False)

    annotated = results[0].plot() 
    cv2.imshow("ESC to quit", annotated)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
