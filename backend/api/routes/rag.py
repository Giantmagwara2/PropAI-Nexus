from flask import Blueprint, request, jsonify
from transformers import pipeline

rag_api = Blueprint('rag_api', __name__)

# Initialize a text-generation pipeline for Retrieval-Augmented Generation (RAG)
rag_generator = pipeline("text-generation", model="gpt2")

@rag_api.route('/insights', methods=['POST'])
def generate_insights():
    try:
        data = request.json
        query = data.get('query', 'Provide insights on the current real estate market.')
        # For demonstration, generate text based on the query (this simulates a RAG process)
        generated = rag_generator(query, max_length=150, num_return_sequences=1)[0]['generated_text']
        return jsonify({'query': query, 'insights': generated}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
