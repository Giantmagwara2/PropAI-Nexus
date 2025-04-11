import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Dummy training data for illustration
def get_training_data():
    data = pd.DataFrame({
        'property_size': [1500, 2000, 1700],
        'year_built': [2000, 1995, 2010],
        'bedrooms': [3, 4, 3],
        'bathrooms': [2, 3, 2],
        'estimated_rent': [2000, 2500, 2200],
        'neighborhood_rent_avg': [1800, 2400, 2100],
        'price': [300000, 400000, 350000]
    })
    return data

def train_valuation_model():
    data = get_training_data()
    X = data.drop(columns=['price'])
    y = data['price']

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def predict_property_value(model, features):
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return prediction
