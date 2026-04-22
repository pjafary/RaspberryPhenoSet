from ultralytics import YOLO
from pathlib import Path

# =========================
# Paths
# =========================
model_path = "/path/to/weights/best.pt"

source_path = "/path/to/test/images"   # folder containing new images

# =========================
# Load model
# =========================
model = YOLO(model_path)

# =========================
# Run inference and save results
# =========================
results = model.predict(
    source=source_path,     # image folder, single image, video, etc.
    imgsz=896,              # inference image size
    conf=0.2,              # confidence threshold
    iou=0.8,                # NMS IoU threshold
    save=True,              # save images with boxes and labels
    save_txt=False,         # set True if you also want txt detections
    save_conf=True,         # save confidence values in txt if save_txt=True
    show_labels=True,       # draw class labels
    show_conf=True,         # draw confidence scores
    project="/export/path/to/save/results",  
    name="test",
    exist_ok=True
)

print("Inference finished.")
print("Saved results to: /export/path/to/save/results/test")