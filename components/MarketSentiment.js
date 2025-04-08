// components/MarketSentiment.js

import React, { useState } from 'react';
import axios from 'axios';

export default function MarketSentiment() {
  const [articles, setArticles] = useState([{ title: '', content: '' }]);
  const [sentiments, setSentiments] = useState([]);

  const handleChange = (index, field, value) => {
    const newArticles = [...articles];
    newArticles[index][field] = value;
    setArticles(newArticles);
  };

  const analyzeSentiment = async () => {
    try {
      const response = await axios.post('/api/analyze/sentiment', { articles });
      setSentiments(response.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="bg-white dark:bg-gray-800 shadow-md rounded-xl p-6">
      <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-4">Market Sentiment Analyzer</h2>

      {articles.map((article, idx) => (
        <div key={idx} className="mb-4">
          <input
            value={article.title}
            onChange={(e) => handleChange(idx, 'title', e.target.value)}
            placeholder="Title"
            className="mb-2 p-2 w-full rounded"
          />
          <textarea
            value={article.content}
            onChange={(e) => handleChange(idx, 'content', e.target.value)}
            placeholder="Content"
            className="mb-2 p-2 w-full rounded"
          />
        </div>
      ))}

      <button onClick={analyzeSentiment} className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
        Analyze Sentiment
      </button>

      {sentiments.length > 0 && (
        <div className="mt-4 space-y-2">
          {sentiments.map((s, idx) => (
            <div key={idx} className="text-gray-900 dark:text-white">
              <strong>{s.title}</strong>: {s.sentiment} ({s.sentiment_score})
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
