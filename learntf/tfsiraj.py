import input_data

mnist = input_data.read_data_sets("/tmp/data", one_hot=True)

import tensorflow as tf

# setting parameters
learning_rate = 0.01
training_iteration = 30
batch_size = 100
display_step = 2

x = tf.placeholder("float", [None, 784])
y = tf.placeholder("float", [None, 10])

# creating a model

# set model weights
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

with tf.name_scope("Wx_b") as scope:
    # constructing a linear model
    # cost_function = 
    pass