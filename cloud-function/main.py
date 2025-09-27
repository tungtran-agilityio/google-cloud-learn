"""
Simple Cloud Function - Basic Text Processing
This is a simple Cloud Function that demonstrates basic functionality
"""

import json
import functions_framework


@functions_framework.http
def simple_text_processor(request):
    """
    Simple Cloud Function that processes text
    """
    # Set CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    # Handle preflight requests
    if request.method == 'OPTIONS':
        return ('', 204, headers)
    
    try:
        # Get text from request
        if request.method == 'GET':
            text = request.args.get('text', '')
        else:
            request_json = request.get_json(silent=True)
            text = request_json.get('text', '') if request_json else ''
        
        if not text:
            return (json.dumps({"error": "No text provided"}), 400, headers)
        
        # Simple text processing
        result = {
            "original_text": text,
            "character_count": len(text),
            "word_count": len(text.split()),
            "uppercase": text.upper(),
            "lowercase": text.lower(),
            "reversed": text[::-1],
            "message": "Text processed successfully!"
        }
        
        return (json.dumps(result), 200, headers)
        
    except Exception as e:
        return (json.dumps({"error": f"Error: {str(e)}"}), 500, headers)