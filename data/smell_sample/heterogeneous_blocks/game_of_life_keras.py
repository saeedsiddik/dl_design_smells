# https://gist.github.com/Denbergvanthijs/a634d249e8784e340aa8d5d90d527711
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from matplotlib.animation import FuncAnimation
from tensorflow.keras.layers import Conv2D, InputLayer, Layer
from tensorflow.keras.models import Sequential

size = 128
n_frames = 240
full_size = (1, size, size, 1)

env = np.random.randint(0, 2, full_size)

# env = np.zeros(full_size, dtype=int)
# glider = ((1, 2), (2, 3), (3, 1), (3, 2), (3, 3))
# for pos in glider:
#     env[(0,) + pos] = 1


class TorusPaddingLayer(Layer):
    def __init__(self, **kwargs):
        """Based on: https://stackoverflow.com/questions/39088489/tensorflow-periodic-padding"""
        super(TorusPaddingLayer, self).__init__(**kwargs)
        top_row = np.zeros((1, size))
        bottom_row = np.zeros((1, size))
        top_row[0, -1] = 1
        bottom_row[-1, 0] = 1

        self.pre = tf.convert_to_tensor(np.vstack((top_row, np.eye(size), bottom_row)), dtype=tf.float32)
        self.pre = tf.expand_dims(self.pre, 0)
        self.pre = tf.expand_dims(self.pre, -1)
        self.pre_T = tf.transpose(self.pre)

    def call(self, inputs):
        """Matrix product of three matrices of shape (1, size, size, 1) while keeping outer dimensions."""
        return tf.einsum("abcd,ecfg,hfij->abij", self.pre, inputs, self.pre_T)


def kernel(shape, dtype=None):
    kernel = np.ones(shape)
    kernel[1, 1] = 0  # Don't count the cell itself in the number of neighbours
    return tf.convert_to_tensor(kernel, dtype=dtype)


# convolve2d of scipy does support torus-padding but that's obviously not as cool as a neural network
model = Sequential([InputLayer(input_shape=full_size[1:]),
                    TorusPaddingLayer(),
                    Conv2D(1, 3, padding="valid", activation=None, use_bias=False, kernel_initializer=kernel)])

frames = []
for i in range(n_frames):
    neighbours = model(env)
    env = np.where((env & np.isin(neighbours, (2, 3))) | ((env == 0) & (neighbours == 3)), 1, 0)
    frames.append(env.squeeze())


fig = plt.figure(figsize=(6, 6))
ax = plt.axes(xlim=(0, size), ylim=(0, size))
render = plt.imshow(frames[0], interpolation="none", cmap="binary")


def animate(i: int):
    render.set_array(frames[i])
    return [render]


anim = FuncAnimation(fig, animate, frames=n_frames, interval=30, blit=True)
plt.axis("off")
plt.gca().invert_yaxis()
anim.save("glider.gif", fps=30)
plt.show()
