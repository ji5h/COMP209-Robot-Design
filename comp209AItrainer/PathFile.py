from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model.train(data="C:\\Users\\Ronny\\comp209AItrainer\\GARBAGE CLASSIFICATION 3.v2-gc1.yolov8\\data.yaml", epochs=10)
