from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam, SGD

import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from matplotlib import pyplot as plt

input_df = pd.read_excel("Output.xlsx", index_col=None, header=None)

x_train = input_df[["mic_1", "mic_2", "mic_3"]].copy()
y_train = input_df[["direction"]].copy()

model_1 = Sequential()
model_1.add(Dense(9, input_dim=4, activation='relu'))
model_1.add(Dense(1, activation='sigmoid'))
model_1.summary()

Optimizer = SGD(lr=0.1)
model_1.compile(optimizer=Optimizer, loss='mean_squared_error')

fitted_model_1 = model_1.fit(x_train, y_train, epochs=1000, verbose=1)

history_model_1 = fitted_model_1.history
loss_model_1 = history_model_1['loss']

plt.figure()
plt.plot(loss_model_1, 'b')
plt.legend(['Training'])
plt.ylabel("Training loss")
plt.xlabel("Epochs")
plt.show()
