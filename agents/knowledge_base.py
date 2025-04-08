from flask import Blueprint, request, jsonify
import redis
import json

knowledge_base = Blueprint('knowledge_base', __name__)

# Connect to Redis to simulate our knowledge base storage
r = redis.Redis(host='localhost', port=6379, db=0)

@knowledge_base.route('/data', methods=['GET'])
def get_market_data():
    try:
        # Retrieve latest market data from the Redis channel (simulation)
        # In production, this would be a database query.
        data = r.get('latest_market_data')
        if data:
            market_data = json.loads(data)
        else:
            market_data = {}
        return jsonify(market_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Optional: Endpoint to update latest market data (simulate knowledge base update)
@knowledge_base.route('/data', methods=['POST'])
def update_knowledge_base():
    try:
        data = request.json
        # Store the data in Redis as the latest market data
        r.set('latest_market_data', json.dumps(data))
        return jsonify({"message": "Knowledge base updated", "data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
