# src/model_train.py

import pandas as pd
import os
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

PROCESSED_DATA_DIR = 'data/processed'

def load_data(file_name):
    path = os.path.join(PROCESSED_DATA_DIR, file_name)
    return pd.read_csv(path)

def train_model():
    df = load_data('property_data_features.csv')

    # Target: Price Prediction Example
    X = df.drop(['price'], axis=1)
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    rmse = mean_squared_error(y_test, preds, squared=False)

    print(f'✅ Model trained. RMSE: {rmse:.2f}')

    # Save the model
    model.save_model('property_value_predictor.json')
    print("✅ Model saved.")

if __name__ == '__main__':
    train_model()
