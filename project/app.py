from flask import Flask
from api.routes.rental_yield import rental_yield_api
from api.routes.market_sentiment import market_sentiment_api

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(rental_yield_api, url_prefix='/api')
app.register_blueprint(market_sentiment_api, url_prefix='/api')

@app.route('/')
def index():
    return "AI Real Estate API is running!"

if __name__ == '__main__':
    app.run(debug=True)
