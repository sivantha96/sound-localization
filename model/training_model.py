import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import sys
sys.path.append('C:/Users/Sivantha_112068/Documents/Projects/sound-localization')

# import helper functions
from helper_functions import save_model, plot_history, predict_category, test_model, get_encoder

# set the categories
categories = pd.DataFrame(['AC', 'AB', 'BC'])

# load dataset
df = pd.read_csv('C:/sound.csv')

# get the encoder
encoder = get_encoder(categories)

# split dataset for training and testing
df_train, df_test = train_test_split(df, test_size=0.2)

# training data input-X output-Y
X_train = df_train[["A", "B", "C"]].copy()
Y_train = df_train[["DIRECTION"]].copy()

# testing data input-X output-Y
X_test = df_test[["A", "B", "C"]].copy()
Y_test = df_test[["DIRECTION"]].copy()

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
# print(predict_category(model, encoder, 5.6, 3, 4.5))

# plot the loss of the training proccess
plot_history(hist)

# save the model and weights
save_model(model)
