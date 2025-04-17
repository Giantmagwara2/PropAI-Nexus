# api/routes/rental_yield.py
from flask import Blueprint, request, jsonify
import xgboost as xgb
import pandas as pd

rental_yield_api = Blueprint('rental_yield_api', __name__)

# Load a placeholder XGBoost model (replace with your actual trained model)
model = xgb.XGBRegressor()
try:
    model.load_model('api/models/rental_yield_predictor.json')
except Exception as e:
    print("Model loading failed:", e)

@rental_yield_api.route('/predict/rental-yield', methods=['POST'])
def predict_rental_yield():
    try:
        data = request.json
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        response = {'predicted_rental_yield': round(prediction * 100, 2)}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
