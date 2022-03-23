from keras.layers.normalization import BatchNormalization

model = Sequential()
model.add(Conv1D(100,2,activation='relu',input_shape=(18000,1))) 
model.add(Conv1D(10,2))
model.add(Dropout(0.5))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling1D(4))
model.add(Flatten())
model.add(Dense(6,activation='softmax'))
model.summary()