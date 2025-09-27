#!/bin/bash

# Simple Demo API Cloud Run Deployment Script

set -e

# Configuration
PROJECT_ID=${PROJECT_ID:-"learn-cloud-473302"}
SERVICE_NAME="simple-demo-api"
REGION=${REGION:-"us-central1"}

echo "🚀 Deploying Simple Demo API to Google Cloud Run"
echo "Project ID: $PROJECT_ID"
echo "Service Name: $SERVICE_NAME"
echo "Region: $REGION"
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ gcloud CLI is not installed. Please install it first."
    exit 1
fi

# Check if user is authenticated
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | grep -q .; then
    echo "❌ No active gcloud authentication found. Please run 'gcloud auth login'"
    exit 1
fi

# Set project
echo "📋 Setting project..."
gcloud config set project $PROJECT_ID

# Enable Cloud Run API
echo "🔧 Enabling Cloud Run API..."
gcloud services enable run.googleapis.com

# Build and push Docker image
echo "🐳 Building Docker image..."
IMAGE_NAME="gcr.io/$PROJECT_ID/$SERVICE_NAME"
docker build -t $IMAGE_NAME .

echo "📤 Pushing image to Google Container Registry..."
docker push $IMAGE_NAME

# Deploy to Cloud Run
echo "🚀 Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
    --image $IMAGE_NAME \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --memory 256Mi \
    --cpu 1 \
    --timeout 60 \
    --concurrency 80 \
    --max-instances 5 \
    --port 8080

# Get service URL
SERVICE_URL=$(gcloud run services describe $SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)')

echo ""
echo "✅ Deployment completed successfully!"
echo "Service URL: $SERVICE_URL"
echo ""
echo "🧪 Test the service:"
echo "curl $SERVICE_URL/health"
echo ""
echo "🎲 Try some endpoints:"
echo "curl $SERVICE_URL/time"
echo "curl $SERVICE_URL/random"
echo "curl $SERVICE_URL/quote"
echo "curl $SERVICE_URL/weather/London"
echo "curl $SERVICE_URL/math/add/5/3"
echo ""
echo "📖 Run the example script:"
echo "export API_URL=$SERVICE_URL"
echo "python example.py"
