# Choice of Pre-trained Model

- VGG16 as the model pretained on large dataset
- Pre-trained on ImageNet and rcognizes general features (edges, textures, shapes).

# Fine-Tuning Process
- Load Pre-trained VGG16: Exclude top layers, set input shape to (32, 32, 3).
- Freeze Layers: Prevent retraining of VGG16 layers to save computation.

## Addition of Custom Layers:
- Flatten layer to convert 3D output to 1D.
- Dense(64) layer with ReLU activation.
- Dense(10) layer for classification (10 classes).
- Combine VGG16 to custom layers added

# Performance Improvements
- Faster Convergence: Pre-trained features speed up adaptation.
- Reduced Training Time: Freezing layers reduces parameters to train.