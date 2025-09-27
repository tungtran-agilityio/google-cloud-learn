# 🚀 Simple Demo API - Google Cloud Run

A super simple Python web service deployed on Google Cloud Run that demonstrates basic functionality without any external dependencies or API keys required.

## ✨ Features

- **No External Dependencies**: Works completely offline, no API keys needed
- **Multiple Endpoints**: Various demo functions to showcase Cloud Run capabilities
- **Self-Contained**: All data is generated locally
- **Easy to Deploy**: One-command deployment to Google Cloud Run
- **Perfect for Learning**: Great for understanding Cloud Run basics

## 🎯 Available Endpoints

| Endpoint                 | Description                             | Example                         |
| ------------------------ | --------------------------------------- | ------------------------------- |
| `GET /`                  | API information and available endpoints | `/`                             |
| `GET /health`            | Health check                            | `/health`                       |
| `GET /time`              | Current server time                     | `/time`                         |
| `GET /random`            | Random number generator                 | `/random?min=1&max=100&count=5` |
| `GET /quote`             | Random inspirational quote              | `/quote`                        |
| `GET /weather/<city>`    | Fake weather for any city               | `/weather/London`               |
| `GET /cities`            | List of demo cities                     | `/cities`                       |
| `GET /math/<op>/<a>/<b>` | Math operations                         | `/math/add/5.0/3.0`             |
| `GET /stats`             | Basic statistics                        | `/stats`                        |

## 🚀 Quick Start

### Prerequisites
- Google Cloud Project with billing enabled
- `gcloud` CLI installed and authenticated
- Docker installed

### 1. Deploy to Cloud Run
```bash
# Set your project ID
export PROJECT_ID="your-project-id"

# Deploy the service
./deploy.sh
```

### 2. Test the Service
```bash
# Set the service URL (from deployment output)
export API_URL="https://your-service-url.run.app"

# Run the example
python example.py
```

## 🛠️ Local Development

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Locally
```bash
python main.py
```

The service will be available at `http://localhost:8080`

## 🐳 Docker

### Build and Run
```bash
# Build image
docker build -t simple-demo-api .

# Run container
docker run -p 8080:8080 simple-demo-api
```

## 📊 Example Responses

### Health Check
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00",
  "service": "simple-demo-api",
  "uptime": "running"
}
```

### Random Numbers
```json
{
  "numbers": [23, 67, 12, 89, 45],
  "count": 5,
  "min": 1,
  "max": 100,
  "sum": 236,
  "average": 47.2
}
```

### Fake Weather
```json
{
  "city": "London",
  "temperature": 15,
  "humidity": 78,
  "pressure": 1013,
  "condition": "cloudy",
  "note": "This is demo data - not real weather!"
}
```

### Math Operations
```json
{
  "operation": "add",
  "a": 5.0,
  "b": 3.0,
  "result": 8.0,
  "timestamp": "2024-01-15T10:30:00"
}
```

## 🧪 Testing

### Manual Testing
```bash
# Health check
curl https://your-service-url.run.app/health

# Get current time
curl https://your-service-url.run.app/time

# Generate random numbers
curl "https://your-service-url.run.app/random?min=1&max=50&count=3"

# Get a quote
curl https://your-service-url.run.app/quote

# Fake weather
curl https://your-service-url.run.app/weather/Paris

# Math operations
curl https://your-service-url.run.app/math/multiply/7.0/6.0
```

### Run Example Script
```bash
python example.py
```

## 🔧 Configuration

### Cloud Run Settings
- **Memory**: 256MB (minimal for demo)
- **CPU**: 1 vCPU
- **Timeout**: 60 seconds
- **Concurrency**: 80 requests per instance
- **Max Instances**: 5

### Environment Variables
- `PORT`: Service port (default: 8080)

## 📈 Monitoring

### View Logs
```bash
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=simple-demo-api" --limit 50
```

### Cloud Run Metrics
- Request count and latency
- Error rates
- Memory and CPU utilization

## 🎓 Learning Points

This demo showcases:
- **Basic Flask Application**: Simple web service structure
- **Cloud Run Deployment**: Serverless container deployment
- **Docker Containerization**: Multi-stage build optimization
- **Error Handling**: Proper HTTP status codes and error responses
- **API Design**: RESTful endpoints with clear responses
- **No External Dependencies**: Self-contained service

## 🔒 Security

- Non-root user in container
- Input validation
- Error handling
- No sensitive data

## 📄 License

This project is licensed under the MIT License.

## 🙏 Perfect For

- Learning Google Cloud Run basics
- Understanding serverless deployment
- Testing Cloud Run concepts
- Demonstrating simple API design
- No external API key requirements
