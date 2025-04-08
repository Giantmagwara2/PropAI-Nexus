PropAI_Nexus/
├── api/
│   ├── models/
│   │   ├── rental_yield_predictor.json       # Pre-trained XGBoost model for rental yield
│   │   └── (Other models as needed)
│   ├── routes/
│   │   ├── rental_yield.py                   # Rental yield prediction API endpoints
│   │   ├── market_sentiment.py               # Market sentiment analysis API endpoints
│   │   └── rag.py                          # Retrieval-Augmented Generation (RAG) endpoints
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── RentalYieldPrediction.js      # React component for rental yield predictions
│   │   │   └── MarketSentiment.js            # React component for sentiment analysis
│   │   ├── context/
│   │   │   └── ThemeContext.js               # Dark mode and theming context
│   │   ├── App.js                            # Main React app integrating components
│   │   └── index.js                          # React entry point
│   ├── public/
│   │   └── index.html                        # HTML template
│   └── package.json
├── static/
│   └── css/
│       └── main.css                          # CSS for dark mode and responsive design
├── app.py                                    # Flask app initialization and route registration
├── app.yaml                                  # Google App Engine configuration
├── requirements.txt                          # Python dependencies
└── README.md
property_evaluation_agent/
├── config.py
├── main.py
├── data_sources/
│   ├── attom.py
│   ├── estated.py
│   ├── rentcast.py
│   ├── zoopla.py
├── utils/
│   └── api_helpers.py
└── models/
    └── valuation_model.py
