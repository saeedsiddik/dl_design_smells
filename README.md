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
* Using batchnorm after dropout in DL Model
* Function BatchNormalization() and Dropout() both are callable at least one time

### What it can identify
* Calls of BatchNormalization() and Dropout()
* Calling sequence of both methods from AST of the corresponding Python files

### When it cannot detect
* Outside the Keras and Tensorflow 
* BatchNormalization() and Dropout() are called as a local function under a variable 

### TODO
* Select 10 repositories with the smell and run them
* Refactor the 10 files and run the projects again
* Evaluate the performance of the model
