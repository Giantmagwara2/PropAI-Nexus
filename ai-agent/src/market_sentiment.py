# src/market_sentiment.py

from textblob import TextBlob
import requests

def analyze_news_sentiment(news_articles):
    sentiments = []
    for article in news_articles:
        blob = TextBlob(article['content'])
        polarity = blob.sentiment.polarity
        sentiments.append({
            'title': article['title'],
            'sentiment_score': polarity
        })
    return sentiments

def fetch_sample_news():
    # Dummy function - replace with news API
    return [
        {'title': 'Property prices are booming in Cape Town!', 'content': 'Experts predict growth of 10% in the next year.'},
        {'title': 'Rental demand plunges in Joburg CBD.', 'content': 'Tenants are moving to suburban areas due to safety concerns.'}
    ]

if __name__ == '__main__':
    news = fetch_sample_news()
    sentiment_results = analyze_news_sentiment(news)
    print(sentiment_results)
