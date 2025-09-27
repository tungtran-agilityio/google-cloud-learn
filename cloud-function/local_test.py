#!/usr/bin/env python3
"""
Local testing script for the Text Processing Cloud Function
This allows you to test the function locally before deploying
"""

from main import process_text
from flask import Flask, request as flask_request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def local_handler():
    return process_text(flask_request)

@app.route('/health', methods=['GET'])
def health():
    return '{"status": "healthy", "service": "text-processing-function"}', 200, {
        'Content-Type': 'application/json'
    }

if __name__ == "__main__":
    print("Starting local development server...")
    print("Available endpoints:")
    print("  GET  /?text=your_text&operation=analysis")
    print("  POST / with JSON body: {\"text\": \"your_text\", \"operation\": \"analysis\"}")
    print("  GET  /health")
    print("\nOperations: analysis, transform, validate, readability, all")
    print("Transform types: uppercase, lowercase, title, reverse, reverse_words, etc.")
    
    app.run(host='0.0.0.0', port=8080, debug=True)
