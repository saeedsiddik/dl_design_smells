# Deep Learning Design Smells

ECE720 Course Project 2022

## Non--expanding feature map
### Assumptions
* Conv2D is called with constant filters like Conv2D(32, ...) or Conv2D(filters=32, ...)
* All the calls of Conv2D in a scope/method are part of same model

### What it can identify
* Calls of Conv2D
* Values of filters in argument of Conv2D either in a form of constant value or as a keyword argument

### What it cannot identify
* Calls of Conv2D in form of layers.Conv2D

### When it cannot detect
* Multiple calls of Conv2D where Conv2D is inside another method
* Conv2D called with variable filters value

