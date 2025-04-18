# api/routes/property_evaluation.py

from flask import Blueprint, request, jsonify
from services.data_merger_service import merge_property_data

property_eval_api = Blueprint('property_eval_api', __name__)

@property_eval_api.route('/evaluate', methods=['POST'])
def evaluate_property():
    try:
        data = request.json
        attom_data = data.get('attom_data', {})
        estated_data = data.get('estated_data', {})
        rentcast_data = data.get('rentcast_data', {})
        zoopla_data = data.get('zoopla_data', {})

        merged_report = merge_property_data(attom_data, estated_data, rentcast_data, zoopla_data)
        return jsonify(merged_report), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
