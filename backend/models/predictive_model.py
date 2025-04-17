# /backend/models/predictive_model.py

import numpy as np
import pandas as pd
import joblib
import os

# Load the trained property value prediction model
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'property_value_model.pkl')
property_model = joblib.load(model_path)

def predict_property_value(features: dict) -> float:
    """
    Predicts the property value based on input features.

    Args:
        features (dict): A dictionary of property features.

    Returns:
        float: Predicted property value.
    """
    try:
        # Prepare DataFrame
        df = pd.DataFrame([features])
        if "country" in df.columns:
            df = df.drop(columns=["country"])
        if "currency" in df.columns:
            df = df.drop(columns=["currency"])

        # Ensure feature alignment
        df = pd.get_dummies(df)
        df = df.reindex(columns=property_model.feature_names_in_, fill_value=0)

        # Predict
        prediction = property_model.predict(df)[0]
        return round(float(prediction), 2)
    
    except Exception as e:
        # In production, proper logging should be here
        print(f"Prediction error: {e}")
        return np.nan
