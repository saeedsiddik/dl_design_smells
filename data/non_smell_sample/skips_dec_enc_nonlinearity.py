import tensorflow as tf

def get_conv(x):
  # 112,112,3
  x = tf.keras.layers.Conv2D(filters=16,kernel_size=(3,3),padding='same')(x)
  x = tf.keras.layers.BatchNormalization()(x)
  x1 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Conv2D(filters=16,kernel_size=(3,3),padding='same')(x1)
  x = tf.keras.layers.BatchNormalization()(x)
  x2 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Add()([x1,x2])
  x56 = tf.keras.layers.MaxPool2D()(x)
  # 56,56,16
  x = tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3),padding='same')(x56)
  x = tf.keras.layers.BatchNormalization()(x)
  x1 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3),padding='same')(x1)
  x = tf.keras.layers.BatchNormalization()(x)
  x2 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Add()([x1,x2])
  x28 = tf.keras.layers.MaxPool2D()(x)
  # 28,28,32
  x = tf.keras.layers.Conv2D(filters=64,kernel_size=(3,3),padding='same')(x28)
  x = tf.keras.layers.BatchNormalization()(x)
  x1 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Conv2D(filters=64,kernel_size=(3,3),padding='same')(x1)
  x = tf.keras.layers.BatchNormalization()(x)
  x2 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Add()([x1,x2])
  x14 = tf.keras.layers.MaxPool2D()(x)
  # 14,14,64
  x = tf.keras.layers.Conv2D(filters=128,kernel_size=(3,3),padding='same')(x14)
  x = tf.keras.layers.BatchNormalization()(x)
  x1 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Conv2D(filters=128,kernel_size=(3,3),padding='same')(x1)
  x = tf.keras.layers.BatchNormalization()(x)
  x2 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Add()([x1,x2])
  x = tf.keras.layers.MaxPool2D()(x)
  # 7,7,128
  return x,x14,x28,x56

def get_encoder(input1,input2,input3,input4):
  conv1,c1_x14,c1_x28,c1_x56 = get_conv(input1)
  conv2,c2_x14,c2_x28,c2_x56 = get_conv(input2)
  conv3,c3_x14,c3_x28,c3_x56 = get_conv(input3)
  conv4,c4_x14,c4_x28,c4_x56 = get_conv(input4)

  x1 = tf.keras.layers.GlobalAveragePooling2D()(conv1)
  x2 = tf.keras.layers.GlobalAveragePooling2D()(conv2)
  x3 = tf.keras.layers.GlobalAveragePooling2D()(conv3)
  x4 = tf.keras.layers.GlobalAveragePooling2D()(conv4)

  x = tf.concat([x1,x2,x3,x4], axis=1)
  x = tf.keras.layers.Dense(6272, activation='relu', use_bias=False)(x)

  x14 = tf.keras.layers.Add()([c1_x14,c2_x14,c3_x14,c4_x14])
  x28 = tf.keras.layers.Add()([c1_x28,c2_x28,c3_x28,c4_x28])
  x56 = tf.keras.layers.Add()([c1_x56,c2_x56,c3_x56,c4_x56])
  return x, x14, x28, x56

def get_decoder(latent_space,x14, x28, x56):
  x = tf.keras.layers.Reshape((7,7,128))(latent_space)
  # 7,7,128
  x = tf.keras.layers.Conv2D(filters=64,kernel_size=(3,3),padding='same')(x)
  x = tf.keras.layers.BatchNormalization()(x)
  x1 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Conv2D(filters=64,kernel_size=(3,3),padding='same')(x1)
  x = tf.keras.layers.BatchNormalization()(x)
  x2 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Add()([x1,x2])
  x = tf.keras.layers.UpSampling2D()(x)
  # 14,14,64
  x14 = tf.keras.layers.Conv2D(filters=64,kernel_size=(1,1),padding='valid',activation='relu')(x14)
  x = tf.keras.layers.Add()([x,x14]) # From encoder

  x = tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3),padding='same')(x)
  x = tf.keras.layers.BatchNormalization()(x)
  x1 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3),padding='same')(x1)
  x = tf.keras.layers.BatchNormalization()(x)
  x2 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Add()([x1,x2])
  x = tf.keras.layers.UpSampling2D()(x)
  # 28,28,32
  x28 = tf.keras.layers.Conv2D(filters=32,kernel_size=(1,1),padding='valid',activation='relu')(x28)
  x = tf.keras.layers.Add()([x,x28]) # From encoder

  x = tf.keras.layers.Conv2D(filters=16,kernel_size=(3,3),padding='same')(x)
  x = tf.keras.layers.BatchNormalization()(x)
  x1 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Conv2D(filters=16,kernel_size=(3,3),padding='same')(x1)
  x = tf.keras.layers.BatchNormalization()(x)
  x2 = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.Add()([x1,x2])
  x = tf.keras.layers.UpSampling2D()(x)
  # 56,56,16
  x56 = tf.keras.layers.Conv2D(filters=16,kernel_size=(1,1),padding='valid',activation='relu')(x56)
  x = tf.keras.layers.Add()([x,x56]) # From encoder

  x = tf.keras.layers.Conv2D(filters=3,kernel_size=(3,3),padding='same')(x)
  x = tf.keras.layers.BatchNormalization()(x)
  x = tf.keras.layers.ReLU()(x)
  x = tf.keras.layers.UpSampling2D()(x)
  return x

def get_autoencoder():
  input1 = tf.keras.layers.Input((112, 112, 3))
  input2 = tf.keras.layers.Input((112, 112, 3))
  input3 = tf.keras.layers.Input((112, 112, 3))
  input4 = tf.keras.layers.Input((112, 112, 3))

  latent_space, x14,x28,x56 = get_encoder(input1,input2,input3,input4)
  decoded_img = get_decoder(latent_space,x14, x28, x56)
  autoencoder = tf.keras.Model(inputs=[input1,input2,input3,input4], outputs=decoded_img)
  return autoencoder
