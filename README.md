# Facial-Keypoint-Detection

This repository contains my project for the **Introduction to Computer Vision** course, where I built a neural network to detect key facial landmarks in images.

## 📌 Project Overview

Facial keypoint detection is a computer vision task that involves identifying specific points on a human face, such as the corners of the eyes, eyebrows, nose tip, and mouth corners. It is a fundamental step in many applications like facial recognition, emotion detection, and augmented reality.

## 📂 Project Structure

- **1. Load and Visualize Data.ipynb**: Load the dataset of facial images and corresponding keypoints, visualize sample images, and inspect missing data.
- **2. Define the Network Architecture.ipynb**: Design and build a custom Convolutional Neural Network (CNN) using PyTorch for detecting facial keypoints.
- **3. Facial Keypoint Detection, Complete Pipeline.ipynb**: Combine the data preprocessing, model training, evaluation, and inference to detect keypoints on new images.
- **models.py**: A custom neural network architecture with four convolutional layers each followed by a maxpool layer and a dropout layer after the last pooling layer which is finally followed by a linear layer that produces the keypoints out. 

## 📝 Dataset

The dataset consists of 5770 color images split into training and testing set and each image in the set has a single face with 68 labeled keypoints marking eyes, corners of the mouth, the nose, etc. 

## 🛠️ Tools & Libraries

- Python
- PyTorch
- NumPy
- OpenCV
- Matplotlib
- Pandas

## 📊 Results

The trained model was able to accurately predict keypoints on unseen images, successfully overlaying the detected landmarks on test images.

## 📖 What I Learned

- Handling incomplete datasets
- Data normalization and augmentation (RandomCrop and Rescaling) for better model generalization
- Designing and training CNN architectures for regression problems
- Visualizing model predictions to evaluate performance

## 📸 Sample Output
<img src='images/key_pts_example.png' width=100% height=100%/>
