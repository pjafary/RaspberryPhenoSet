# RaspberryPhenoSet
## Overview
**Overview:**

RaspberryPhenoSet is a publicly available phenology-based computer vision dataset and benchmarking framework developed for automated monitoring of raspberry fruit development. The repository accompanies our research on integrating deep learning with biologically meaningful growth-stage annotations to support practical agricultural applications such as growth tracking, yield estimation, and harvest-time forecasting.

Unlike conventional fruit detection datasets that focus only on fruit presence or coarse ripeness categories, RaspberryPhenoSet is organized around seven developmental stages aligned with the BBCH phenological scale. This stage-aware structure enables models to learn subtle transitions throughout the fruit growth cycle, making the dataset suitable not only for detection tasks, but also for temporal decision-making in precision agriculture.

The dataset contains 1,853 annotated images with 6,907 labeled raspberry instances collected across three cultivars: Polana, Prelude, and Joan J. Annotations are provided in both bounding-box format for object detection and mask format for segmentation tasks.

This repository also includes pretrained models, and implementation resources for several state-of-the-art deep learning frameworks, including YOLOv8, YOLOv10, RT-DETR, Faster R-CNN, and Mask R-CNN. For full methodology and benchmarking results, see our [preprint on arXiv](https://arxiv.org/abs/2401.12345](https://arxiv.org/abs/2411.00967).

RaspberryPhenoSet is intended to serve as a benchmark resource for researchers in agricultural AI, computer vision, robotics, and smart farming systems seeking robust phenology-aware models for real-world crop monitoring.
### Abstract
**Abstract:**

The future of agriculture is intertwined with automation. Accurate fruit detection, yield estimation, and harvest time prediction are crucial for efficient supply chain management by optimizing resources and logistic utilization. Computer vision can automate these tasks to reduce labour costs and improve efficiency by training deep learning models on appropriate data to perform knowledge-based tasks. Although fruit detection has been the focus of literature, yield prediction and harvest time estimation remain practical challenges for farmers. This is particularly important for high-value, highly perishable crops, such as raspberries, where contractual obligations require precise harvest timing. This paper addresses this gap by providing a pipeline for raspberry maturity detection and harvest time estimation. For this end, a phenology study of raspberry plants from three different cultivars was carried out and seven development stages were identified based on the BBCH-scale; for the first time, a phenology-based dataset of developing raspberry flowers and fruit was curated and made available publicly which contains 1,853 high-resolution images and 6,907 manually labelled annotations. A comprehensive benchmark was developed from state-of-the-art object detection models and finally a tailored deep-learning model capable of real-time inference was established that achieved 92.2% detection accuracy in vertical farm field test. The proposed pipeline can be used for raspberry yield estimation 28 to 33 days in advance of harvesting, depending on cultivar identity. The confusion matrix reveals that the classification of phenological stages with subtle morphological differences is challenging for deep-learning models. This challenge highlights the value of the established dataset and pipeline for future deep-learning model development.

### Conclusion
**Conclusion:**

Raspberry production faces significant logistical challenges due to the crop’s high perishability, narrow harvest window, and growing demand for consistent quality and supply. Accurate, real-time monitoring of phenological development is essential to mitigate postharvest losses, reduce manual labour dependence, and optimize scheduling across the supply chain. This study presents a phenology study of raspberry growth stages, a phenology-based image dataset (Raspberry PhenoSet), a benchmarking analysis of state-of-the-art object detection models for classifying seven biologically meaningful developmental stages, and a tailored object detection model for real-time maturity stage detection of raspberries under vertical farming conditions.
Among the tested models, the tailored YOLOv8-x achieved the highest detection accuracy across stages, including strong performance on both early-stage structures (e.g., floral buds) and harvest-ready fruit. Stage-level classification results demonstrated the model's capacity to distinguish phenological features with subtle differences in shape and colour, even in visually complex and occluded environments. The dataset and models were also validated under realistic deployment conditions, with YOLOv8-x operating at frame rates compatible with real-time applications. The annotated dataset and trained models enable a range of downstream applications, including yield forecasting, harvest readiness alerts, integration with robotic harvesting platforms, and health monitoring. These tools support the development of scalable, precision agriculture systems for soft fruits, offering a path toward reduced waste and more responsive supply chains. Given the global market value of raspberries and the increasing need for automation in horticulture, phenology-based detection frameworks such as those demonstrated here represent a timely and valuable contribution to the agri-food technology sector.

## Installation
## Dataset
## Training
## Inference
## Results
## Citation
## Contact


