from flask import Blueprint, request, jsonify
from textblob import TextBlob

market_sentiment_api = Blueprint('market_sentiment_api', __name__)

@market_sentiment_api.route('/analyze/sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        articles = request.json.get('articles', [])
        results = []

        for article in articles:
            content = article.get('content', '')
            blob = TextBlob(content)
            polarity = blob.sentiment.polarity
            sentiment = 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'

            results.append({
                'title': article.get('title'),
                'sentiment_score': round(polarity, 2),
                'sentiment': sentiment
            })

        return jsonify(results), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
