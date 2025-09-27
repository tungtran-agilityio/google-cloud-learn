#!/bin/bash

# Text Processing Cloud Function Deployment Script

set -e

# Configuration
PROJECT_ID=${PROJECT_ID:-"learn-cloud-473302"}
FUNCTION_NAME="simple-text-function"
REGION=${REGION:-"us-central1"}
RUNTIME="python311"
ENTRY_POINT="simple_text_processor"

echo "🚀 Deploying Simple Cloud Function"
echo "Project ID: $PROJECT_ID"
echo "Function Name: $FUNCTION_NAME"
echo "Region: $REGION"
echo "Runtime: $RUNTIME"
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

# Enable required APIs
echo "🔧 Enabling required APIs..."
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable cloudbuild.googleapis.com

# Deploy the Cloud Function
echo "🚀 Deploying Cloud Function..."
gcloud functions deploy $FUNCTION_NAME \
    --gen2 \
    --runtime=$RUNTIME \
    --region=$REGION \
    --source=. \
    --entry-point=$ENTRY_POINT \
    --trigger-http \
    --allow-unauthenticated \
    --memory=256MB \
    --timeout=60s \
    --max-instances=10

# Get function URL
FUNCTION_URL=$(gcloud functions describe $FUNCTION_NAME --region=$REGION --format='value(serviceConfig.uri)')

echo ""
echo "✅ Deployment completed successfully!"
echo "Function URL: $FUNCTION_URL"
echo ""
echo "🧪 Test the function:"
echo "curl \"$FUNCTION_URL?text=Hello World\""
echo ""
echo "📝 Try different texts:"
echo "curl \"$FUNCTION_URL?text=Simple Test\""
echo "curl \"$FUNCTION_URL?text=Cloud Function Demo\""
echo ""
echo "📖 Run the example script:"
echo "export FUNCTION_URL=$FUNCTION_URL"
echo "python example.py"
echo ""
echo "🔧 View function logs:"
echo "gcloud functions logs read $FUNCTION_NAME --region=$REGION --limit=50"
