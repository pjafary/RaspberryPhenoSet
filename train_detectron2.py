# Libraries -------------------------------------------------------
import torch
import torchvision
import cv2
import os
import numpy as np
import json
import random
import matplotlib.pyplot as plt
from detectron2.structures import BoxMode
from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2 import model_zoo
from detectron2.engine import DefaultTrainer, DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import ColorMode, Visualizer
from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader
#-----------------------------------------------------------------

# Registering Dataset --------------------------------------------
def get_data_dicts(img_dir, json_file, classes, category_mapping):
    with open(json_file) as f:
        imgs_anns = json.load(f)
    
    dataset_dicts = []
    for idx, v in enumerate(imgs_anns["images"]):
        record = {}
        
        filename = os.path.join(img_dir, v["file_name"])
        
        record["file_name"] = filename
        record["image_id"] = idx
        record["height"] = 600
        record["width"] = 900
      
        annos = [anno for anno in imgs_anns["annotations"] if anno["image_id"] == v["id"]]
        objs = []
        for anno in annos:
            px = anno['segmentation'][0][0::2]
            py = anno['segmentation'][0][1::2]
            poly = [(x, y) for x, y in zip(px, py)]
            poly = [p for x in poly for p in x]

            category_id = anno["category_id"]
            category_name = category_mapping[category_id]
            category_index = classes.index(category_name)

            obj = {
                "bbox": anno["bbox"],
                "bbox_mode": BoxMode.XYWH_ABS,
                "segmentation": [poly],
                "category_id": category_index,
                "iscrowd": anno.get("iscrowd", 0)
            }
            objs.append(obj)
        record["annotations"] = objs
        dataset_dicts.append(record)
    return dataset_dicts

classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
category_mapping = {
    3554254475: 'A',
    1255198513: 'B',
    1037565863: 'C',
    2746444292: 'D',
    3568589458: 'E',
    1304234792: 'F',
    985283518: 'G'
}
######################################################### update the paths to your dataset accordingly #################################################
train_img_dir = '/path/to/images/train'
train_json_file = '/path/to/labels/train2.json'
test_img_dir = '/path/to/images/test'
test_json_file = '/path/to/labels/test2.json'
######################################################################################################################################################
def register_datasets():
    DatasetCatalog.register("category_train", lambda: get_data_dicts(train_img_dir, train_json_file, classes, category_mapping))
    MetadataCatalog.get("category_train").set(thing_classes=classes)
    
    DatasetCatalog.register("category_test", lambda: get_data_dicts(test_img_dir, test_json_file, classes, category_mapping))
    MetadataCatalog.get("category_test").set(thing_classes=classes)

register_datasets()

microcontroller_metadata = MetadataCatalog.get("category_train")
#----------------------------------------------------------------------------

# Training on the dataset ---------------------------------------------------
cfg = get_cfg()

#################################################### Choose the model architecture you want to train (comment out the rest) ###############################
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml"))
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml"))
###########################################################################################################################################################


cfg.DATASETS.TRAIN = ("category_train",)
cfg.DATASETS.TEST = ("category_test",)
cfg.DATALOADER.NUM_WORKERS = 4


########################################################### Set the path to the pre-trained model weights (comment out the rest) ###########################
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml")
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")  
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml")  
cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "trial1.pth") ############################## this one is for loading pretrained weights

###########################################################################################################################################################
num_train_images=1301
batch_size=12
cfg.SOLVER.IMS_PER_BATCH = batch_size
cfg.SOLVER.BASE_LR = (((16*10//batch_size+1)/10)*0.001)
cfg.SOLVER.MAX_ITER = (num_train_images//batch_size)*150
cfg.MODEL.ROI_HEADS.NUM_CLASSES = len(classes)

os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
trainer = DefaultTrainer(cfg) 
trainer.resume_or_load(resume=False)
trainer.train()

# Set image size for testing
#cfg.INPUT.MIN_SIZE_TEST = 300
#cfg.INPUT.MAX_SIZE_TEST = 450
#------------------------------------------------------------------------------

# Inferencing using the trained model -----------------------------------------
cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5 
cfg.DATASETS.TEST = ("category_test",)
predictor = DefaultPredictor(cfg)
test_dataset_dicts = get_data_dicts(test_img_dir, test_json_file, classes, category_mapping)
#------------------------------------------------------------------------------

# Evaluation ------------------------------------------------------------------
evaluator = COCOEvaluator("category_test", cfg, False, output_dir="/path/to/output/") ######################### update this accordingly #####################
val_loader = build_detection_test_loader(cfg, "category_test")
evaluation_results = inference_on_dataset(predictor.model, val_loader, evaluator)
#------------------------------------------------------------------------------

# Print the evaluation results
print(evaluation_results)

