from sklearn.preprocessing import LabelEncoder
import numpy as np

# function to get the label encode to encode categorical label for training data
def get_encoder(Y):
    encoder = LabelEncoder()
    encoder.fit(np.ravel(Y))
    return encoder

def test():
    return True