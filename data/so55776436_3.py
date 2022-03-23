model = Sequential()
model.add(Dense(128, input_dim=dims, activation='relu'))
model.add(Dropout(0.2))
model.add(layers.BatchNormalization())
model.add(Dense(16, activation='relu', kernel_initializer='normal', kernel_regularizer=regularizers.l1(x)))
model.add(Dropout(0.2))
model.add(layers.BatchNormalization())
model.add(Dense(1, kernel_initializer='normal'))

model.compile(optimizer=optimizers.adam(lr=l), loss='mean_squared_error')

reduce_lr = ReduceLROnPlateau(monitor='val_loss', mode='min', factor=0.5, patience=3, min_lr=0.000001, verbose=1, cooldown=0)

history = model.fit(xtrain, ytrain, epochs=epochs, batch_size=batch_size, validation_split=0.3, callbacks=[reduce_lr])