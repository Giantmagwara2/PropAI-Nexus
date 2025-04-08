from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_cors import CORS
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
import logging
import sqlite3
import os
import numpy as np
import pickle
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

# Import our authentication module (defined in auth.py)
from auth import User, get_user_by_id, get_user_by_username, register_user

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "supersecretkey")
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Database file name
DATABASE = os.environ.get('DATABASE_NAME', 'propai_nexus.db')

# Load ML models (placeholders)
MODEL_PATH = os.path.join('models', 'price_prediction_model.pkl')
RECOMMEND_MODEL_PATH = os.path.join('models', 'recommendation_model.pkl')

try:
    with open(MODEL_PATH, 'rb') as f:
        price_model = pickle.load(f)
    logger.info("Price prediction model loaded.")
except Exception as e:
    logger.error("Failed to load price prediction model: %s", e)
    price_model = None

try:
    with open(RECOMMEND_MODEL_PATH, 'rb') as f:
        recommendation_model = pickle.load(f)
    logger.info("Recommendation model loaded.")
except Exception as e:
    logger.error("Failed to load recommendation model: %s", e)
    recommendation_model = None

# ---------------------------
# Flask-Login User Loader
# ---------------------------
@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)

# ---------------------------
# Helper: Database Connection
# ---------------------------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# ---------------------------
# Routes: Public Pages
# ---------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    from auth import get_user_by_username  # Import from auth module
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            # Check account lockout if implemented (omitted for brevity)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials. Please try again.")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form.get('role', 'user')
        register_user(username, password, role)
        flash("Registration successful. Please log in.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('index'))

# ---------------------------
# Routes: Protected Pages
# ---------------------------
@app.route('/dashboard')
@login_required
def dashboard():
    conn = get_db_connection()
    properties = conn.execute('SELECT * FROM properties ORDER BY timestamp DESC LIMIT 10').fetchall()
    conn.close()
    return render_template('dashboard.html', properties=properties, user=current_user)

# ---------------------------
# API Endpoints
# ---------------------------
@app.route('/api/predict', methods=['POST'])
def predict():
    if price_model is None:
        return jsonify({'error': 'Model unavailable'}), 500
    data = request.json
    try:
        features = np.array(data['features']).reshape(1, -1)
        prediction = price_model.predict(features)[0]
        return jsonify({'prediction': float(prediction)})
        
    except Exception as e:
        logger.error("Prediction error: %s", e)
        return jsonify({'error': 'Prediction failed'}), 500

@app.route('/api/recommend', methods=['POST'])
def recommend():
    if recommendation_model is None:
        return jsonify({'error': 'Recommendation model unavailable'}), 500
    user_preferences = request.json
    try:
        # Simulate recommendations
        recommendations = recommendation_model.recommend(user_preferences)
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        logger.error("Recommendation error: %s", e)
        return jsonify({'error': 'Recommendation failed'}), 500

# ---------------------------
# Error Handlers
# ---------------------------
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server error'}), 500

# ---------------------------
# Enforce CSP Header
# ---------------------------
@app.after_request
def set_csp(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://trusted.cdn.com"
    return response

# ---------------------------
# Application Entry Point
# ---------------------------
if __name__ == '__main__':
    # For local testing use HTTPS with self-signed certs (if desired)
    # app.run(host='0.0.0.0', port=8080, ssl_context=('server.crt', 'server.key'))
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
