from helper_functions import predict_category
from helper_functions import get_encoder
import pandas as pd
from keras.models import model_from_json
import sys
# sys.path.append('C:/Users/Sivantha_112068/Documents/Projects/sound-localization')
sys.path.append('/home/pi/Documents/Projects/sound-localization')

# import helper functions

# set the categories
categories = pd.DataFrame(['Iris-virginica', 'Iris-setosa', 'Iris-versicolor'])

# get the encoder
encoder = get_encoder(categories)

# open model.json
json_file = open('/home/pi/Documents/Projects/sound-localization/model.json', 'r')
model_json = json_file.read()
json_file.close()

# load model
model = model_from_json(model_json)
model.load_weights("/home/pi/Documents/Projects/sound-localization/model.h5")

# compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print("Model is ready")

vol_A = 4.0
vol_B = 2.2
vol_C = 0

# print the prediction
while True:
    print(vol_A, vol_B, vol_C)
    print(predict_category(model, encoder, vol_A, vol_B, vol_C))
    vol_A = vol_A + 0.003
    vol_B = vol_B + 0.007
    vol_C = vol_C + 0.01
