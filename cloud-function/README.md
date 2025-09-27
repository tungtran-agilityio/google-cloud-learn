# 🚀 Simple Cloud Function

A simple Google Cloud Function that demonstrates basic text processing capabilities.

## ✨ Features

- **Character Count**: Count characters in text
- **Word Count**: Count words in text  
- **Text Transformation**: Convert to uppercase, lowercase, and reverse
- **Simple & Fast**: Minimal dependencies, quick response

## 🚀 Quick Start

### Prerequisites
- Google Cloud Project with billing enabled
- `gcloud` CLI installed and authenticated

### 1. Deploy to Cloud Functions
```bash
# Set your project ID
export PROJECT_ID="your-project-id"

# Deploy the function
./deploy.sh
```

### 2. Test the Function
```bash
# Set the function URL (from deployment output)
export FUNCTION_URL="https://your-function-url.run.app"

# Run the example
python example.py
```

## 📚 API Usage

### GET Request
```bash
curl "https://your-function-url.run.app?text=Hello World"
```

### POST Request
```bash
curl -X POST "https://your-function-url.run.app" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello World"}'
```

### Response Format
```json
{
  "original_text": "Hello World",
  "character_count": 11,
  "word_count": 2,
  "uppercase": "HELLO WORLD",
  "lowercase": "hello world",
  "reversed": "dlroW olleH",
  "message": "Text processed successfully!"
}
```

## 🛠️ Local Development

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Locally
```bash
functions-framework --target=simple_text_processor --source=main.py --port=8080
```

### 3. Test Locally
```bash
# Set local URL
export FUNCTION_URL="http://localhost:8080"

# Run tests
python example.py
```

## 🧪 Testing

### Manual Testing
```bash
# Basic test
curl "https://your-function-url.run.app?text=Hello World"

# Different text
curl "https://your-function-url.run.app?text=Cloud Function Test"

# POST request
curl -X POST "https://your-function-url.run.app" \
  -H "Content-Type: application/json" \
  -d '{"text": "Simple Test"}'
```

### Run Example Script
```bash
python example.py
```

## 📊 Example Use Cases

### 1. Text Statistics
```python
import requests
response = requests.get("https://your-function-url.run.app?text=Hello World")
data = response.json()
print(f"Words: {data['word_count']}, Characters: {data['character_count']}")
```

### 2. Text Transformation
```python
import requests
response = requests.get("https://your-function-url.run.app?text=hello world")
data = response.json()
print(f"Uppercase: {data['uppercase']}")
print(f"Reversed: {data['reversed']}")
```

## 🔧 Configuration

### Cloud Function Settings
- **Runtime**: Python 3.11
- **Memory**: 256MB (default)
- **Timeout**: 60 seconds (default)
- **Trigger**: HTTP

## 📈 Monitoring

### View Function Logs
```bash
gcloud functions logs read simple-text-function --region=us-central1 --limit=50
```

## 🎓 Learning Points

This simple Cloud Function demonstrates:
- **Basic Cloud Function Structure**: Single function with HTTP trigger
- **Request Handling**: GET and POST request processing
- **Response Formatting**: JSON responses with proper headers
- **Error Handling**: Basic error responses
- **CORS Support**: Cross-origin request handling

## 📄 License

This project is licensed under the MIT License.

## 🙏 Perfect For

- Learning Google Cloud Functions basics
- Understanding serverless function structure
- Simple text processing needs
- Quick API prototyping