"""
Simple Demo API using Google Cloud Run
This service provides basic functionality without external dependencies
"""

import os
import json
import random
import math
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demo purposes
CITIES = [
    {"name": "New York", "country": "USA", "population": 8336817},
    {"name": "London", "country": "UK", "population": 8982000},
    {"name": "Tokyo", "country": "Japan", "population": 13929286},
    {"name": "Paris", "country": "France", "population": 2161000},
    {"name": "Sydney", "country": "Australia", "population": 5312163}
]

QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Life is what happens to you while you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It is during our darkest moments that we must focus to see the light. - Aristotle"
]


def generate_fake_weather(city_name: str) -> dict:
    """Generate fake weather data for demo purposes"""
    # Use city name to generate consistent "random" data
    seed = hash(city_name.lower()) % 1000
    random.seed(seed)
    
    temp = random.randint(-10, 35)
    humidity = random.randint(30, 90)
    pressure = random.randint(980, 1030)
    
    conditions = ["sunny", "cloudy", "rainy", "snowy", "foggy", "windy"]
    condition = random.choice(conditions)
    
    return {
        "city": city_name,
        "temperature": temp,
        "humidity": humidity,
        "pressure": pressure,
        "condition": condition,
        "note": "This is demo data - not real weather!"
    }


@app.route('/')
def home():
    """Home endpoint with API information"""
    return jsonify({
        'message': 'Simple Demo API',
        'version': '1.0.0',
        'description': 'A simple Cloud Run demo without external dependencies',
        'endpoints': {
            '/health': 'Health check',
            '/time': 'Current server time',
            '/random': 'Random number generator',
            '/quote': 'Random inspirational quote',
            '/weather/<city>': 'Fake weather for a city',
            '/cities': 'List of demo cities',
            '/math/<operation>/<a>/<b>': 'Basic math operations'
        },
        'examples': [
            '/time',
            '/random',
            '/quote',
            '/weather/London',
            '/cities',
            '/math/add/5/3'
        ]
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'simple-demo-api',
        'uptime': 'running'
    })


@app.route('/time')
def get_time():
    """Get current server time"""
    now = datetime.now()
    return jsonify({
        'current_time': now.isoformat(),
        'timestamp': now.timestamp(),
        'timezone': 'UTC',
        'formatted': now.strftime('%Y-%m-%d %H:%M:%S')
    })


@app.route('/random')
def get_random():
    """Generate random numbers"""
    min_val = int(request.args.get('min', 1))
    max_val = int(request.args.get('max', 100))
    count = int(request.args.get('count', 1))
    
    if min_val >= max_val:
        return jsonify({'error': 'min must be less than max'}), 400
    
    if count > 100:
        return jsonify({'error': 'count cannot exceed 100'}), 400
    
    numbers = [random.randint(min_val, max_val) for _ in range(count)]
    
    return jsonify({
        'numbers': numbers,
        'count': len(numbers),
        'min': min_val,
        'max': max_val,
        'sum': sum(numbers),
        'average': round(sum(numbers) / len(numbers), 2)
    })


@app.route('/quote')
def get_quote():
    """Get a random inspirational quote"""
    quote = random.choice(QUOTES)
    return jsonify({
        'quote': quote,
        'timestamp': datetime.now().isoformat()
    })


@app.route('/weather/<city>')
def get_weather(city):
    """Get fake weather for a city"""
    weather_data = generate_fake_weather(city)
    return jsonify(weather_data)


@app.route('/cities')
def get_cities():
    """Get list of demo cities"""
    return jsonify({
        'cities': CITIES,
        'total': len(CITIES),
        'note': 'This is demo data'
    })


@app.route('/math/<operation>/<float:a>/<float:b>')
def math_operation(operation, a, b):
    """Perform basic math operations"""
    try:
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return jsonify({'error': 'Division by zero'}), 400
            result = a / b
        elif operation == 'power':
            result = a ** b
        elif operation == 'sqrt':
            if a < 0:
                return jsonify({'error': 'Cannot calculate square root of negative number'}), 400
            result = math.sqrt(a)
        else:
            return jsonify({'error': 'Invalid operation. Use: add, subtract, multiply, divide, power, sqrt'}), 400
        
        return jsonify({
            'operation': operation,
            'a': a,
            'b': b,
            'result': result,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/stats')
def get_stats():
    """Get some basic statistics"""
    return jsonify({
        'total_cities': len(CITIES),
        'total_quotes': len(QUOTES),
        'random_number': random.randint(1, 1000),
        'pi': math.pi,
        'e': math.e,
        'timestamp': datetime.now().isoformat()
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found',
        'available_endpoints': [
            '/', '/health', '/time', '/random', '/quote', 
            '/weather/<city>', '/cities', '/math/<operation>/<a>/<b>', '/stats'
        ]
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
