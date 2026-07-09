# Hybrid Intrusion Detection System using PCA, Harris Hawks Optimization, SVM & KNN

A machine learning-based Intrusion Detection System (IDS) that detects malicious network traffic using a hybrid classification framework. The project combines Principal Component Analysis (PCA) for dimensionality reduction, Harris Hawks Optimization (HHO) for feature selection, Support Vector Machine (SVM) for binary intrusion detection, and K-Nearest Neighbors (KNN) for multi-class attack classification.

---

# Overview

Intrusion Detection Systems (IDS) play a crucial role in protecting modern computer networks against cyber threats. Traditional signature-based approaches often struggle to detect new or evolving attacks. This project implements a hybrid machine learning pipeline that improves detection accuracy while reducing feature dimensionality and computational complexity.

The project uses the **NSL-KDD** benchmark dataset and follows a complete end-to-end machine learning workflow, including preprocessing, feature engineering, model training, and performance evaluation.

---

# Features

- Network Intrusion Detection System
- Data preprocessing and feature engineering
- One-Hot Encoding of categorical features
- Principal Component Analysis (PCA)
- Harris Hawks Optimization (HHO) for feature selection
- Binary classification using Support Vector Machine (SVM)
- Multi-class attack classification using K-Nearest Neighbors (KNN)
- Confusion Matrix visualization
- Classification Reports
- Reproducible machine learning pipeline

---

# Project Pipeline
The complete workflow is:
NSL-KDD Dataset
↓
Data Cleaning
↓
One-Hot Encoding
↓
Feature Scaling
↓
Principal Component Analysis (PCA)
↓
Harris Hawks Optimization (HHO)
↓
Support Vector Machine (Binary Classification)
↓
K-Nearest Neighbors (Attack Classification)
↓
Performance Evaluation

# Dataset
The project uses the **NSL-KDD** intrusion detection dataset.

Attack categories include:

- Normal
- DoS (Denial of Service)
- Probe
- R2L (Remote to Local)
- U2R (User to Root)
The dataset is not included in this repository due to licensing and size limitations.
You can download it from:
https://www.kaggle.com/datasets/hassan06/nslkdd


# Methodology
## 1. Data Preprocessing
- Data loading
- Missing value inspection
- One-Hot Encoding
- Label Encoding
- Standard Scaling
## 2. Principal Component Analysis (PCA)
Principal Component Analysis is applied to reduce feature dimensionality while preserving approximately 95% of the information contained in the original dataset.
Benefits include:
- Reduced computational complexity
- Faster model training
- Lower risk of overfitting
## 3. Harris Hawks Optimization (HHO)
Harris Hawks Optimization is a nature-inspired optimization algorithm used to identify the most informative subset of features after PCA.
Advantages:
- Reduced feature redundancy
- Improved classification efficiency
- Better feature subset selection
## 4. Binary Classification
Support Vector Machine (SVM) classifies network traffic into:
- Normal Traffic
- Malicious Traffic
## 5. Multi-Class Classification
K-Nearest Neighbors (KNN) classifies detected attacks into:
- DoS
- Probe
- R2L
- U2R


# Repository Structure
Hybrid-Intrusion-Detection-System/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
├── images/
├── results/
└── src/

# Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

# Installation
Clone the repository
git clone https://github.com/YOUR_USERNAME/Hybrid-Intrusion-Detection-System.git

Navigate into the project
cd Hybrid-Intrusion-Detection-System

Install required libraries
pip install -r requirements.txt

Run the notebook
jupyter notebook
or execute the Python scripts inside the `src` directory.



# Results

## Binary Classification (Support Vector Machine)

| Metric | Value |
|---------|-------|
| Accuracy | 98.77%|
| Precision |99%|
| Recall | 99% |
| F1 Score |99% |


## Multi-Class Classification (K-Nearest Neighbors)

| Metric | Value |
|---------|-------|
| Accuracy | 98.52%|
| Weighted Precision | 99% |
| Weighted Recall | 99% |
| Weighted F1 Score | 99%|


# Binary Classification Report

| Class | Precision | Recall | F1 Score |
|---------|----------|---------|----------|
| Normal | 0.99 | 0.99 | 0.99 |
| Attack | 0.99 | 0.99 | 0.99 |


# Multi-Class Classification Report

| Attack Type | Precision | Recall | F1 Score |
|--------------|----------|---------|----------|
| DoS | 0.99 | 1.00 | 0.99 |
| Normal | 0.99 | 0.99 | 0.99 |
| Probe | 0.98 | 0.95 | 0.96 |
| R2L | 0.91 | 0.88 | 0.89 |
| U2R | 0.64 | 0.39 | 0.48 |


# Key Highlights

- Achieved 98.77% binary classification accuracy using SVM.
- Achieved 98.52% multi-class classification accuracy using KNN.
- Reduced feature dimensionality using Principal Component Analysis.
- Applied Harris Hawks Optimization for feature subset selection.
- Evaluated using precision, recall, F1-score, and confusion matrices.
- Implemented a complete machine learning workflow from preprocessing to evaluation.
-

# Limitations

- The U2R attack class has significantly fewer samples than other classes, resulting in lower classification performance.
- The implementation is designed for offline analysis and does not currently support real-time network monitoring.
- Further hyperparameter optimization and evaluation on additional datasets could improve model generalization.

# Author
Kavya Kilari
