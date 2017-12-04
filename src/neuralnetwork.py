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
        # builds the model
        # this reshapes self.X into a 2d tensor, multiplies it by the weights 
        # function, and adds the biases
        # after adding the biases, applies the softmax activation function
        # you can think of the activation function as the function required to 
        # activate the neuron 
        Y = tf.nn.softmax(tf.matmul(tf.reshape(self.X, [-1, 784]), W) + b)
        print("Y:", Y)
        sys.exit()
        # placeholder for the correct labels
        Y_ = tf.placeholder(tf.float32, [None, 10])

        # loss function
        crossEntropy = -tf.reduce_sum(Y * tf.log(Y))

        # % of correct answers found in the batch
        isCorrect = tf.equal(tf.argmax(Y, 1), tf.argmax(Y_, 1))
        accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))



n = NeuralNetwork()
n.buildModel()


class NeuralNetwork:
    
    def buildNetwork(self):
        pass
        # code to buildModel
    
    def train(self):
        # train model
    
    def test(self, test):
        return trainedValue # this is what I imagine such a neural network might
        # look like