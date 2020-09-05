from sklearn.metrics import r2_score

# the function to test the performance of the model using R2 value
def test_model(Y_test, X_test, model):
    Y_pred = model.predict(X_test)
    print("R2 value:\t{:0.3f}".format(r2_score(Y_test, Y_pred)))
