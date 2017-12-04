import tensorflow as tf
import sys

class NeuralNetwork:

    def __init__(self):
        # creating a neural network to train data gathered from facial features
        self.X = tf.placeholder(tf.float32, [None, 28, 28, 1], shape=())
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
        Y = tf.nn.softmax(tf.matmul(tf.reshape(self.X, [-1, 784]), self.W) + self.b)
        print("Y:", Y)
        sys.exit()
        # placeholder for the correct labels
        Y_ = tf.placeholder(tf.float32, [None, 10], shape=())

        # loss function
        # this is the function we are trying to minimize with gradient descent
        # Y*tf.log(Y) is 
        crossEntropy = -tf.reduce_sum(Y_ * tf.log(Y))

        # % of correct answers found in the batch
        # not 100% sure how these work, so will skip for now
        isCorrect = tf.equal(tf.argmax(Y, 1), tf.argmax(Y_, 1))
        accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

        # this will 
        optimizer = tf.train.GradientDescentOptimizer(0.003)
        trainStep = optimizer.minimize(crossEntropy)
        print("Type of trainstep:", type(trainStep))
        print("optimizer.minimize", trainStep)
        
        # init
        # initializes global variables in the graph
        # how to handle this if we don't have global variables?
        init = tf.global_variables_initializer()
        sess = tf.Session()
        sess.run(init)

    def trainingStep(i, updateTestData, updateTrainData):
        
        # loading the images and the correct answers
        # they're being trained in batches of 100
        batchX, batchY = mnist.train.next_batch(100)
        trainData = {X: batchX, Y_: batchY}

        # training!
        # if updateTrainData is not None or False,
        if updateTrainData:
            # not exactly sure what a, c, im, w, and b are.
            a, c, im, w, b = sess.run([accuracy, crossEntropy, I, allweights, 
                                       allbiases], feed_dict={X: batchX, 
                                                              Y_: batchY})

        sess.run(trainStep, feed_dict=trainData)



def main():
    n = NeuralNetwork()
    n.buildModel()

if __name__ == "__main__":
    main()