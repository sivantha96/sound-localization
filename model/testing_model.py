import pandas as pd
from keras.models import model_from_json

# import helper functions
from helper_functions import get_encoder
from helper_functions import predict_category

# set the categories
categories = pd.DataFrame(['Iris-virginica', 'Iris-setosa', 'Iris-versicolor'])

# get the encoder
encoder = get_encoder(categories)

# open model.json
json_file = open('model.json', 'r')
model_json = json_file.read()
json_file.close()

# load model
model = model_from_json(model_json)
model.load_weights("model.h5")

# compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# print the prediction
print(predict_category(model, encoder, 5.1, 3.5, 1.4))