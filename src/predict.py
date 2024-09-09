import joblib
import pandas as pd

def load_model():
    return joblib.load('models/model.pkl')

def predict(model, X):
    return model.predict(X)
