# Baseline Model Overview

## Architecture

The baseline model is a CNN designed for image classification with CIFAR-10 datset. 

Key components:

- **Input Layer**: Accepts images of shape (32, 32, 3). 
- **Data Augmentation**: Applies random horizontal flipping, rotation (0.1), and zooming (0.1).
- **Convolutional & Pooling Layers**:
  - 32 filters with (3x3) kernel, ReLU activation, batch normalization, max pooling (2x2), and dropout (0.25).
  - 64 filters with (3x3) kernel, ReLU activation, batch normalization, max pooling (2x2), and dropout (0.25).
  - 128 filters with (3x3) kernel, ReLU activation, batch normalization, and global average pooling.
- **Fully Connected Layers**:
  - Dense layer with 128 units, ReLU activation, L2 regularization (0.01), and dropout (0.5).
  - Output layer with 10 units (softmax activation) for classification.

## Training Process

- **Preprocessing**: Normalized pixel values and applied data augmentation.
- **Configuration**:
  - Optimizer: Adam
  - Loss Function: Sparse Categorical Crossentropy
  - Metrics: Accuracy - to keep track of accuracy when training the model
- **Steps**:
  1. Load and preprocess the CIFAR-10 dataset.
  2. Compile the model with the specified optimizer, loss function, and metrics.
  3. Train the model using the training dataset and validate against the validation dataset.

## Performance Metrics

- **Test Accuracy**: 10%, 

Further improvements could include additional tuning of hyperparameters.