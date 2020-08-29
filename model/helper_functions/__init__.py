# the function used to predict categories
import pandas as pd
import numpy as np
from numpy import argmax
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder

def predict_category(model, encoder, val_A, val_B, val_C):
    # define a dataframe from values
    df = pd.DataFrame([val_A, val_B, val_C])
    # transpose it to get the shape (4,1)
    df = df.transpose()
    # prediction - returns an array of predictions (but here, it contains only one element)
    prediction = model.predict(df)
    # round the values of the array to integers
    prediction.round(decimals=0)
    # get the maximum value along an axis of the first element (since it only has one element)
    prediction = argmax(prediction[0])
    # get the inverse transform of the prediction using the encoder
    prediction = encoder.inverse_transform([prediction])
    # return the value
    return prediction[0]

# the function to plot the loss of the training process
def plot_history(history):
    hist_dict = history.history
    loss_reg = hist_dict['loss']
    plt.figure()
    plt.plot(loss_reg, 'b')
    plt.legend(['Training'])
    plt.ylabel("Training loss")
    plt.xlabel("Epoch")
    plt.draw()
    plt.show()

# the function to test the performance of the model using R2 value
def test_model(Y_test, X_test, model):
    Y_pred = model.predict(X_test)
    print("R2 value:\t{:0.3f}".format(r2_score(Y_test, Y_pred)))

# the function to save the model architecture and the trained weights to the disk
def save_model(model):
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model.h5")
    print("Saved model to disk")

def get_encoder(Y):
    encoder = LabelEncoder()
    encoder.fit(np.ravel(Y))
    return encoder