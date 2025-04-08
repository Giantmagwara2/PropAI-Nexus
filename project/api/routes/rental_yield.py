from flask import Blueprint, request, jsonify
import xgboost as xgb
import pandas as pd

rental_yield_api = Blueprint('rental_yield_api', __name__)

# Load trained XGBoost model
model = xgb.XGBRegressor()
model.load_model('api/models/rental_yield_predictor.json')

@rental_yield_api.route('/predict/rental-yield', methods=['POST'])
def predict_rental_yield():
    try:
        data = request.json
        df = pd.DataFrame([data])

        # Predict rental yield
        prediction = model.predict(df)[0]

        response = {
            'predicted_rental_yield': round(prediction * 100, 2)
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
