import numpy as np
import tflearn


# downloading the Titanic dataset
from tflearn.datasets import titanic

titanicDatabasePath = "learntf/titanic_dataset.csv"
titanic.download_dataset(titanicDatabasePath)

# loading the csv file, indicating that the first comment represents labels
from tflearn.data_utils import load_csv
# I'm guessing the above thing came from the 'titanic.download_dataset' that we 
# ran

data, labels = load_csv(titanicDatabasePath, target_column=0,
                        categorical_labels=True, n_classes=2)

# not sure what the n_classes is...

def preprocess(data, columns_to_ignore):
    for id in sorted(columns_to_ignore, reverse=True):
        # [r.pop(id) for r in data]
        for r in data: r.pop(id)
    for i in range(len(data)):
        # converting sex field to float (id is 1 after removing labels column)
        data[i][1] = 1. if data[i][1] == "female" else 0.
    
    return np.array(data, dtype=np.float32)

to_ignore = [1, 6]

# preprocess data
data = preprocess(data, to_ignore)

# build a 3 layer neural network using tflearn
net = tflearn.input_data(shape=[None, 6]) # the None means that we don't know 
# how many things are going to be in the inputted data
# the 6 indicates the number of features

net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation="softmax")
net = tflearn.regression(net)


# writing the CNN model
model = tflearn.DNN(net)

# starting to train and applying gradient descent algorithm
model.fit(data, labels, n_epoch=10, batch_size=16, show_metric=True)


dicaprio = [3, "Jack Dawson", "male", 19, 0, 0, "N/A", 5.0000]
winslet = [1, "Rose DeWitt Bukater", "female", 17, 1, 2, "N/A", 100.0000]
# preprocess data

dicaprio, winslet = preprocess([dicaprio, winslet], to_ignore)

pred = model.predict([dicaprio, winslet])
print("\nDicaprio surviving rate:", pred[0][1])
print("Winslet surviving rate:", pred[1][1])
