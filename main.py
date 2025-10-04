import cv2
from ultralytics import YOLO

models = YOLO("yolo11n-pose.pt")
cap = cv2.VidioCapture(0, cv.CAP_DSHOW)

while True:
    ok, frame = cap.read()
    if not ok:
        break