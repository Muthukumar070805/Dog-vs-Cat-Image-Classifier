# Dog vs Cat Classifier

A convolutional neural network (CNN) model for classifying images as either cats or dogs. This project uses a CNN built with Keras to distinguish between cat and dog images, trained on a labeled dataset.

## Project Overview
This project implements a binary image classifier to categorize images as "cat" or "dog". The classifier is trained on images resized to 100x100 pixels and uses a simple CNN architecture to achieve good accuracy.

## Dataset
The dataset used for this project is the [Dogs vs. Cats dataset from Kaggle](https://www.kaggle.com/c/dogs-vs-cats/data). Download the dataset from this link and organize it as follows:
- `train/cat`: Contains cat images.
- `train/dog`: Contains dog images.

#Running the Project in a Jupyter Notebook on Visual Studio Code

## Requirements
Install the following packages to run the project:
```bash
pip install numpy opencv-python matplotlib tensorflow keras 
