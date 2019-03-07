from scipy.misc import imread
import numpy as np
import pandas as pd
import os
root = './gestures'

# going through each directory in the root folder given above
for directory, subdirectories, files in os.walk(root):
# going through each file in that directory
    for file in files:
    # reading the image file and extracting pixels
        print(file)
        im = imread(os.path.join(directory,file))
        value = im.flatten()
        value = np.hstack((directory[8:],value))
        df = pd.DataFrame(value).T
        df = df.sample(frac=1) # shuffle the dataset
        with open('train.csv', 'a') as dataset:
            df.to_csv(dataset, header=False, index=False)