from ultralytics import YOLO
from config import model_path

model = YOLO(model_path)

def detector(frame):
    results = model(frame, stream=True, conf = 0.6, device = 0, classes=[0])
    return results