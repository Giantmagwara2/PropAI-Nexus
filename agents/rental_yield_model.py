# src/rental_yield_model.py

import pandas as pd
import os
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

PROCESSED_DATA_DIR = 'data/processed'

def load_data(file_name):
    path = os.path.join(PROCESSED_DATA_DIR, file_name)
    return pd.read_csv(path)

def train_rental_yield_model():
    df = load_data('property_data_features.csv')

    # Assume we have 'annual_rent_income' and 'price'
    df['rental_yield'] = df['annual_rent_income'] / df['price']

    X = df.drop(['rental_yield', 'price', 'annual_rent_income'], axis=1)
    y = df['rental_yield']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    print(f'✅ Rental Yield Model Trained. MAE: {mae:.4f}')

    # Save model
    model.save_model('rental_yield_predictor.json')
    print("✅ Rental Yield Model saved.")

if __name__ == '__main__':
    train_rental_yield_model()
