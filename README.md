# Deep Learning Design Smells Detection

ECE720: Machine Learning Systems Engineering Course Project 2022

## Non-expanding feature map
### Assumptions
* Conv2D is called with constant filters like Conv2D(32, ...) or Conv2D(filters=32, ...)
* All the calls of Conv2D in a scope/method are part of same model

### What it can identify
* Calls of Conv2D
* Values of filters in argument of Conv2D either in a form of constant value or as a keyword argument

### When it cannot detect
* Calls of Conv2D where Conv2D is inside another method
* Conv2D called with variable filters value

### Observations
* Some variant of convolutional neural network use the non-expanding feature map as their architecture like U-Net, AlexNet, Inception

## Non-representative Statistics Estimation
### Assumptions
* Using batchnormalization after dropout in DL Model
* If the batchnorm is placed after the dropout, it will compute non-representative global statistics on the dropped outputs of the
layer.
* Function BatchNormalization() and Dropout() both are callable at least one time

### What it can identify
* Calls of BatchNormalization() and Dropout()
* Calling sequence of both methods from AST of the corresponding Python files

### When it cannot detect
* Outside the Keras and Tensorflow 
* BatchNormalization() and Dropout() are called as a local function under a variable 

### TODO
* Complete manual validation
* Merge the smell detectors
* Run the detector from command line
  `python3 design_smells_detector.py <project_path>`
* Select 10 repositories with the smell and run them
* Refactor the 10 files and run the projects again
* Compare the performance of the model
