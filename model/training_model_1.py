import pandas as pd
import sklearn
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from matplotlib import pyplot as plt
import numpy as np
from numpy import argmax

# the function used to predict categories
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
    hist_dict = hist.history
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

# load dataset
df = pd.read_csv('C:/sound.csv')

# split dataset for training and testing
df_train, df_test = train_test_split(df, test_size=0.2)

# training data input-X output-Y
X_train = df_train[["A", "B", "C"]].copy()
Y_train = df_train[["DIRECTION"]].copy()

# testing data input-X output-Y
X_test = df_test[["A", "B", "C"]].copy()
Y_test = df_test[["DIRECTION"]].copy()

# defining one-hot encoder
encoder = LabelEncoder()
encoder.fit(np.ravel(Y_train))

# coverting training output to one-hot representation
encoded_Y_train = encoder.transform(np.ravel(Y_train))
Y_train = np_utils.to_categorical(encoded_Y_train)

# coverting testing output to one-hot representation
encoded_Y_test = encoder.transform(np.ravel(Y_test))
Y_test = np_utils.to_categorical(encoded_Y_test)

# defining the deep learning model model
model = Sequential()
model.add(Dense(8, input_dim=3, activation='relu'))
model.add(Dense(3, activation='softmax'))

# compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the model and save the history
hist = model.fit(X_train, Y_train, epochs=1000, verbose=0)

# test the performance of the model
test_model(Y_test, X_test, model)

# print the prediction
print(predict_category(model, encoder, 5.1, 3.5, 1.4))

# plot the loss of the training proccess
plot_history(hist)
