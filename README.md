# Deep Learning Design Smells Detection

ECE720: Machine Learning Systems Engineering Course Project 2022

### How to run
Run the detector from command line
  ```python3 design_smells_detector.py <design_smell> <project_path>```

Here, 
* `<design_smell>` denotes a code name for the design smells. Currently, the supported values are `nrse` and `nfm` where `nrse` is the code for Non-representative Statistics Estimation and `nfm` is the code for Non-expanding Feature Map.  
* `<project_path>` denotes the path of the project. All the files under this path will be considered for the design smells detection.
* Example ```python3 design_smells_detector.py nrse data/repositories_with_smells/nrse/```

## Non-expanding Feature Map
### Assumptions
* Conv2D is called with constant filters like Conv2D(32, ...) or Conv2D(filters=32, ...)
* All the calls of Conv2D in a scope/method are part of same model

### When it cannot detect
* Calls of Conv2D where Conv2D is inside another method
* Conv2D called with variable filters value
* Concatenation of models

### Observations
* Some variant of convolutional neural network use the non-expanding feature map as their architecture like U-Net, AlexNet, Inception

## Non-representative Statistics Estimation
### Assumptions
* Using batchnormalization after dropout in DL Model
* If the batchnorm is placed after the dropout, it will compute non-representative global statistics on the dropped outputs of the
layer.
* Function BatchNormalization() and Dropout() both are callable at least one time

### When it cannot detect
* Outside the Keras and Tensorflow 
* BatchNormalization() and Dropout() are called as a local function under a variable