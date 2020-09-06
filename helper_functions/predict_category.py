import pandas as pd
import numpy as np


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
    prediction = np.argmax(prediction[0])
    # get the inverse transform of the prediction using the encoder
    prediction = encoder.inverse_transform([prediction])
    # return the value
    return prediction[0]
