# import numpy as np
# x = np.load('bottleneck_features_validation_layer1.npy')
# print(len(x))
import argparse
import os

import matplotlib
import cv2
matplotlib.use('AGG')

import matplotlib.pyplot as plt
import numpy as np

from keras.datasets import cifar10
from keras.layers import (Activation, Conv3D, Dense, Dropout, Flatten,
                          MaxPooling3D, MaxPooling2D, regularizers)

from keras.layers.advanced_activations import LeakyReLU
from keras.losses import categorical_crossentropy
from keras.models import Sequential
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.utils.vis_utils import plot_model
from sklearn.model_selection import train_test_split

from tqdm import tqdm

from keras.callbacks import ModelCheckpoint
from keras.models import Model
from keras.layers import Input, Dense,Conv2D,GlobalAveragePooling2D,BatchNormalization
import keras


def multi_input_model():
    """构建多输入模型"""
    model = Sequential()

    model.add(Conv2D(filters=32, kernel_size=(12,12), strides=(1, 1), padding='valid', input_shape=(224, 224, 1),
    activation = 'relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))


    model.add(Conv2D(64, kernel_size=(9, 9), strides=(1, 1), padding='valid', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(128, kernel_size=(6, 6), strides=(1, 1), padding='valid', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))


    model.add(Conv2D(256, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))


    model.add(GlobalAveragePooling2D())
    model.add(BatchNormalization())

    model.add(Dense(10, activation='softmax'))
    model.summary()


def multi_input_models():
    """构建多输入模型"""
    model = Sequential()

    model.add(Conv2D(filters=32, kernel_size=(3,3), strides=(1, 1), padding='same', input_shape=(224, 224, 1),
    activation = 'relu'))
    model.add(BatchNormalization())
    # model.add(MaxPooling2D(pool_size=(2, 2)))


    model.add(Conv2D(64, kernel_size=(6, 6), strides=(1, 1), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2),padding="same"))

    model.add(Conv2D(128, kernel_size=(9, 9), strides=(1, 1), padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))


    # model.add(Flatten())
    #
    #
    # model.add(Dense(512, activation='relu'))
    # model.add(Dense(128, activation='relu'))

    model.add(GlobalAveragePooling2D())
    model.add(BatchNormalization())

    model.add(Dense(10, activation='softmax'))
    model.summary()


def multi_input_modelss():
    """构建多输入模型"""
    model = Sequential()

    model.add(Conv2D(filters=128, kernel_size=(3,3), strides=(1, 1), padding='same', input_shape=(238, 238, 1),
    activation = 'relu'))
    # model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))


    model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'))
    # model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'))
    # model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))


    model.add(Flatten())


    model.add(Dense(1024, activation='relu'))
    model.add(Dense(256, activation='relu'))

    # model.add(GlobalAveragePooling2D())
    # model.add(BatchNormalization())

    model.add(Dense(10, activation='softmax'))
    model.summary()


def multi_input_modelssd():
    """构建多输入模型"""
    model = Sequential()

    model.add(Conv2D(filters=32, kernel_size=(3,3), strides=(1, 1), padding='valid', input_shape=(100, 100,3),activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(MaxPooling2D())

    model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'))
    model.add(Dropout(0.5))
    model.add(MaxPooling2D())

    model.add(Conv2D(128, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'))
    model.add(Dropout(0.5))
    model.add(MaxPooling2D())

    model.add(Conv2D(256, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'))
    model.add(Dropout(0.5))
    model.add(MaxPooling2D())

    model.add(Conv2D(512, kernel_size=(3, 3), strides=(1, 1), padding='valid', activation='relu'))
    model.add(Dropout(0.5))
    model.add(MaxPooling2D())
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    # model.add(Flatten())

    model.add(Dropout(0.5))


    model.add(Dense(10, activation='softmax'))
    model.summary()



# def multi_input_models():
#     """构建多输入模型"""
#     model = Sequential()
#
#     model.add(Conv2D(filters=32, kernel_size=(12,12), strides=(1, 1), padding='same', input_shape=(224, 224, 1),
#     activation = 'relu'))
#     # model.add(BatchNormalization())
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#
#
#     model.add(Conv2D(64, kernel_size=(12, 12), strides=(1, 1), padding='valid', activation='relu'))
#     # model.add(BatchNormalization())
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#
#     model.add(Conv2D(128, kernel_size=(12, 12), strides=(1, 1), padding='valid', activation='relu'))
#     # model.add(BatchNormalization())
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#
#     model.add(Conv2D(256, kernel_size=(12, 12), strides=(1, 1), padding='valid', activation='relu'))
#     # model.add(BatchNormalization())
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#
#
#     # model.add(Flatten())
#     #
#     #
#     # model.add(Dense(1024, activation='relu'))
#     # model.add(Dense(256, activation='relu'))
#
#     model.add(GlobalAveragePooling2D())
#     # model.add(BatchNormalization())
#
#     model.add(Dense(10, activation='softmax'))
#     model.summary()


multi_input_modelssd()




