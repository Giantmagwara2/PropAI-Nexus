from flask import Blueprint, request, jsonify
import redis
import json
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

knowledge_base = Blueprint('knowledge_base', __name__)

# Connect to Redis to simulate our knowledge base storage
try:
    r = redis.Redis(host='localhost', port=6379, db=0)
except redis.RedisError as e:
    logger.error(f"Failed to connect to Redis: {e}")
    r = None

@knowledge_base.route('/data', methods=['GET'])
def get_market_data():
    """
    Retrieve the latest market data from Redis.
    """
    try:
        if not r:
            raise redis.RedisError("Redis connection is not available.")
        
        # Retrieve latest market data
        data = r.get('latest_market_data')
        if data:
            market_data = json.loads(data)
        else:
            market_data = {}
        
        return jsonify(market_data), 200
    except redis.RedisError as e:
        logger.error(f"Redis error: {e}")
        return jsonify({"error": f"Redis error: {str(e)}"}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@knowledge_base.route('/data', methods=['POST'])
def update_knowledge_base():
    """
    Update the knowledge base with new market data.
    """
    try:
        if not r:
            raise redis.RedisError("Redis connection is not available.")
        
        data = request.json
        if not data or not isinstance(data, dict):
            return jsonify({"error": "Invalid data format. Expected a JSON object."}), 400
        
        # Store the data in Redis as the latest market data
        r.set('latest_market_data', json.dumps(data))
        logger.info("Knowledge base updated successfully.")
        
        return jsonify({"message": "Knowledge base updated", "data": data}), 200
    except redis.RedisError as e:
        logger.error(f"Redis error: {e}")
        return jsonify({"error": f"Redis error: {str(e)}"}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
