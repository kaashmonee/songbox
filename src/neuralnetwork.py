import tensorflow as tf

class NeuralNetwork:

    def __init__(self):
        # creating a neural network to train data gathered from facial features
        self.X = tf.placeholder(tf.float32, [None, 28, 28, 1])
        # learning training for mnist dataset, where images are 28x28
        # None is the number of images in the batch, and that is unkown at this time; 
        # will be known during time of training

        self.W = tf.Variable(tf.zeros([784, 10]))
        self.b = tf.Variable(tf.zeros([10]))

        self.init = tf.initialize_all_variables()

    def buildModel(self):
        tf.nn.softmax(tf.matmul(tf.reshape(self.X)))


print("Running till here!")