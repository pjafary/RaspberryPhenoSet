# Raspberry PhenoSet
## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Dataset](#dataset)
- [Training](#training)
- [Inference](#inference)
- [Results](#results)
- [Citation](#citation)

## Overview
RaspberryPhenoSet is a publicly available phenology-based computer vision dataset and benchmarking framework developed for automated monitoring of raspberry fruit development. The repository accompanies our research on integrating deep learning with biologically meaningful growth-stage annotations to support practical agricultural applications such as growth tracking, yield estimation, and harvest-time forecasting.

Unlike conventional fruit detection datasets that focus only on fruit presence or coarse ripeness categories, RaspberryPhenoSet is organized around seven developmental stages aligned with the BBCH phenological scale. This stage-aware structure enables models to learn subtle transitions throughout the fruit growth cycle, making the dataset suitable not only for detection tasks, but also for temporal decision-making in precision agriculture.

The dataset contains 1,853 annotated images with 6,907 labeled raspberry instances collected across three cultivars: Polana, Prelude, and Joan J. Annotations are provided in both bounding-box format for object detection and mask format for segmentation tasks.

This repository also includes pretrained models, and implementation resources for several state-of-the-art deep learning frameworks, including YOLOv8, YOLOv10, RT-DETR, Faster R-CNN, and Mask R-CNN. For full methodology and benchmarking results, see our [preprint on arXiv](https://arxiv.org/abs/2411.00967).

RaspberryPhenoSet is intended to serve as a benchmark resource for researchers in agricultural AI, computer vision, robotics, and smart farming systems seeking robust phenology-aware models for real-world crop monitoring.

## In a Nutshell
You can use/reproduce the benchmark reported in the paper in 5 easy steps:
1. Download and organize the dataset.
2. Prepare the Python environments and install dependencies.
3. Train or load the models from the corresponding folders.
4. Run validation on the test set.
5. Compare the output metrics across models.

If you already know your way around CV and DL models, without further ado check out the dataset [here](https://drive.google.com/drive/folders/1LjmMFmOruVmRGwyY0pPJtkRCH17aW7Tz?usp=drive_link) and the provided models and let me know your feedback :))

New to AI and Computer Vision? Fear not, just follow the instructions below. 

## Installation

To run YOLO and RT-DETR models you need to have Ultralytics installed, you can install it manually from their source at [Ultralytics](https://github.com/ultralytics/ultralytics) or if you have Conda installed use the following instructions (recommended).

Start by cloning the repository

```bash
git clone https://github.com/pjafary/RaspberryPhenoSet.git
cd RaspberryPhenoSet
```
Now let's create a Conda environment

```bash
conda env create -f environment.yml
```

## Dataset
## Training
## Inference
## Results
## Citation
## Contact


