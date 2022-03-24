import np as np
from keras import Input, Model
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense


def build_model(SHAPE, nb_classes, bn_axis, seed=None):

    if seed:
        np.random.seed(seed)

    input_layer = Input(shape=SHAPE)

    # Step 1
    x = Conv2D(32, 3, 3, init='glorot_uniform', border_mode='same', activation='relu')(input_layer)
    # Step 2 - Pooling
    x = MaxPooling2D(pool_size=(2, 2))(x)

    # Step 1
    x = Conv2D(48, 3, 3, init='glorot_uniform', border_mode='same', activation='relu')(x)
    # Step 2 - Pooling
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Dropout(0.25)(x)

    # Step 1
    x = Conv2D(64, 3, 3, init='glorot_uniform', border_mode='same', activation='relu')(x)
    # Step 2 - Pooling
    x = MaxPooling2D(pool_size=(2, 2))(x)

    # Step 1
    x = Conv2D(96, 3, 3, init='glorot_uniform', border_mode='same', activation='relu')(x)
    # Step 2 - Pooling
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Dropout(0.25)(x)

    # Step 3 - Flattening
    x = Flatten()(x)

    # Step 4 - Full connection

    x = Dense(output_dim=256, activation='relu')(x)
    # Dropout
    x = Dropout(0.5)(x)

    x = Dense(output_dim=2, activation='softmax')(x)

    model = Model(input_layer, x)

    return model