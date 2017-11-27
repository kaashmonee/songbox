import tensorflow as tf

# creating a neural network to train data gathered from facial features
X = tf.placeholder(tf.float32, [None, 28, 28, 1])
# learning training for mnist dataset, where images are 28x28
# None is the number of images in the batch, and that is unkown at this time; 
# will be known during time of training

W = tf.Variable(tf.zeroes([784, 10]))
b = tf.Variable(tf.zeroes([10]))
print("Running till here!")