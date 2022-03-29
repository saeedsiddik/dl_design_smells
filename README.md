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

### TODO
* Run detector on all the code files
* Select 10 files with the smell
* Clone the full repository of the 10 files and run them
* Read paper to set correct values of filters for the Conv2D calls
* Refactor the 10 files and run the projects again
* Evaluate the performance of the model

