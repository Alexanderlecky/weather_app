from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib

def train_model(historical_data):
    # Assuming historical_data is a DataFrame with features and target
    X = historical_data.drop('target', axis=1)
    y = historical_data['target']
    model = RandomForestRegressor()
    model.fit(X, y)
    joblib.dump(model, 'models/weather_model.pkl')

def predict_weather(model, input_data):
    prediction = model.predict(input_data)
    return prediction