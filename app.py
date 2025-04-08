# app.py

from flask import Flask, jsonify
from api.routes.rental_yield import rental_yield_api
from api.routes.market_sentiment import market_sentiment_api
from api.routes.knowledge_base import knowledge_base_api
from api.routes.property_evaluation import property_eval_api
from agents.market_analysis import publish_market_insights

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(rental_yield_api, url_prefix='/api')
app.register_blueprint(market_sentiment_api, url_prefix='/api')
app.register_blueprint(knowledge_base_api, url_prefix='/kb')
app.register_blueprint(property_eval_api, url_prefix='/api')

# Endpoint to trigger Market Analysis Agent update
@app.route('/agent/market/update', methods=['POST'])
def update_market():
    try:
        publish_market_insights()
        return jsonify({"message": "Market data updated and published."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return "PropAI Nexus Multi-Agent System is Live!"

if __name__ == '__main__':
    app.run(debug=True)
