# Deep Learning Design Smells

ECE720 Course Project 2022

### Assumptions for _Non-expanding feature map_
* Conv2D is called with constant filters like Conv2D(32, ...) or Conv2D(filters=32, ...)
* All the calls of Conv2D in a scope/method are part of same model


