# api/routes/knowledge_base.py
from flask import Blueprint, request, jsonify
import redis
import json

knowledge_base_api = Blueprint('knowledge_base_api', __name__)

# Connect to Redis (make sure Redis is running; in production, use a proper database)
r = redis.Redis(host='localhost', port=6379, db=0)

@knowledge_base_api.route('/data', methods=['GET'])
def get_market_data():
    try:
        data = r.get('latest_market_data')
        if data:
            market_data = json.loads(data)
        else:
            market_data = {}
        return jsonify(market_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@knowledge_base_api.route('/data', methods=['POST'])
def update_market_data():
    try:
        data = request.json
        r.set('latest_market_data', json.dumps(data))
        return jsonify({"message": "Knowledge base updated", "data": data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
