# Raspberry PhenoSet
## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Dataset](#dataset)
- [Training](#training)
- [Inference](#inference)
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

If you already know your way around CV and DL models, without further ado check out the dataset [here](https://drive.google.com/drive/folders/1LjmMFmOruVmRGwyY0pPJtkRCH17aW7Tz?usp=drive_link) and feel free to get in touch!

New to AI and Computer Vision? Fear not, just follow the instructions below. 

## Installation
Below you'll find the instructions for configuring the environment using Conda and installing Ultralytics and Detectron2 dependencies (you can have your pick among steps 2 and 3 based on the models you want to use.

**Note:** GPU acceleration requires a compatible NVIDIA GPU and installed NVIDIA driver. The provided environment file installs the required Python and CUDA runtime dependencies, but not the system-level GPU driver.

1. Start by cloning the repository

```bash
git clone https://github.com/pjafary/RaspberryPhenoSet.git
cd RaspberryPhenoSet
conda env create -f environment.yml
```
2. Install Ultralytics
To run YOLO and RT-DETR models, you need to have [Ultralytics](https://github.com/ultralytics/ultralytics) installed; you can use the following instructions.

```bash
conda activate raspberry_phenoset
pip install ultralytics
```
3. Detectron2
To run Faster R-CNN and Mask R-CNN models, you need to have [Detectron2](https://github.com/facebookresearch/detectron2) installed; you can use either of the following instructions.

```bash
conda activate raspberry_phenoset
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
# (add --user if you don't have permission)
```
Or, to install it from a local clone:
```bash
git clone https://github.com/facebookresearch/detectron2.git
python -m pip install -e detectron2
```

## Dataset
The Raspberry PhenoSet dataset is publicly available and can be downloaded from [here](https://drive.google.com/drive/folders/1LjmMFmOruVmRGwyY0pPJtkRCH17aW7Tz?usp=drive_link)

The dataset was developed for raspberry fruit phenology-stage detection and includes annotations aligned with seven biologically meaningful developmental stages based on the BBCH phenological framework.

### Dataset Contents
The download directory contains two image versions:

- **High Resolution Images** – original-resolution images for multi-GPU training.  
- **Low Resolution Images** – resized images optimized for training and inference on standard mid-class GPUs (ours was NVIDIA RTX 3060 12GB).  

Each image folder also includes a compressed labels archive containing the corresponding annotations.

### Folder Structure

After downloading and extracting the files you should have:

```text
RaspberryPhenoSet/
├── high.resolution(raw)/
│   ├── images/
│   └── labels.zip
│
├── low.resolution(resized)/
│   ├── images/
│   └── labels.zip
```

If using Ultralytics training make sure to arrange them in you arbitrary path as:
```text
dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
```

## Training
Ready-to-use Python scripts are provided for training with examples on how to configure a model either to train scratch or load a pre-trained model for further fine-tuning, please refer to `train_ultralytics.py` or `train_detectron2.py`.

## Inference
Similar to the training procedure, Python scripts are provided for inference as well with examples on how to load a pre-trained for inference, please refer to `detect_ultralytics.py` or `detec_detectron2.py` or for live camera inferece use `livecam_ultralytics.py

## Citation
Currently we appreciate your citations on our arXiv paper:
```text
@article{jafary2024raspberry,
  title={Raspberry PhenoSet: A Phenology-based Dataset for Automated Growth Detection and Yield Estimation},
  author={Jafary, Parham and Bazangeya, Anna and Pham, Michelle and Campbell, Lesley G and Saeedi, Sajad and Zareinia, Kourosh and Bougherara, Habiba},
  journal={arXiv preprint arXiv:2411.00967},
  year={2024}
}
```
## Contact
You can contact me by email at pjafary@torontomu.ca

