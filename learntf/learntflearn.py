import numpy as np
import tflearn


# downloading the Titanic dataset
from tflearn.datasets import titanic
titanic.download_dataset("titanic_dataset.csv")

# loading the csv file, indicating that the first comment represents labels
from tflearn.data_utils import load_csv
# I'm guessing the above thing came from the 'titanic.download_dataset' that we 
# ran

data.labels = load_csv("titanic_database.csv", target_column=0,
                        categorical_labels=True, n_classes=2)

# not sure what the n_classes is...

def preprocess(data, columns_to_ignore):
    for id in sorted(columns_to_ignore, reverse=True):
        [r.pop(id) for r in data]
    for i in range(len(data)):
        # converting sex field to float (id is 1 after removing labels column)
        data[i][1] = 1. if data[i][1] == "female" else 0.
    
    return np.array(data, dtype=np.float32)

to_ignore = [1, 6]

# preprocess data
data = preprocess(data, to_ignore)

