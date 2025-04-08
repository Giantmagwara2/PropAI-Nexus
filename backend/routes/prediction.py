from flask import Blueprint, request, jsonify
from models.predictive_model import predict_property_value

prediction_bp = Blueprint('prediction_bp', __name__)

@prediction_bp.route('/property', methods=['POST'])
def property_prediction():
    data = request.get_json()
    features = data.get("features", {})
    predicted_value = predict_property_value(features)
    return jsonify({"predicted_value": predicted_value})
