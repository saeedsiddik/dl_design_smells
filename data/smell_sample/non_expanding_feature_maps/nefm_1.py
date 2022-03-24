# https://stackoverflow.com/questions/50426349/input-0-is-incompatible-with-layer-conv2d-121-expected-ndim-4-found-ndim-5
from keras.layers import Conv2D
from keras.models import Sequential

if __name__ == '__main__':
    model = Sequential()
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(50000, 32, 32, 1)))
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same', strides=2))
    model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))

    model.add(Conv2D(512, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    # model.add(UpSampling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    # model.add(UpSampling2D((2, 2)))
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(2, (3, 3), activation='tanh', padding='same'))
    # model.add(UpSampling2D((2, 2)))

    model.compile(optimizer='rmsprop', loss='mse')
    model_info = model.fit(X_train, Y_train,
                           batch_size=128, epochs=200)