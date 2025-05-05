from ultralytics import YOLO

model = YOLO("C:\\Users\\Ronny\\comp209AItrainer\\runs\\detect\\train4\\weights\\best.pt")

results = model.predict(source="Detector.py", show=True)