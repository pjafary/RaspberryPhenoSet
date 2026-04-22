from ultralytics import YOLO
from ultralytics import RTDETR


# to load one of Ultralytics' pretrained models use one of the examples below
model = YOLO("yolov8x.pt")
model = YOLO("yolov10n.pt")
model = RTDETR("rtdetr-l.pt")

# to load a pretrained model on PhenoSet, pass the path to the pretrained weights
model = YOLO("/path/to/RaspberryPhenoSet/ModelName/weights/best.pt")

# to train a custom model architecture, pass the path to a YAML file specifying the model
model = YOLO("/path/to/yaml/yolov8x_p2_shallow.yaml") # note that this is different from data yaml file
model.load("yolov8x.pt")   # optional: loads matching pretrained weights where shapes match

# configure the training hyperparameters below and train the model on the PhenoSet
results = model.train(
    data='Raspberry_PhenoSet.yaml',
    # data='PhenoSet_clahe.yaml',
    epochs=100,
    batch=12,
    imgsz=640,
    #weight_decay=0.0005,
    # auto_augment=False,
    # hsv_h=0.05,
    # hsv_s=0.7,
    # hsv_v=0.6,
    # degrees=20.0,
    # translate=0.2,
    # scale=0.5,
    # shear=10.0,
    # perspective=0.0005,
    # flipud=0.0,
    # fliplr=0.5,
    # mosaic=1.0,
    # mixup=0.2
    )
