# Azure AI 102 Certification Study Guide

## Table of Contents
1. [Python Libraries](#python-libraries)
2. [Computer Vision Services](#computer-vision-services)
3. [Azure Face API](#azure-face-api)
4. [Natural Language Processing](#natural-language-processing)
5. [Speech Services](#speech-services)
6. [Document Intelligence](#document-intelligence)
7. [Video Indexer](#video-indexer)
8. [Azure AI Search](#azure-ai-search)
9. [Azure AI Foundry](#azure-ai-foundry)
10. [Model Context Protocol (MCP)](#model-context-protocol-mcp)
11. [Code Interceptor](#code-interceptor)
12. [Infrastructure as Code](#infrastructure-as-code)

---

## Python Libraries

### Essential Azure AI Libraries

#### 1. azure-cognitiveservices-vision-computervision

**Purpose:** Computer Vision image analysis, OCR, object detection

**Installation:**
```bash
pip install azure-cognitiveservices-vision-computervision==0.9.0
```

**Key Imports:**
```python
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
```

**Common Usage:**
```python
# Initialize client
credentials = CognitiveServicesCredentials(api_key)
client = ComputerVisionClient(endpoint, credentials)

# Analyze image
results = client.analyze_image_in_stream(image_data, visual_features=[VisualFeatureTypes.objects])
```

---

#### 2. azure-ai-vision-face

**Purpose:** Face detection, verification, identification, and liveness detection

**Installation:**
```bash
pip install azure-ai-vision-face==0.16.0
```

**Key Imports:**
```python
from azure.ai.vision.face import FaceClient
from azure.ai.vision.face.models import FaceDetectionModel, FaceRecognitionModel
from azure.core.credentials import AzureKeyCredential
```

**Common Usage:**
```python
# Initialize client
face_client = FaceClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

# Detect faces
detected_faces = face_client.detect(image_content=image_data.read())
```

---

#### 3. azure-cognitiveservices-speech

**Purpose:** Speech-to-text, text-to-speech, speaker recognition

**Installation:**
```bash
pip install azure-cognitiveservices-speech==1.35.0
```

**Key Imports:**
```python
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, SpeechSynthesizer
```

**Common Usage:**
```python
# Initialize speech config
speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)

# Create recognizer for speech-to-text
recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
```

---

#### 4. azure-cognitiveservices-language-textanalytics

**Purpose:** Text analysis, sentiment analysis, entity recognition

**Installation:**
```bash
pip install azure-cognitiveservices-language-textanalytics==5.3.0
```

**Key Imports:**
```python
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from azure.cognitiveservices.language.textanalytics.models import TextDocumentInput
from msrest.authentication import CognitiveServicesCredentials
```

**Common Usage:**
```python
# Initialize client
credentials = CognitiveServicesCredentials(api_key)
client = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)

# Analyze sentiment
results = client.sentiment(documents=[{"id": "1", "language": "en", "text": "I love this!"}])
```

---

#### 5. azure-cognitiveservices-language-luis

**Purpose:** Language Understanding (LUIS) for intent and entity extraction

**Installation:**
```bash
pip install azure-cognitiveservices-language-luis==3.3.0
```

**Key Imports:**
```python
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
```

**Common Usage:**
```python
# Initialize client
credentials = CognitiveServicesCredentials(api_key)
client = LUISRuntimeClient(endpoint, credentials)

# Predict intent
results = client.prediction.resolve(app_id, query)
```

---

#### 6. azure-ai-formrecognizer

**Purpose:** Document Intelligence (formerly Form Recognizer) for document processing

**Installation:**
```bash
pip install azure-ai-formrecognizer==3.3.3
```

**Key Imports:**
```python
from azure.ai.formrecognizer import DocumentAnalysisClient, AnalyzeDocumentType
from azure.core.credentials import AzureKeyCredential
```

**Common Usage:**
```python
# Initialize client
client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

# Analyze document
with open(document_path, "rb") as document:
    poller = client.begin_analyze_document("prebuilt-invoice", document)
    result = poller.result()
```

---

#### 7. azure-search-documents

**Purpose:** Azure AI Search for indexing and querying documents

**Installation:**
```bash
pip install azure-search-documents==11.4.0
```

**Key Imports:**
```python
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient, SearchIndexerClient
from azure.core.credentials import AzureKeyCredential
```

**Common Usage:**
```python
# Initialize client
search_client = SearchClient(endpoint, index_name, AzureKeyCredential(api_key))

# Search documents
results = search_client.search(search_text="Azure AI")
```

---

#### 8. openai

**Purpose:** OpenAI API access for GPT models (including Azure OpenAI)

**Installation:**
```bash
pip install openai==1.3.0
```

**Key Imports:**
```python
from openai import AzureOpenAI
import openai
```

**Common Usage:**
```python
# Initialize client
client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-05-01-preview",
    azure_endpoint=endpoint
)

# Create chat completion
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}]
)
```

---

### Supporting Libraries

#### 9. Pillow (PIL)

**Purpose:** Image processing and manipulation

**Installation:**
```bash
pip install Pillow==10.0.0
```

**Key Imports:**
```python
from PIL import Image, ImageDraw, ImageFont
```

**Common Usage:**
```python
# Open and manipulate images
image = Image.open("image.jpg")
draw = ImageDraw.Draw(image)
draw.rectangle([(x1, y1), (x2, y2)], outline="red", width=2)
image.save("output.jpg")
```

---

#### 10. matplotlib

**Purpose:** Data visualization and image display

**Installation:**
```bash
pip install matplotlib==3.8.0
```

**Key Imports:**
```python
from matplotlib import pyplot as plt
```

**Common Usage:**
```python
# Display image with annotations
plt.figure(figsize=(10, 8))
plt.imshow(image)
plt.axis('off')
plt.show()
```

---

#### 11. numpy

**Purpose:** Numerical computing and array manipulation

**Installation:**
```bash
pip install numpy==1.24.0
```

**Key Imports:**
```python
import numpy as np
```

**Common Usage:**
```python
# Convert image to array
image_array = np.array(image)
print(f"Image shape: {image_array.shape}")
```

---

#### 12. requests

**Purpose:** HTTP client for REST API calls

**Installation:**
```bash
pip install requests==2.31.0
```

**Key Imports:**
```python
import requests
from requests.auth import HTTPBasicAuth
```

**Common Usage:**
```python
# Make HTTP request
headers = {"api-key": api_key, "Content-Type": "application/json"}
response = requests.post(url, headers=headers, json=data)
result = response.json()
```

---

#### 13. python-dotenv

**Purpose:** Load environment variables from .env files

**Installation:**
```bash
pip install python-dotenv==1.0.0
```

**Key Imports:**
```python
from dotenv import load_dotenv
import os
```

**Common Usage:**
```python
# Load environment variables
load_dotenv()
api_key = os.getenv('API_KEY')
endpoint = os.getenv('ENDPOINT')
```

---

#### 14. azure-identity

**Purpose:** Azure authentication (DefaultAzureCredential, etc.)

**Installation:**
```bash
pip install azure-identity==1.14.0
```

**Key Imports:**
```python
from azure.identity import DefaultAzureCredential, ClientSecretCredential
```

**Common Usage:**
```python
# Use managed identity
credential = DefaultAzureCredential()

# Or use service principal
credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)
```

---

#### 15. semantic-kernel

**Purpose:** Semantic Kernel for AI agents and orchestration

**Installation:**
```bash
pip install semantic-kernel==0.8.0
```

**Key Imports:**
```python
from semantic_kernel import Kernel
from semantic_kernel.agents import AgentGroupChat, ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
```

**Common Usage:**
```python
# Create kernel
kernel = Kernel()

# Add service
service = AzureChatCompletion(deployment_name="gpt-4", endpoint=endpoint, api_key=api_key)
kernel.add_service(service)
```

---

### Setup Virtual Environment

**Create and activate Python virtual environment:**

```bash
# Create virtual environment
python -m venv labenv

# Activate (macOS/Linux)
source labenv/bin/activate

# Activate (Windows)
labenv\Scripts\activate
```

**Install all required libraries:**

```bash
# Create requirements.txt
cat > requirements.txt << EOF
azure-cognitiveservices-vision-computervision==0.9.0
azure-ai-vision-face==0.16.0
azure-cognitiveservices-speech==1.35.0
azure-cognitiveservices-language-textanalytics==5.3.0
azure-cognitiveservices-language-luis==3.3.0
azure-ai-formrecognizer==3.3.3
azure-search-documents==11.4.0
openai==1.3.0
Pillow==10.0.0
matplotlib==3.8.0
numpy==1.24.0
requests==2.31.0
python-dotenv==1.0.0
azure-identity==1.14.0
semantic-kernel==0.8.0
EOF

# Install all packages
pip install -r requirements.txt
```

**Verify installation:**

```bash
python -c "import azure; print(f'Azure SDK version: {azure.__version__}')"
pip list | grep azure
```

---

## Computer Vision Services

## Computer Vision Services

### 1. Computer Vision (Image Analysis)

**Service Description:**
Azure Computer Vision provides advanced image analysis capabilities including content tagging, object detection, face detection, OCR, and scene understanding.

**Key Features:**
- Image analysis (objects, tags, descriptions)
- Optical Character Recognition (OCR)
- Face detection and identification
- Celebrity and landmark recognition
- Brand detection
- Image moderation

**Available Models:**
- Vision 4.0 (latest)
- Vision 3.2 (legacy)

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Max Image Size** | 4 MB per image |
| **Supported Formats** | JPEG, PNG, GIF, BMP, WEBP, RAW, TIFF |
| **Min/Max Image Dimensions** | 50x50 to 10000x10000 pixels |
| **Rate Limits (Free Tier)** | 20 calls/min |
| **Rate Limits (S0/S1)** | 10 calls/sec |
| **OCR Supported Languages** | 70+ languages |
| **Text Recognition Accuracy** | Best with 40x40 pixel minimum per character |
| **Face Detection Limit** | Up to 64 faces per image |
| **Maximum Requests per Batch** | 64 images |
| **Timeout** | 30 seconds per request |
| **Quota (Free Tier)** | 20 calls/month per API |

#### Azure CLI Command

```bash
# Create Computer Vision service
az cognitiveservices account create \
  --name myComputerVision \
  --resource-group myResourceGroup \
  --kind ComputerVision \
  --sku S1 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myComputerVision \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myComputerVision \
  --resource-group myResourceGroup \
  --query properties.endpoint
```

#### Python Code Example

```python
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import requests

# Initialize client
subscription_key = "YOUR_SUBSCRIPTION_KEY"
endpoint = "YOUR_ENDPOINT"

client = ComputerVisionClient(
    endpoint=endpoint,
    credentials=CognitiveServicesCredentials(subscription_key)
)

# Analyze local image
image_path = "path/to/image.jpg"
with open(image_path, "rb") as image_file:
    results = client.analyze_image_in_stream(
        image=image_file,
        visual_features=[
            VisualFeatureTypes.objects,
            VisualFeatureTypes.tags,
            VisualFeatureTypes.faces,
            VisualFeatureTypes.adult,
            VisualFeatureTypes.brands
        ]
    )

# Process results
print("Objects detected:")
for obj in results.objects:
    print(f"  {obj.object_property}: {obj.confidence:.2f}")

print("\nTags:")
for tag in results.tags:
    print(f"  {tag.name}: {tag.confidence:.2f}")

if results.faces:
    print(f"\nFaces detected: {len(results.faces)}")
    for face in results.faces:
        print(f"  Position: {face.face_rectangle}")

print(f"\nAdult content: {results.adult.is_adult_content}")
```

#### REST API Example

```bash
curl -X POST \
  "YOUR_ENDPOINT/vision/v3.2/analyze?visualFeatures=Objects,Tags,Faces,Adult,Brands" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"https://example.com/image.jpg\"}"
```

**Request Fields:**
- `url`: URL of the image to analyze
- `visualFeatures`: Comma-separated list of visual features (Objects, Tags, Faces, Brands, Adult, etc.)
- `details`: Optional additional details (Celebrities, Landmarks)
- `language`: Language code for text results (default: en)

**Response Fields:**
```json
{
  "objects": [
    {
      "rectangle": {
        "x": 0,
        "y": 0,
        "w": 100,
        "h": 100
      },
      "object": "object_name",
      "confidence": 0.95
    }
  ],
  "tags": [
    {
      "name": "tag_name",
      "confidence": 0.98
    }
  ],
  "faces": [
    {
      "age": 25,
      "gender": "Female",
      "faceRectangle": {
        "left": 50,
        "top": 50,
        "width": 80,
        "height": 80
      },
      "faceAttributes": {
        "emotion": {
          "anger": 0,
          "contempt": 0,
          "disgust": 0,
          "fear": 0,
          "happiness": 1,
          "neutral": 0,
          "sadness": 0,
          "surprise": 0
        },
        "glasses": "NoGlasses"
      }
    }
  ],
  "adult": {
    "isAdultContent": false,
    "isRacyContent": false,
    "adultScore": 0.0,
    "racyScore": 0.0
  },
  "brands": [
    {
      "name": "brand_name",
      "confidence": 0.92,
      "rectangle": {
        "x": 10,
        "y": 10,
        "w": 50,
        "h": 50
      }
    }
  ]
}
```

---

### 2. Custom Vision

**Service Description:**
Azure Custom Vision allows you to build, deploy, and improve custom image classification and object detection models with minimal code.

**Key Features:**
- Image classification (single-label and multi-label)
- Object detection
- Model training and iteration
- Real-time predictions
- Export to multiple formats (CoreML, ONNX, TensorFlow, Docker)

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Max Images per Project** | Unlimited |
| **Max Tags per Project** | 500 tags |
| **Max Images per Tag** | Unlimited |
| **Training Images Minimum** | 15 images per tag (Classification), 15 per class (Detection) |
| **Training Time** | 1-60 minutes depending on data size |
| **Prediction Rate Limit** | 10 requests/sec (per seat) |
| **Max Concurrent Predictions** | Limited by subscription tier |
| **Model File Size** | Varies (typically 50-300 MB) |
| **Supported Image Formats** | JPEG, PNG, GIF, BMP |
| **Max Image Size** | 6 MB |
| **Min Image Dimension** | 256 pixels (for optimal training) |
| **Quota (Free Tier)** | 2 projects |
| **Quota (Standard)** | Unlimited projects |
| **Iterations per Project** | Unlimited |
| **Export Formats Limit** | 2 simultaneous exports |

#### Azure CLI Command

```bash
# Create Custom Vision Training account
az cognitiveservices account create \
  --name myCustomVisionTraining \
  --resource-group myResourceGroup \
  --kind CustomVision.Training \
  --sku F0 \
  --location eastus \
  --yes

# Create Custom Vision Prediction account
az cognitiveservices account create \
  --name myCustomVisionPrediction \
  --resource-group myResourceGroup \
  --kind CustomVision.Prediction \
  --sku F0 \
  --location eastus \
  --yes

# Get training key
az cognitiveservices account keys list \
  --name myCustomVisionTraining \
  --resource-group myResourceGroup

# Get prediction key
az cognitiveservices account keys list \
  --name myCustomVisionPrediction \
  --resource-group myResourceGroup
```

#### Python Code Example

```python
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from msrest.authentication import CognitiveServicesCredentials

# Training setup
training_key = "YOUR_TRAINING_KEY"
training_endpoint = "YOUR_TRAINING_ENDPOINT"
prediction_key = "YOUR_PREDICTION_KEY"
prediction_resource_id = "YOUR_PREDICTION_RESOURCE_ID"

trainer = CustomVisionTrainingClient(
    training_key, 
    endpoint=training_endpoint
)

# Create project
project = trainer.create_project(
    name="My Custom Vision Project",
    description="Project for detecting cats vs dogs"
)

# Create tags
cat_tag = trainer.create_tag(
    project_id=project.id,
    name="cat"
)

dog_tag = trainer.create_tag(
    project_id=project.id,
    name="dog"
)

# Upload and tag images
base_image_location = "path/to/images/"
image_list = []

for image_num in range(1, 11):
    file_path = f"{base_image_location}cat_{image_num}.jpg"
    with open(file_path, "rb") as image_data:
        image_list.append(
            ImageFileCreateEntry(
                name=f"cat_{image_num}",
                image_data=image_data,
                tag_ids=[cat_tag.id]
            )
        )

trainer.create_images_from_files(
    project_id=project.id,
    images=image_list
)

# Train the model
iteration = trainer.train_project(project_id=project.id)
while iteration.status == "Training":
    import time
    time.sleep(1)
    iteration = trainer.get_iteration(project_id=project.id, iteration_id=iteration.id)

print(f"Training completed. Precision: {iteration.precision}")

# Publish the iteration
trainer.publish_iteration(
    project_id=project.id,
    iteration_id=iteration.id,
    publish_iteration_name="Production",
    prediction_id=prediction_resource_id
)

# Make predictions
predictor = CustomVisionPredictionClient(
    prediction_key,
    endpoint=prediction_endpoint
)

with open("test_image.jpg", "rb") as image_data:
    results = predictor.classify_image(
        project_id=project.id,
        published_name="Production",
        image_data=image_data
    )

for prediction in results.predictions:
    print(f"{prediction.tag_name}: {prediction.probability:.2%}")
```

#### REST API Example

```bash
# Make prediction
curl -X POST \
  "YOUR_PREDICTION_ENDPOINT/customvision/v3.0/Prediction/YOUR_PROJECT_ID/classify/iterations/Production/image" \
  -H "Prediction-Key: YOUR_PREDICTION_KEY" \
  -H "Content-Type: application/octet-stream" \
  --data-binary "@image.jpg"
```

**Request Fields:**
- `image`: Binary image data or URL
- `iteration`: Published iteration name
- `application`: Optional application/model identifier

**Response Fields:**
```json
{
  "id": "guid",
  "project": "project_id",
  "iteration": "iteration_id",
  "predictions": [
    {
      "tagId": "tag_id",
      "tagName": "cat",
      "probability": 0.95
    },
    {
      "tagId": "tag_id",
      "tagName": "dog",
      "probability": 0.05
    }
  ]
}
```

---

### 3. Content Moderator

**Service Description:**
Azure Content Moderator analyzes text, images, and videos to identify potentially offensive, unwanted, or risky content.

**Key Features:**
- Text moderation (profanity, PII detection)
- Image moderation (adult/racy content, gore, violence)
- Video moderation with frame analysis
- Review tool for human review workflows

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Max Text Size** | 1,024 characters per request |
| **Max Image Size** | 4 MB |
| **Supported Image Formats** | JPEG, PNG, GIF, BMP |
| **Rate Limits (Free Tier)** | 1 call/sec |
| **Rate Limits (S1)** | 10 calls/sec |
| **Text Moderation Languages** | English, Spanish, German, French, Italian, Portuguese |
| **Profanity Dictionary Size** | 100,000+ terms |
| **PII Detection Limit** | Email, Phone, SSN, Address, IPA |
| **Image Moderation Score Range** | 0.0 - 1.0 |
| **Video Frame Sampling** | 1 frame per second (minimum) |
| **Max Video Duration** | 10 minutes |
| **Timeout** | 30 seconds per request |
| **Concurrent Requests (Free)** | 1 |
| **Concurrent Requests (S1)** | 10 |

#### Azure CLI Command

```bash
# Create Content Moderator account
az cognitiveservices account create \
  --name myContentModerator \
  --resource-group myResourceGroup \
  --kind ContentModerator \
  --sku S0 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myContentModerator \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myContentModerator \
  --resource-group myResourceGroup \
  --query properties.endpoint

# Update to higher tier
az cognitiveservices account update \
  --name myContentModerator \
  --resource-group myResourceGroup \
  --sku S1
```

#### Python Code Example

```python
from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
from msrest.authentication import CognitiveServicesCredentials

subscription_key = "YOUR_SUBSCRIPTION_KEY"
endpoint = "YOUR_ENDPOINT"

client = ContentModeratorClient(
    endpoint=endpoint,
    credentials=CognitiveServicesCredentials(subscription_key)
)

# Text moderation
text_to_moderate = "This is a test message with [bad word]"

response = client.text_moderation.screen_text(
    language="eng",
    text=text_to_moderate,
    autocorrect=True,
    pii=True,
    classify=True
)

print(f"Is appropriate: {response.is_likely_junk}")
print(f"Profanity score: {response.score}")
if response.pii_data:
    print(f"PII detected: {response.pii_data}")

# Image moderation
image_url = "https://example.com/image.jpg"

response = client.image_moderation.evaluate_url(
    url=image_url,
    cache_image=True
)

print(f"Adult score: {response.adult_classification_score}")
print(f"Racy score: {response.racy_classification_score}")
print(f"Is adult content: {response.is_image_adult_classified}")
```

#### REST API Example

```bash
# Text moderation
curl -X POST \
  "YOUR_ENDPOINT/contentmoderator/moderate/v1.0/ProcessText/Screen" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: text/plain" \
  -d "Sample text for moderation"

# Image moderation
curl -X POST \
  "YOUR_ENDPOINT/contentmoderator/moderate/v1.0/ProcessImage/Evaluate" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"DataRepresentation\": \"URL\", \"Value\": \"https://example.com/image.jpg\"}"
```

**Response Fields for Text Moderation:**
```json
{
  "OriginalText": "original text",
  "NormalizedText": "normalized text",
  "MisSpelledTerms": [],
  "Terms": [
    {
      "Index": 0,
      "OriginalIndex": 0,
      "ListId": 0,
      "Term": "flagged_term"
    }
  ],
  "Language": "eng",
  "Terms": [],
  "Status": 200,
  "TrackingId": "tracking_id",
  "PII": {
    "Email": [],
    "SocialSecurityNumber": [],
    "Phone": [],
    "Address": [],
    "IPA": []
  },
  "Classification": {
    "Category1": {
      "Score": 0.0
    },
    "Category2": {
      "Score": 0.0
    },
    "Category3": {
      "Score": 0.0
    },
    "ReviewRecommended": false
  }
}
```

---

## Azure Face API

### 1. Azure Face API Service

**Service Description:**
Azure Face API provides advanced facial recognition and analysis capabilities including face detection, verification, identification, liveness detection, and demographic analysis.

**Key Features:**
- Face detection with landmarks and attributes
- Face verification (1:1 comparison)
- Face identification (1:many matching)
- Face grouping and similarity
- Large person groups and face lists
- Liveness detection for anti-spoofing
- Demographic attributes (age, gender, smile, emotion)
- Face redaction for privacy

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Max File Size** | 6 MB per image |
| **Supported Formats** | JPEG, PNG, GIF, BMP, WEBP |
| **Image Resolution** | 36x36 to 4096x4096 pixels |
| **Face Size Range** | 36x36 to 4096x4096 pixels |
| **Detection Accuracy** | 95%+ for frontal faces, 85%+ for profile |
| **Faces per Image** | Up to 64 faces detectable |
| **Rate Limits (Free)** | 20 calls/min |
| **Rate Limits (Standard)** | 10 calls/sec |
| **Identification Model Accuracy** | 95%+ with quality training data |
| **Verification Accuracy** | 99%+ for 1:1 matching |
| **Max Person Group Size** | 10,000 people |
| **Max Faces per Person** | 248 faces |
| **Training Time** | < 1 minute for 1000 people |
| **Liveness Detection Accuracy** | 98%+ |
| **Supported Emotions** | anger, contempt, disgust, fear, happiness, neutral, sadness, surprise |
| **Supported Languages** | 45+ languages for metadata |
| **API Version** | 1.0 (latest: v1.1-preview.1) |
| **Free Tier Quota** | 30,000 requests/month |

#### Azure CLI Command

```bash
# Create Face API account
az cognitiveservices account create \
  --name myFaceAPI \
  --resource-group myResourceGroup \
  --kind Face \
  --sku S0 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myFaceAPI \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myFaceAPI \
  --resource-group myResourceGroup \
  --query properties.endpoint

# Create face list for grouping
az cognitiveservices account face-list create \
  --name myFaceList \
  --resource-group myResourceGroup \
  --face-api-account myFaceAPI
```

#### Python Code Example

```python
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import TrainingStatusType
from msrest.authentication import CognitiveServicesCredentials
import os
from PIL import Image
import matplotlib.pyplot as plt

subscription_key = "YOUR_SUBSCRIPTION_KEY"
endpoint = "YOUR_ENDPOINT"

face_client = FaceClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Detect faces
image_path = "person.jpg"
detected_faces = face_client.face.detect_with_url(
    url="https://example.com/person.jpg",
    detection_model="detection_03",
    return_face_attributes=["age", "gender", "headPose", "smile", "emotion", "facialHair"]
)

print("=== Face Detection Results ===")
for face in detected_faces:
    print(f"Face ID: {face.face_id}")
    print(f"Face Rectangle: {face.face_rectangle}")
    print(f"Age: {face.face_attributes.age}")
    print(f"Gender: {face.face_attributes.gender}")
    print(f"Smile: {face.face_attributes.smile}")
    print(f"Emotion: {face.face_attributes.emotion}")
    print()

# Face verification (1:1 comparison)
face1_id = detected_faces[0].face_id
face2_id = detected_faces[1].face_id if len(detected_faces) > 1 else None

if face2_id:
    verify_result = face_client.face.verify_face_to_face(face1_id, face2_id)
    print(f"=== Verification Result ===")
    print(f"Is Same Person: {verify_result.is_identical}")
    print(f"Confidence: {verify_result.confidence}")

# Create person group for identification
person_group_id = "my-person-group"
face_client.person_group.create(person_group_id, "My Person Group")

# Add person to group
person1 = face_client.person_group_person.create(
    person_group_id,
    "John Doe"
)

# Add face to person
with open("john_doe_photo.jpg", "rb") as f:
    face_client.person_group_person.add_face_from_stream(
        person_group_id,
        person1.person_id,
        f,
        detection_model="detection_03"
    )

# Train the model
face_client.person_group.train(person_group_id)

# Wait for training to complete
while True:
    training_status = face_client.person_group.get_training_status(person_group_id)
    if training_status.status == TrainingStatusType.succeeded:
        break

# Face identification (1:many matching)
test_image_faces = face_client.face.detect_with_url(
    url="https://example.com/test_person.jpg",
    detection_model="detection_03"
)

for face in test_image_faces:
    identify_results = face_client.face.identify(
        [face.face_id],
        person_group_id
    )
    
    for result in identify_results:
        print(f"Face {result.face_id} identified as:")
        for candidate in result.candidates:
            person = face_client.person_group_person.get(
                person_group_id,
                candidate.person_id
            )
            print(f"  {person.name} (Confidence: {candidate.confidence:.2%})")

# Face liveness detection
from azure.ai.vision.face import FaceClient as LivenessClient
from azure.ai.vision.face.models import LivenessSessionRequest

liveness_client = LivenessClient(endpoint, CognitiveServicesCredentials(subscription_key))

liveness_request = LivenessSessionRequest(
    detect_liveness_with_verify_image=True,
    liveness_operation_mode="Passive"
)

liveness_session = liveness_client.create_liveness_session(liveness_request)
print(f"Liveness Session ID: {liveness_session.session_id}")
```

#### REST API Example

```bash
# Detect faces
curl -X POST \
  "YOUR_ENDPOINT/face/v1.0/detect?detectionModel=detection_03&returnFaceAttributes=age,gender,smile,emotion" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/person.jpg"
  }'

# Response
{
  "faceId": "face-id-1",
  "faceRectangle": {
    "top": 131,
    "left": 177,
    "width": 100,
    "height": 100
  },
  "faceAttributes": {
    "age": 30,
    "gender": "male",
    "smile": 0.87,
    "emotion": {
      "anger": 0.0,
      "contempt": 0.0,
      "disgust": 0.0,
      "fear": 0.0,
      "happiness": 0.87,
      "neutral": 0.13,
      "sadness": 0.0,
      "surprise": 0.0
    }
  }
}

# Verify faces (1:1 comparison)
curl -X POST \
  "YOUR_ENDPOINT/face/v1.0/verify" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "faceId1": "face-id-1",
    "faceId2": "face-id-2"
  }'

# Response
{
  "isIdentical": true,
  "confidence": 0.98
}

# Create person group
curl -X PUT \
  "YOUR_ENDPOINT/face/v1.0/persongroups/my-group" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My Person Group",
    "userData": "Group for identification"
  }'

# Identify faces (1:many)
curl -X POST \
  "YOUR_ENDPOINT/face/v1.0/identify" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "personGroupId": "my-group",
    "faceIds": ["face-id-1"],
    "maxNumOfCandidatesReturned": 1,
    "confidenceThreshold": 0.5
  }'
```

---

## Natural Language Processing

### 1. Text Analytics

**Service Description:**
Azure Text Analytics provides NLP services for sentiment analysis, key phrase extraction, entity recognition, and language detection.

**Key Features:**
- Sentiment analysis
- Key phrase extraction
- Named entity recognition (NER)
- PII detection
- Language detection
- Entity linking

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Max Text Size** | 5,120 characters per document |
| **Max Documents per Request** | 10 documents (batch) |
| **Supported Languages** | 120+ languages |
| **Sentiment Analysis Accuracy** | ~90% |
| **Rate Limits (Free Tier)** | 100 calls/min |
| **Rate Limits (S/1/2/3/4)** | 1,000 calls/min |
| **Entities Supported** | 10+ types (Person, Location, Organization, etc.) |
| **Key Phrase Extraction** | Up to 120 key phrases per document |
| **PII Detection Entity Types** | 15+ types including Email, Phone, SSN |
| **Entity Linking Precision** | 70-85% accuracy |
| **Batch Processing Timeout** | 90 seconds |
| **Response Time** | <500 ms per document |
| **Concurrent Connections** | Based on subscription tier |
| **Free Tier Quota** | 5,000 records/month |
| **Data Retention** | 30 days (default) |

#### Azure CLI Command

```bash
# Create Text Analytics account
az cognitiveservices account create \
  --name myTextAnalytics \
  --resource-group myResourceGroup \
  --kind TextAnalytics \
  --sku S \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myTextAnalytics \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myTextAnalytics \
  --resource-group myResourceGroup \
  --query properties.endpoint

# Regenerate keys
az cognitiveservices account keys regenerate \
  --name myTextAnalytics \
  --resource-group myResourceGroup \
  --key-name key1
```

#### Python Code Example

```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

subscription_key = "YOUR_SUBSCRIPTION_KEY"
endpoint = "YOUR_ENDPOINT"

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(subscription_key)
)

# Sentiment analysis
documents = [
    "I had a wonderful experience at this hotel.",
    "The service was terrible and food was cold."
]

response = client.analyze_sentiment(
    documents=documents,
    language="en"
)

for doc in response:
    print(f"Sentiment: {doc.sentiment}")
    print(f"Positive: {doc.confidence_scores.positive}")
    print(f"Neutral: {doc.confidence_scores.neutral}")
    print(f"Negative: {doc.confidence_scores.negative}")

# Named Entity Recognition
response = client.recognize_entities(
    documents=documents,
    language="en"
)

for doc in response:
    print("Entities:")
    for entity in doc.entities:
        print(f"  {entity.text} ({entity.category}): {entity.confidence_score}")

# Key phrase extraction
response = client.extract_key_phrases(
    documents=documents,
    language="en"
)

for doc in response:
    print("Key phrases:")
    for phrase in doc.key_phrases:
        print(f"  {phrase}")

# Language detection
response = client.detect_language(documents=documents)

for doc in response:
    print(f"Language: {doc.primary_language.name} ({doc.primary_language.iso6391_name})")
```

#### REST API Example

```bash
# Sentiment analysis
curl -X POST \
  "YOUR_ENDPOINT/text/analytics/v3.1/sentiment" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"documents\": [
      {
        \"id\": \"1\",
        \"language\": \"en\",
        \"text\": \"I had a great experience!\"
      }
    ]
  }"
```

**Response Fields:**
```json
{
  "documents": [
    {
      "id": "1",
      "sentiment": "positive",
      "confidenceScores": {
        "positive": 0.99,
        "neutral": 0.01,
        "negative": 0.0
      },
      "sentences": [
        {
          "text": "I had a great experience!",
          "sentiment": "positive",
          "confidenceScores": {
            "positive": 0.99,
            "neutral": 0.01,
            "negative": 0.0
          }
        }
      ]
    }
  ],
  "errors": [],
  "modelVersion": "2021-06-01"
}
```

---

### 2. Language Understanding (LUIS)

**Service Description:**
Azure Language Understanding enables applications to understand what people want in their own words through custom machine learning.

**Key Features:**
- Intent recognition
- Entity extraction
- Prebuilt domains
- Active learning recommendations
- Batch prediction

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Max Intents per App** | 500 intents |
| **Max Entities per App** | 500 entities |
| **Max Labels per Document** | 50,000 labels |
| **Max Application Size** | 500 MB |
| **Supported Languages** | 13 languages |
| **Rate Limits** | 50 calls/sec |
| **Prediction Timeout** | 30 seconds |
| **Batch Prediction Size** | Up to 100 utterances |
| **Training Time** | 1-10 minutes |
| **Active Learning Suggestions** | Up to 1000 per week |
| **User Utterances Retention** | 30 days |
| **Model Accuracy Target** | 75-95% depending on data |
| **Free Tier Requests** | 1,000 per month |
| **Slot Limit** | 2 slots per app (Staging, Production) |
| **API Limit per Seat** | Varies by plan |

#### Azure CLI Command

```bash
# Create LUIS Authoring account
az cognitiveservices account create \
  --name myLuisAuthoring \
  --resource-group myResourceGroup \
  --kind LUIS.Authoring \
  --sku F0 \
  --location westus \
  --yes

# Create LUIS Prediction account
az cognitiveservices account create \
  --name myLuisPrediction \
  --resource-group myResourceGroup \
  --kind LUIS \
  --sku S0 \
  --location eastus \
  --yes

# Get authoring key
az cognitiveservices account keys list \
  --name myLuisAuthoring \
  --resource-group myResourceGroup

# Get prediction key
az cognitiveservices account keys list \
  --name myLuisPrediction \
  --resource-group myResourceGroup
```

#### Python Code Example

```python
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

subscription_key = "YOUR_SUBSCRIPTION_KEY"
endpoint = "YOUR_ENDPOINT"
app_id = "YOUR_APP_ID"

client = LUISRuntimeClient(
    endpoint=endpoint,
    credentials=CognitiveServicesCredentials(subscription_key)
)

# Predict intent and entities
query = "Turn on the lights in the living room"

response = client.prediction.resolve(
    app_id=app_id,
    slot_name="Production",
    query=query
)

print(f"Top intent: {response.top_scoring_intent.intent}")
print(f"Confidence: {response.top_scoring_intent.score}")

if response.entities:
    print("Entities detected:")
    for entity in response.entities:
        print(f"  {entity.entity} ({entity.type}): {entity.additional_properties}")
```

#### REST API Example

```bash
curl -X POST \
  "YOUR_ENDPOINT/luis/prediction/v3.0/apps/YOUR_APP_ID/slots/production/predict" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"Turn on the lights in the living room\"}"
```

---

### 3. Conversational Language Understanding (CLU)

**Service Description:**
Azure Conversational Language Understanding enables apps to understand user intents and extract entities from natural language conversations using custom-trained models.

**Key Features:**
- Intent classification
- Entity extraction
- Multi-intent support
- Zero-shot learning capabilities
- Utterance optimization with active learning
- Multilingual support
- Integration with Language service

**Service Limitations:**

| Limitation | Details |
|-----------|----------|
| **Max Intents per Project** | 500 intents |
| **Max Entities per Project** | 500 entities |
| **Max Training Documents** | 100,000 documents |
| **Max Entity Types** | List, Regex, Prebuilt |
| **Supported Languages** | 95+ languages |
| **Rate Limits (Free)** | 2 calls/sec, 200 calls/minute |
| **Rate Limits (Standard)** | 50 calls/sec |
| **Training Time** | 1-10 minutes |
| **Model Accuracy** | 80-98% depending on training data |
| **Maximum Payload Size** | 10 KB per request |
| **Batch Prediction Size** | Up to 1000 utterances |
| **Active Learning Suggestions** | Up to 5000 per month (free tier) |
| **API Versions** | 2022-10-01-preview and later |
| **Token Limits** | 256 tokens per request |
| **Free Tier Quota** | 1000 requests/month |

#### Azure CLI Command

```bash
# Create Language resource for CLU
az cognitiveservices account create \
  --name myLanguageService \
  --resource-group myResourceGroup \
  --kind Language \
  --sku S0 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myLanguageService \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myLanguageService \
  --resource-group myResourceGroup \
  --query properties.endpoint
```

#### Python Code Example - CLU Intent & Entity Recognition

```python
from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint = "YOUR_ENDPOINT"
key = "YOUR_SUBSCRIPTION_KEY"
client = ConversationAnalysisClient(endpoint, AzureKeyCredential(key))

# Analyze conversation
with open("conversational_input.txt") as f:
    query = f.read()

result = client.analyze_conversation(
    task={
        "kind": "Conversation",
        "analysisInput": {
            "conversationItem": {
                "id": "1",
                "participantId": "1",
                "text": query
            }
        },
        "parameters": {
            "projectName": "YOUR_PROJECT_NAME",
            "deploymentName": "YOUR_DEPLOYMENT_NAME",
            "verbose": True
        }
    }
)

print("=== CLU Analysis Results ===")
print(f"Top Intent: {result['result']['prediction']['topIntent']}")
print(f"Confidence: {result['result']['prediction']['intents'][0]['confidenceScore']}")

print("\nIntents:")
for intent in result['result']['prediction']['intents']:
    print(f"  - {intent['category']}: {intent['confidenceScore']:.2%}")

print("\nEntities:")
if result['result']['prediction']['entities']:
    for entity in result['result']['prediction']['entities']:
        print(f"  - {entity['category']}: {entity['text']} (confidence: {entity['confidenceScore']:.2%})")
else:
    print("  No entities detected")
```

#### CLU Schema Definition & Field Explanations

**Project Configuration:**
```json
{
  "projectName": "CustomerServiceBot",
  "language": "en-us",
  "multilingual": false,
  "description": "Conversational AI for customer service",
  "settings": {
    "normalizeAccents": true,
    "caseSensitive": false,
    "confidenceScoreThreshold": 0.5
  }
}
```

**Intent Schema:**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| id | string | Unique intent identifier | intent_001 |
| category | string | Intent name/category | OrderProduct |
| description | string | Intent definition | User wants to purchase a product |
| confidenceScore | float (0-1) | Prediction confidence level | 0.95 |
| utterances | array | Training examples | ["I want to buy", "Order this item"] |

**Entity Schema:**

| Field | Type | Description | Example | Value Type |
|-------|------|-------------|---------|-------------|
| category | string | Entity type name | ProductName | string |
| text | string | Extracted entity value | "laptop" | string |
| confidenceScore | float | Detection confidence (0-1) | 0.92 | number |
| offset | integer | Character position in text | 10 | number |
| length | integer | Character length of entity | 6 | number |
| extraInformation | object | Additional entity metadata | {"type": "PRODUCT"} | object |

**Training Data Format (JSONL):**
```json
{
  "text": "I want to order a blue laptop",
  "intent": "OrderProduct",
  "entities": [
    {
      "category": "Color",
      "offset": 19,
      "length": 4,
      "text": "blue"
    },
    {
      "category": "Product",
      "offset": 24,
      "length": 6,
      "text": "laptop"
    }
  ]
}
```

**API Response Schema:**
```json
{
  "result": {
    "prediction": {
      "topIntent": "OrderProduct",
      "projectKind": "Conversation",
      "intents": [
        {
          "category": "OrderProduct",
          "confidenceScore": 0.98
        },
        {
          "category": "CheckOrder",
          "confidenceScore": 0.01
        }
      ],
      "entities": [
        {
          "category": "Color",
          "text": "blue",
          "offset": 19,
          "length": 4,
          "confidenceScore": 0.95,
          "extraInformation": []
        },
        {
          "category": "Product",
          "text": "laptop",
          "offset": 24,
          "length": 6,
          "confidenceScore": 0.97,
          "extraInformation": []
        }
      ]
    }
  }
}
```

#### REST API Example

```bash
curl -X POST \
  "YOUR_ENDPOINT/language/:analyze-conversations?api-version=2022-10-01-preview" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "kind": "Conversation",
    "analysisInput": {
      "conversationItem": {
        "id": "1",
        "participantId": "1",
        "text": "I want to order a blue laptop"
      }
    },
    "parameters": {
      "projectName": "CustomerServiceBot",
      "deploymentName": "production",
      "verbose": true
    }
  }'
```

---

### 4. Translator

**Service Description:**
Azure Translator provides machine translation across 70+ languages with support for transliteration and language detection.

**Key Features:**
- Text translation
- Document translation
- Transliteration
- Language detection
- Back-translation

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Supported Languages** | 70+ languages |
| **Max Text Size per Request** | 50,000 characters |
| **Rate Limits (Free Tier)** | 2 calls/sec |
| **Rate Limits (Standard)** | 40 calls/sec |
| **Max Document Translation Size** | 2 MB |
| **Translation Accuracy** | 85-95% for common language pairs |
| **Batch Translation Documents** | Up to 1,000 per batch |
| **Processing Time (Batch)** | 1-24 hours depending on size |
| **Custom Translator Projects** | Unlimited (with data) |
| **Custom Translator Document Limit** | 10 million parallel sentences |
| **Transliteration Supported Languages** | 5 languages (Arabic, Chinese, Devanagari, Greek, Russian, etc.) |
| **Back-translation Languages** | 50+ languages |
| **Free Tier Quota** | 2 million characters/month |
| **Data Retention** | Customer data not retained |
| **Timeout** | 30 seconds per request |

#### Azure CLI Command

```bash
# Create Translator account
az cognitiveservices account create \
  --name myTranslator \
  --resource-group myResourceGroup \
  --kind TextTranslation \
  --sku S1 \
  --location global \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myTranslator \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myTranslator \
  --resource-group myResourceGroup \
  --query properties.endpoint
```

#### Python Code Example

```python
import requests
import uuid

subscription_key = "YOUR_SUBSCRIPTION_KEY"
endpoint = "https://api.cognitive.microsofttranslator.com"

def translate_text(text, target_language):
    path = '/translate'
    constructed_url = endpoint + path
    
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': target_language
    }
    
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': 'YOUR_REGION',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    
    body = [{'text': text}]
    
    response = requests.post(
        constructed_url,
        params=params,
        headers=headers,
        json=body
    )
    
    return response.json()

# Translate text
result = translate_text("Hello, how are you?", "es")
print(result[0]['translations'][0]['text'])  # Output: "Hola, ¿cómo estás?"

# Detect language
def detect_language(text):
    path = '/detect'
    constructed_url = endpoint + path
    
    params = {'api-version': '3.0'}
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json'
    }
    body = [{'text': text}]
    
    response = requests.post(
        constructed_url,
        params=params,
        headers=headers,
        json=body
    )
    
    return response.json()

detection = detect_language("Bonjour, comment allez-vous?")
print(detection[0]['language'])  # Output: "fr"
```

#### REST API Example

```bash
curl -X POST \
  "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=es" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d "[{\"text\": \"Hello, how are you?\"}]"
```

**Response:**
```json
[
  {
    "translations": [
      {
        "text": "Hola, ¿cómo estás?",
        "to": "es"
      }
    ]
  }
]
```

---

## Speech Services

### 1. Speech to Text (STT)

**Service Description:**
Azure Speech to Text converts spoken audio into written text with support for multiple languages and dialects.

**Key Features:**
- Real-time speech recognition
- Batch transcription
- Custom speech models
- Phrase lists for improved accuracy
- Language identification

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Supported Languages** | 100+ languages and variants |
| **Audio Format Support** | WAV, MP3, OGG, FLAC, M4A |
| **Audio Sample Rate** | 8 kHz - 48 kHz |
| **Max Audio Duration (Real-time)** | Limited by connection |
| **Max Audio Duration (Batch)** | 600 minutes per file |
| **Batch Transcription File Size** | 2 GB maximum |
| **Accuracy** | 90-95% for clear audio |
| **Rate Limits** | 20 concurrent connections per subscription |
| **Real-time Latency** | <1 second (typical) |
| **Batch Processing Time** | 1-5x real-time duration |
| **Custom Speech Models** | Up to 10 active models |
| **Training Data Size** | 1 GB maximum |
| **Silence Timeout** | 15 seconds |
| **Initial Silence Timeout** | 20 seconds |
| **Final Silence Timeout** | 1 second |
| **Free Tier Monthly Quota** | 1,000 minutes |

#### Azure CLI Command

```bash
# Create Speech Services account
az cognitiveservices account create \
  --name mySpeech \
  --resource-group myResourceGroup \
  --kind SpeechServices \
  --sku S0 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name mySpeech \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name mySpeech \
  --resource-group myResourceGroup \
  --query properties.endpoint

# List all Speech accounts
az cognitiveservices account list \
  --resource-group myResourceGroup \
  --query "[?kind=='SpeechServices']"
```

#### Python Code Example

```python
import azure.cognitiveservices.speech as speechsdk

subscription_key = "YOUR_SUBSCRIPTION_KEY"
region = "YOUR_REGION"

# Create speech config
speech_config = speechsdk.SpeechConfig(
    subscription=subscription_key,
    region=region
)

# Configure output format
speech_config.output_format = speechsdk.OutputFormat.Detailed

# Create speech recognizer from microphone
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# Recognize speech
print("Say something...")
result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print(f"Recognized: {result.text}")
elif result.reason == speechsdk.ResultReason.NoMatch:
    print(f"Not recognized: {result.no_match_details}")
elif result.reason == speechsdk.ResultReason.Canceled:
    print(f"Error: {result.cancellation_details.error_details}")

# Recognize from audio file
audio_config = speechsdk.audio.AudioConfig(filename="path/to/audio.wav")
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config
)

result = speech_recognizer.recognize_once()
print(result.text)
```

#### REST API Example

```bash
curl -X POST \
  "https://YOUR_REGION.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary "@audio.wav"
```

**Response:**
```json
{
  "RecognitionStatus": "Success",
  "DisplayText": "What's the weather like?",
  "Offset": 0,
  "Duration": 23456789,
  "NBest": [
    {
      "Confidence": 0.98,
      "Lexical": "what's the weather like",
      "ITN": "what's the weather like",
      "MaskedITN": "what's the weather like",
      "Display": "What's the weather like?"
    }
  ]
}
```

---

### 2. Text to Speech (TTS)

**Service Description:**
Azure Text to Speech converts written text into natural-sounding speech with multiple voice options and languages.

**Key Features:**
- Neural voices
- Custom voice creation
- Multiple languages and dialects
- SSML support for prosody control
- Real-time synthesis

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Supported Languages** | 140+ languages and variants |
| **Neural Voices Available** | 400+ voices across multiple languages |
| **Audio Output Formats** | MP3, PCM, Opus, ALAW, MULAW, OGG |
| **Audio Sample Rate** | 8 kHz - 48 kHz |
| **Max Text per Request** | 10,000 characters |
| **Synthesis Latency** | <500 ms for typical sentences |
| **Voice Profile Creation** | 10-30 minutes |
| **Custom Voice Phrases Required** | 100+ sentences for training |
| **Custom Voice Accuracy** | 95%+ with good training data |
| **Concurrent Synthesis Requests** | 10-100 (depending on tier) |
| **Rate Limits (Free)** | 20,000 characters/month |
| **Rate Limits (Standard)** | 1,000 requests/hour |
| **SSML Feature Support** | Phoneme, prosody, emphasis, break |
| **Gender Variations** | Male, Female, Neutral options |
| **Pricing Unit** | Per 1 million characters synthesized |

#### Azure CLI Command

```bash
# Create Speech Services account for TTS
az cognitiveservices account create \
  --name mySpeechTTS \
  --resource-group myResourceGroup \
  --kind SpeechServices \
  --sku S0 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name mySpeechTTS \
  --resource-group myResourceGroup

# Show account details
az cognitiveservices account show \
  --name mySpeechTTS \
  --resource-group myResourceGroup
```

#### Python Code Example

```python
import azure.cognitiveservices.speech as speechsdk
import os

subscription_key = "YOUR_SUBSCRIPTION_KEY"
region = "YOUR_REGION"

# Create speech config
speech_config = speechsdk.SpeechConfig(
    subscription=subscription_key,
    region=region
)

# Set the voice
speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"

# Synthesize to speaker
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
)

text = "Hello, this is a test of the text to speech service."

result = speech_synthesizer.speak_text_async(text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized successfully")
elif result.reason == speechsdk.ResultReason.Canceled:
    print(f"Error: {result.cancellation_details.error_details}")

# Synthesize to file
audio_config = speechsdk.audio.AudioOutputConfig(filename="output.wav")
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config
)

result = speech_synthesizer.speak_text_async(text).get()
print(f"Audio saved to output.wav")

# Using SSML for prosody control
ssml_text = """<speak version='1.0' xml:lang='en-US'>
  <voice name='en-US-AriaNeural'>
    <prosody pitch='+50%' rate='0.9'>
      This is a test with modified prosody.
    </prosody>
  </voice>
</speak>"""

result = speech_synthesizer.speak_ssml_async(ssml_text).get()
```

#### REST API Example

```bash
curl -X POST \
  "https://YOUR_REGION.tts.speech.microsoft.com/cognitiveservices/v1" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/ssml+xml" \
  -H "X-Microsoft-OutputFormat: audio-16khz-32kbitrate-mono-mp3" \
  -d "<speak version='1.0' xml:lang='en-US'>
       <voice name='en-US-AriaNeural'>
         Hello, this is a test
       </voice>
      </speak>" \
  --output output.mp3
```

#### SSML Tags and Attributes Reference

**SSML (Speech Synthesis Markup Language)** allows fine-grained control over speech synthesis. Here's a comprehensive guide to all tags and attributes:

##### **Root Tag: `<speak>`**

The root container for SSML content.

| Attribute | Values | Description |
|-----------|--------|-------------|
| `version` | "1.0" | SSML specification version |
| `xml:lang` | "en-US", "fr-FR", etc. | Language and locale code |
| `xmlns` | "http://www.w3.org/2001/10/synthesis" | XML namespace |
| `xmlns:mstts` | "http://www.w3.org/2001/mstts" | Microsoft Text to Speech namespace |

**Example:**
```xml
<speak version="1.0" xml:lang="en-US" xmlns="http://www.w3.org/2001/10/synthesis">
  Content goes here
</speak>
```

---

##### **Voice Selection: `<voice>`**

Selects the voice for speech synthesis.

| Attribute | Values | Description |
|-----------|--------|-------------|
| `name` | "en-US-AriaNeural", "en-US-GuyNeural", etc. | Neural voice name |
| `gender` | "Male", "Female" | Voice gender |
| `age` | "10", "20", "30", etc. | Age of voice (if supported) |
| `variant` | "A", "B", "C" | Voice variant (style variations) |

**Example:**
```xml
<voice name="en-US-AriaNeural">
  This text will be spoken with Aria voice
</voice>
```

**Available Neural Voices:**
- **English (US):** AriaNeural, GuyNeural, JennyNeural, AmberNeural, AshleyNeural, CoraNeural
- **English (UK):** RyanNeural, SoniaNeural
- **French:** DeniseNeural, HenriNeural, ColetteNeural, AlainNeural
- **Spanish:** ConchitaNeural, EnriqueNeural
- **German:** KatjaNeural, ConradNeural
- **Japanese:** Nanami, Keita
- **Chinese (Mandarin):** XiaomoNeural, XiaoxuanNeural, YunyangNeural, YunxiNeural

---

##### **Prosody Control: `<prosody>`**

Modifies pitch, rate, and volume of speech.

| Attribute | Values | Description | Range |
|-----------|--------|-------------|-------|
| `pitch` | "+50Hz", "-50Hz", "+50%", "-20%" | Absolute or relative pitch adjustment | ±50% or ±50Hz |
| `rate` | "0.8", "1.5", "-10%", "+25%" | Speech rate multiplier | 0.5 - 2.0 or -50% to +100% |
| `volume` | "50", "100", "+10%", "-20dB" | Volume level (0-100) or relative dB | 0 - 100 or ±20dB |
| `contour` | "(0%,+20Hz) (10%,+30%) (40%,+10Hz)" | Pitch contour for fine control | N/A |

**Examples:**
```xml
<!-- Increase pitch by 50% -->
<prosody pitch="+50%">
  This sounds higher pitched
</prosody>

<!-- Slow down speech rate -->
<prosody rate="0.8">
  This is spoken slowly
</prosody>

<!-- Increase volume -->
<prosody volume="+5dB">
  This is louder
</prosody>

<!-- Custom pitch contour -->
<prosody contour="(0%,+20Hz) (10%,+30%) (40%,+10Hz) (90%,+20Hz)">
  Complex pitch variation
</prosody>
```

---

##### **Breaks and Pauses: `<break>`**

Inserts silence or breaks between utterances.

| Attribute | Values | Description |
|-----------|--------|-------------|
| `time` | "100ms", "2s" | Duration of break |
| `strength` | "none", "x-weak", "weak", "medium", "strong", "x-strong" | Semantic break strength |

**Example:**
```xml
<speak>
  First sentence.
  <break time="500ms"/>
  Second sentence after a pause.
  <break strength="strong"/>
  Third sentence after a long pause.
</speak>
```

---

##### **Emphasis Control: `<emphasis>`**

Emphasizes text with emotional coloring.

| Attribute | Values | Description |
|-----------|--------|-------------|
| `level` | "strong", "moderate", "reduced" | Emphasis intensity |

**Example:**
```xml
<speak>
  This is <emphasis level="strong">very important</emphasis> information.
  This is <emphasis level="moderate">somewhat important</emphasis>.
  This is <emphasis level="reduced">less important</emphasis>.
</speak>
```

---

##### **Phoneme: `<phoneme>`**

Specifies phonetic pronunciation using ARPABET or IPA.

| Attribute | Values | Description |
|-----------|--------|-------------|
| `alphabet` | "ipa", "sapi" | Phonetic alphabet (IPA or SAPI) |
| `ph` | IPA/ARPABET string | Phonetic transcription |

**Example:**
```xml
<!-- Using ARPABET -->
<phoneme alphabet="sapi">
  You can say it as <phoneme ph="T AE K S">TEKS</phoneme>
</phoneme>

<!-- Using IPA -->
<phoneme alphabet="ipa">
  <phoneme ph="tɛkstəwspeɪʃən">texttospeech</phoneme>
</phoneme>
```

---

##### **Language Switching: `<lang>`**

Switches language within speech.

| Attribute | Values | Description |
|-----------|--------|-------------|
| `xml:lang` | "en-US", "fr-FR", "de-DE", etc. | Language code |

**Example:**
```xml
<speak xml:lang="en-US">
  I speak English
  <lang xml:lang="fr-FR">et un peu de français</lang>
  back to English.
</speak>
```

---

##### **Audio Insertion: `<audio>`**

Plays external audio files.

| Attribute | Values | Description |
|-----------|--------|-------------|
| `src` | URI | Path to audio file (WAV, MP3) |
| `mstts:level` | "0" to "100" | Audio volume level |

**Example:**
```xml
<speak>
  <audio src="https://example.com/sound.wav"/>
  Welcome to our service
</speak>
```

---

##### **Sentence/Word Control: `<s>` and `<w>`**

Marks sentence and word boundaries.

**Example:**
```xml
<speak>
  <s>This is a sentence.</s>
  <s>This is another sentence.</s>
  <w role="amazon:VB">read</w> the document
</speak>
```

---

##### **Microsoft-Specific Tags: `<mstts:*>`**

Special Microsoft extensions for advanced control.

###### **Silence Duration: `<mstts:silence>`**

| Attribute | Values | Description |
|-----------|--------|-------------|
| `type` | "Leading", "Trailing" | Silence position |
| `value` | "200ms", "1s" | Duration |

**Example:**
```xml
<speak>
  <mstts:silence type="Leading" value="500ms"/>
  Hello
  <mstts:silence type="Trailing" value="1s"/>
</speak>
```

###### **Express-As (Emotional Style): `<mstts:express-as>`**

Applies emotional styles to speech.

| Attribute | Values | Description |
|-----------|--------|-------------|
| `style` | "cheerful", "sad", "angry", "fearful", "gentle", "newscast" | Emotion style |
| `styledegree` | "1.0", "2.0" | Intensity of style (1.0-2.0) |
| `role` | "Boy", "Girl", "OlderAdultFemale", "OlderAdultMale", "SeniorFemale", "SeniorMale", "YoungAdultFemale", "YoungAdultMale" | Character role |

**Example:**
```xml
<speak>
  <voice name="en-US-AriaNeural">
    <mstts:express-as style="cheerful" styledegree="2.0">
      I'm so happy to see you!
    </mstts:express-as>
    
    <mstts:express-as style="sad">
      This is unfortunate news.
    </mstts:express-as>
    
    <mstts:express-as style="angry">
      I'm quite upset!
    </mstts:express-as>
  </voice>
</speak>
```

###### **Pitch Range: `<mstts:viseme>`**

Controls visual mouth movements (for avatar synchronization).

| Attribute | Values | Description |
|-----------|--------|-------------|
| `type` | "redlips", "neutral" | Viseme style |

**Example:**
```xml
<speak>
  <mstts:viseme type="neutral">
    This text will sync with neutral mouth movements
  </mstts:viseme>
</speak>
```

---

##### **Sub (Substitution): `<sub>`**

Specifies pronunciation substitution.

| Attribute | Values | Description |
|-----------|--------|-------------|
| `alias` | Text | How to pronounce the text |

**Example:**
```xml
<speak>
  You can read the text as <sub alias="World Wide Web">WWW</sub>
</speak>
```

---

#### Complete SSML Example

```xml
<speak version="1.0" xml:lang="en-US" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts">
  <voice name="en-US-AriaNeural">
    <!-- Introduction with emphasis -->
    <s>
      Welcome to the <emphasis level="strong">Azure Speech Service</emphasis> demonstration.
    </s>
    
    <break time="500ms"/>
    
    <!-- Change pitch and rate -->
    <s>
      <prosody pitch="+50%" rate="0.9">
        Let me explain the key features in detail.
      </prosody>
    </s>
    
    <!-- Emotional expression -->
    <mstts:express-as style="cheerful" styledegree="1.5">
      <s>You're going to love these amazing capabilities!</s>
    </mstts:express-as>
    
    <break strength="medium"/>
    
    <!-- Language switching -->
    <s>
      Our service supports multiple languages:
      <lang xml:lang="fr-FR">Français</lang>,
      <lang xml:lang="de-DE">Deutsch</lang>,
      and <lang xml:lang="es-ES">Español</lang>.
    </s>
    
    <break time="300ms"/>
    
    <!-- Abbreviation pronunciation -->
    <s>
      For more information, visit <sub alias="our website">oursiteURL.com</sub>
    </s>
    
    <!-- Custom phonetics -->
    <s>
      The word <phoneme alphabet="ipa" ph="ˈjuːzəbəl">usable</phoneme> can be pronounced differently.
    </s>
    
    <!-- Final statement with reduced emphasis -->
    <s>
      <emphasis level="reduced">Thank you for your attention.</emphasis>
    </s>
  </voice>
</speak>
```

#### Python Example with SSML

```python
import azure.cognitiveservices.speech as speechsdk

subscription_key = "YOUR_SUBSCRIPTION_KEY"
region = "YOUR_REGION"

speech_config = speechsdk.SpeechConfig(
    subscription=subscription_key,
    region=region
)
speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"

# SSML with multiple features
ssml_content = """
<speak version='1.0' xml:lang='en-US' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts'>
  <voice name='en-US-AriaNeural'>
    <mstts:express-as style='cheerful'>
      <s>Hello! Welcome to Azure Speech Services.</s>
    </mstts:express-as>
    
    <break time='500ms'/>
    
    <prosody pitch='+10%' rate='0.95'>
      <s>This sentence has modified pitch and rate.</s>
    </prosody>
    
    <break strength='strong'/>
    
    <s>
      For technical details, see the <sub alias='documentation'>docs</sub>.
    </s>
  </voice>
</speak>
"""

synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
)

result = synthesizer.speak_ssml_async(ssml_content).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("SSML synthesis successful")
elif result.reason == speechsdk.ResultReason.Canceled:
    print(f"Error: {result.cancellation_details.error_details}")
```

---

#### SSML Best Practices

1. **Always include root attributes:** `version`, `xml:lang`
2. **Use breaks strategically:** Insert `<break>` for natural pausing
3. **Match voice capability:** Check if style/role is supported by chosen voice
4. **Validate XML:** Ensure well-formed XML structure
5. **Test prosody values:** Different voices may interpret pitch/rate differently
6. **Use emotional styles sparingly:** Not all voices support all styles
7. **Optimize for performance:** Keep SSML documents reasonably sized
8. **Browser compatibility:** Some features may not work in all environments

#### Supported Emotional Styles by Voice

| Style | Supported Voices | Use Case |
|-------|------------------|----------|
| cheerful | Most Neural Voices | Positive, friendly content |
| sad | Most Neural Voices | Sorrowful, disappointed tone |
| angry | Most Neural Voices | Frustrated, upset tone |
| fearful | Limited voices | Scared, anxious tone |
| gentle | Most Neural Voices | Soft, calm content |
| newscast | English voices | Professional news reading |

---

### 3. Speaker Recognition

**Service Description:**
Azure Speaker Recognition verifies speaker identity, identifies unknown speakers, and detects speaker changes.

**Key Features:**
- Speaker verification (1:1 matching)
- Speaker identification (1:N matching)
- Speaker diarization

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Supported Languages** | English, Mandarin, Japanese, German, French, Spanish |
| **Audio Format** | PCM, WAV, OGG |
| **Audio Sample Rate** | 16 kHz (recommended) |
| **Min Enrollment Audio** | 20-30 seconds per speaker |
| **Verification Accuracy** | 97-99% with sufficient training |
| **Identification Max Speakers** | 10,000 speakers per project |
| **Identification Latency** | 2-5 seconds |
| **Speaker Profiles per Subscription** | Unlimited |
| **Speech Passphrase Length** | 4-12 seconds |
| **Passphrase Variations** | Up to 5 variations for enrollment |
| **Recognition Timeout** | 30 seconds |
| **Diarization Accuracy** | 85-95% |
| **Max Speakers per Audio (Diarization)** | 10 speakers |
| **Profile Retention** | Indefinite (customer managed) |
| **Concurrent Requests** | Based on subscription tier |

#### Azure CLI Command

```bash
# Create Speech Services account for Speaker Recognition
az cognitiveservices account create \
  --name mySpeakerRecognition \
  --resource-group myResourceGroup \
  --kind SpeechServices \
  --sku S0 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name mySpeakerRecognition \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name mySpeakerRecognition \
  --resource-group myResourceGroup \
  --query properties.endpoint
```

#### Python Code Example

```python
from azure.cognitiveservices.speech.speaker import SpeakerRecognitionClient
from msrest.authentication import CognitiveServicesCredentials

subscription_key = "YOUR_SUBSCRIPTION_KEY"
region = "YOUR_REGION"

client = SpeakerRecognitionClient(
    endpoint=f"https://{region}.api.cognitive.microsoft.com",
    credentials=CognitiveServicesCredentials(subscription_key)
)

# Enrollment (speaker verification)
enrollment_audio = open("enrollment.wav", "rb")

enrollment_profile = client.speaker_profiles.create_enrollment_from_mic(
    locale="en-us"
)

response = client.speaker_recognition.enroll_profile_from_mic(
    profile_id=enrollment_profile.profile_id,
    enrollment_speech=enrollment_audio
)

print(f"Enrollment status: {response.enrollment_status}")
print(f"Remaining enrollments: {response.remaining_enrollment_speech_required_count}")

# Verification
verification_audio = open("verification.wav", "rb")

verification_result = client.speaker_recognition.verify_profile_from_mic(
    profile_id=enrollment_profile.profile_id,
    verification_speech=verification_audio
)

print(f"Verified: {verification_result.result == 'Accept'}")
print(f"Confidence: {verification_result.confidence}")
```

---

## Document Intelligence

### 1. Document Intelligence (Form Recognizer)

**Service Description:**
Azure Document Intelligence extracts structured data from documents including forms, invoices, receipts, and custom documents using prebuilt models and trainable custom models.

**Key Features:**
- Prebuilt models (invoices, receipts, IDs, business cards, W2 tax forms, health insurance cards)
- Custom model training (template-based and neural)
- Layout analysis and OCR
- Table extraction with cell content analysis
- Handwriting recognition (Print and Cursive)
- Composed models (combining multiple custom models)
- Confidence scores for all extracted fields
- Support for documents in 73 languages

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Supported File Formats** | PDF, JPEG, PNG, BMP, TIFF, HEIC |
| **Max File Size** | 2000 pages per document |
| **Max File Size (MB)** | 500 MB for single file |
| **Max Dimensions** | 50 pixels to 10,000 pixels |
| **Image Resolution** | Minimum 150 DPI recommended |
| **Processing Time** | <60 seconds for most documents |
| **Batch Processing Files** | Up to 2000 files per batch |
| **Custom Model Training Samples** | Minimum 5, recommended 50+ |
| **Training Data Size** | Max 100 MB per project |
| **Handwriting Recognition Accuracy** | 80-90% for clear handwriting |
| **OCR Languages Supported** | 73 languages |
| **Table Detection** | Up to 1000 cells per table |
| **Entity Detection Accuracy** | 95%+ for structured forms |
| **Rate Limits (Free)** | 2 transactions per minute |
| **Rate Limits (Standard)** | 15 transactions per second |
| **Maximum Requests per Month (Free)** | 500 pages |
| **Model Versions Available** | 3.0, 4.0 (latest) |
| **Prebuilt Models Available** | 12+ models (Invoice, Receipt, ID, Business Card, W2, Health Insurance, etc.) |
| **Custom Models per Account** | Unlimited |
| **Composed Models** | Can combine up to 100 custom models |

#### Azure CLI Command

```bash
# Create Document Intelligence account
az cognitiveservices account create \
  --name myDocumentIntelligence \
  --resource-group myResourceGroup \
  --kind FormRecognizer \
  --sku S0 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myDocumentIntelligence \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myDocumentIntelligence \
  --resource-group myResourceGroup \
  --query properties.endpoint

# Create with advanced options
az cognitiveservices account create \
  --name myAdvancedFormRecognizer \
  --resource-group myResourceGroup \
  --kind FormRecognizer \
  --sku S0 \
  --location eastus \
  --public-network-access Enabled \
  --yes

# List available models
az cognitiveservices account list-models \
  --name myDocumentIntelligence \
  --resource-group myResourceGroup
```

#### Python Code Example - Prebuilt Models

```python
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
import json

subscription_key = "YOUR_SUBSCRIPTION_KEY"
endpoint = "YOUR_ENDPOINT"

client = DocumentIntelligenceClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(subscription_key)
)

# Analyze invoice using prebuilt model
with open("invoice.pdf", "rb") as f:
    poller = client.begin_analyze_document(
        model_id="prebuilt-invoice",
        document=f
    )

result = poller.result()

print("=== Invoice Analysis ===")
for document in result.documents:
    print(f"Document Type: {document.doc_type}")
    print(f"Confidence: {document.confidence}")
    
    fields = document.fields
    print(f"\nInvoice ID: {fields.get('InvoiceId', {}).get('valueString', 'N/A')}")
    print(f"Invoice Date: {fields.get('InvoiceDate', {}).get('valueDate', 'N/A')}")
    print(f"Due Date: {fields.get('DueDate', {}).get('valueDate', 'N/A')}")
    print(f"Vendor Name: {fields.get('VendorName', {}).get('valueString', 'N/A')}")
    print(f"Customer Name: {fields.get('CustomerName', {}).get('valueString', 'N/A')}")
    print(f"Subtotal: {fields.get('SubTotal', {}).get('valueCurrency', {}).get('amount', 'N/A')}")
    print(f"Tax Amount: {fields.get('TaxAmount', {}).get('valueCurrency', {}).get('amount', 'N/A')}")
    print(f"Invoice Total: {fields.get('InvoiceTotal', {}).get('valueCurrency', {}).get('amount', 'N/A')}")
    
    # Line items
    line_items = fields.get('Items', {}).get('valueArray', [])
    if line_items:
        print("\n=== Line Items ===")
        for item in line_items:
            item_fields = item.get('valueObject', {})
            print(f"  Description: {item_fields.get('Description', {}).get('valueString', 'N/A')}")
            print(f"  Quantity: {item_fields.get('Quantity', {}).get('valueNumber', 'N/A')}")
            print(f"  Unit Price: {item_fields.get('UnitPrice', {}).get('valueCurrency', {}).get('amount', 'N/A')}")
            print(f"  Amount: {item_fields.get('Amount', {}).get('valueCurrency', {}).get('amount', 'N/A')}")

# Analyze receipt using prebuilt model
with open("receipt.jpg", "rb") as f:
    poller = client.begin_analyze_document(
        model_id="prebuilt-receipt",
        document=f
    )

result = poller.result()

print("\n=== Receipt Analysis ===")
for document in result.documents:
    fields = document.fields
    print(f"Merchant Name: {fields.get('MerchantName', {}).get('valueString', 'N/A')}")
    print(f"Transaction Date: {fields.get('TransactionDate', {}).get('valueDate', 'N/A')}")
    print(f"Transaction Time: {fields.get('TransactionTime', {}).get('valueTime', 'N/A')}")
    print(f"Subtotal: {fields.get('Subtotal', {}).get('valueCurrency', {}).get('amount', 'N/A')}")
    print(f"Tax: {fields.get('Tax', {}).get('valueCurrency', {}).get('amount', 'N/A')}")
    print(f"Tip: {fields.get('Tip', {}).get('valueCurrency', {}).get('amount', 'N/A')}")
    print(f"Total: {fields.get('Total', {}).get('valueCurrency', {}).get('amount', 'N/A')}")

# Analyze ID document using prebuilt model
with open("id_document.jpg", "rb") as f:
    poller = client.begin_analyze_document(
        model_id="prebuilt-idDocument",
        document=f
    )

result = poller.result()

print("\n=== ID Document Analysis ===")
for document in result.documents:
    fields = document.fields
    print(f"Document Type: {fields.get('DocumentType', {}).get('valueString', 'N/A')}")
    print(f"First Name: {fields.get('FirstName', {}).get('valueString', 'N/A')}")
    print(f"Last Name: {fields.get('LastName', {}).get('valueString', 'N/A')}")
    print(f"Date of Birth: {fields.get('DateOfBirth', {}).get('valueDate', 'N/A')}")
    print(f"Expiration Date: {fields.get('ExpirationDate', {}).get('valueDate', 'N/A')}")
    print(f"Document Number: {fields.get('DocumentNumber', {}).get('valueString', 'N/A')}")
    print(f"Address: {fields.get('Address', {}).get('valueString', 'N/A')}")
```

#### Python Code Example - Custom Model Training

```python
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import BuildDocumentModelRequest, AzureBlobContentSource
from azure.core.credentials import AzureKeyCredential

client = DocumentIntelligenceClient(
    endpoint="YOUR_ENDPOINT",
    credential=AzureKeyCredential("YOUR_SUBSCRIPTION_KEY")
)

# Template model - best for consistent forms with fixed layout
print("=== Building Template Model ===")
build_request = BuildDocumentModelRequest(
    model_id="custom-invoice-template",
    description="Custom invoice model using template mode",
    build_mode="template",
    azure_blob_source=AzureBlobContentSource(
        container_url="https://yourstorage.blob.core.windows.net/training-docs",
        prefix="invoices/"
    )
)

template_poller = client.begin_build_document_model(build_request)
template_model = template_poller.result()

print(f"Template Model ID: {template_model.model_id}")
print(f"Status: {template_model.status}")
print(f"Created: {template_model.created_date_time}")

# Neural model - best for varying layouts and forms
print("\n=== Building Neural Model ===")
build_request = BuildDocumentModelRequest(
    model_id="custom-invoice-neural",
    description="Custom invoice model using neural mode",
    build_mode="neural",
    azure_blob_source=AzureBlobContentSource(
        container_url="https://yourstorage.blob.core.windows.net/training-docs",
        prefix="invoices/"
    )
)

neural_poller = client.begin_build_document_model(build_request)
neural_model = neural_poller.result()

print(f"Neural Model ID: {neural_model.model_id}")
print(f"Status: {neural_model.status}")

# Use custom model for analysis
print("\n=== Analyzing with Custom Model ===")
with open("custom_invoice.pdf", "rb") as f:
    poller = client.begin_analyze_document(
        model_id="custom-invoice-template",
        document=f
    )

result = poller.result()

for document in result.documents:
    print(f"Doc Type: {document.doc_type}")
    print(f"Confidence: {document.confidence}")
    
    for field_name, field_value in document.fields.items():
        if field_value.value is not None:
            print(f"  {field_name}: {field_value.value} (confidence: {field_value.confidence})")

# Composed model - combine multiple custom models
print("\n=== Building Composed Model ===")
composed_model_request = {
    "model_id": "composed-document-processor",
    "description": "Composed model for invoices and receipts",
    "document_types": {
        "invoice": {
            "azure_document_model_id": f"{template_model.model_id}"
        },
        "receipt": {
            "azure_document_model_id": "prebuilt-receipt"
        }
    }
}

composed_poller = client.begin_build_document_model(composed_model_request)
composed_model = composed_poller.result()

print(f"Composed Model ID: {composed_model.model_id}")
print(f"Status: {composed_model.status}")

# Analyze with composed model
with open("document.pdf", "rb") as f:
    poller = client.begin_analyze_document(
        model_id="composed-document-processor",
        document=f
    )

result = poller.result()
print(f"Detected document type: {result.documents[0].doc_type}")
```

---

### 2. Prebuilt Models - Complete Schema Reference

#### Invoice Model (`prebuilt-invoice`)

**Field Definitions:**

| Field Name | Field Type | Value Type | Description | Example |
|-----------|-----------|-----------|-----------|---------|
| InvoiceId | string | valueString | Unique invoice identifier/number | INV-2024-001 |
| InvoiceDate | date | valueDate | Date invoice was issued | 2024-01-15 |
| DueDate | date | valueDate | Payment due date | 2024-02-15 |
| VendorName | string | valueString | Seller/vendor company name | Acme Corp |
| VendorAddress | string | valueString | Seller's full address | 123 Business St, City, ST 12345 |
| VendorPhone | phone | valuePhoneNumber | Vendor contact phone | (555) 123-4567 |
| VendorEmail | email | valueString | Vendor email address | vendor@acme.com |
| VendorTaxId | string | valueString | Tax identification number | 12-3456789 |
| CustomerName | string | valueString | Buyer/customer company name | ABC Company |
| CustomerAddress | string | valueString | Customer's billing/shipping address | 456 Main Ave, Town, ST 67890 |
| CustomerId | string | valueString | Customer reference or account number | CUST-789 |
| Items | array | valueArray | Array of line item objects | [item1, item2, ...] |
| Items[].Description | string | valueString | Product/service description | Widget Services |
| Items[].Quantity | number | valueNumber | Item quantity ordered | 5 |
| Items[].UnitPrice | currency | valueCurrency | Price per unit | 100.00 |
| Items[].Amount | currency | valueCurrency | Line total (quantity × price) | 500.00 |
| Subtotal | currency | valueCurrency | Total before tax and discounts | 1000.00 |
| TaxAmount | currency | valueCurrency | Tax amount charged | 80.00 |
| DiscountAmount | currency | valueCurrency | Total discount applied | 50.00 |
| ShippingAmount | currency | valueCurrency | Shipping/delivery cost | 25.00 |
| InvoiceTotal | currency | valueCurrency | Final total amount due | 1055.00 |
| PaymentTerms | string | valueString | Terms of payment (Net 30, Due on Receipt, etc.) | Net 30 |
| PurchaseOrder | string | valueString | PO number reference | PO-2024-5678 |
| BillingAddress | string | valueString | Specific billing address | Same as customer |
| ShippingAddress | string | valueString | Specific shipping address | Warehouse 2, Floor 3 |

**Sample Response:**
```json
{
  "status": "succeeded",
  "analyzeResult": {
    "documents": [
      {
        "docType": "invoice",
        "confidence": 0.98,
        "fields": {
          "InvoiceId": {"valueString": "INV-2024-001", "confidence": 0.99},
          "InvoiceDate": {"valueDate": "2024-01-15", "confidence": 0.99},
          "DueDate": {"valueDate": "2024-02-15", "confidence": 0.99},
          "VendorName": {"valueString": "Acme Corporation", "confidence": 0.98},
          "CustomerName": {"valueString": "ABC Company", "confidence": 0.97},
          "Items": {
            "valueArray": [
              {
                "valueObject": {
                  "Description": {"valueString": "Consulting Services", "confidence": 0.96},
                  "Quantity": {"valueNumber": 10, "confidence": 0.98},
                  "UnitPrice": {"valueCurrency": {"amount": 150.00, "currencySymbol": "$"}, "confidence": 0.97},
                  "Amount": {"valueCurrency": {"amount": 1500.00, "currencySymbol": "$"}, "confidence": 0.97}
                }
              }
            ]
          },
          "Subtotal": {"valueCurrency": {"amount": 1500.00, "currencySymbol": "$"}, "confidence": 0.98},
          "TaxAmount": {"valueCurrency": {"amount": 120.00, "currencySymbol": "$"}, "confidence": 0.96},
          "InvoiceTotal": {"valueCurrency": {"amount": 1620.00, "currencySymbol": "$"}, "confidence": 0.98}
        }
      }
    ]
  }
}
```

#### Receipt Model (`prebuilt-receipt`)

**Field Definitions:**

| Field Name | Field Type | Value Type | Description | Example |
|-----------|-----------|-----------|-----------|---------|
| MerchantName | string | valueString | Store/merchant name | Target Store #2341 |
| MerchantAddress | string | valueString | Store location address | 789 Retail Ave, City, ST 12345 |
| MerchantPhoneNumber | phone | valuePhoneNumber | Store phone number | (555) 987-6543 |
| TransactionDate | date | valueDate | Date of purchase | 2024-01-20 |
| TransactionTime | time | valueTime | Time of purchase (24-hour) | 14:30:00 |
| Items | array | valueArray | Array of purchased items | [item1, item2, ...] |
| Items[].Name | string | valueString | Item product name/description | Milk - Whole 1 Gallon |
| Items[].Quantity | number | valueNumber | Quantity purchased | 2 |
| Items[].Price | currency | valueCurrency | Price per unit | 3.99 |
| Items[].TotalPrice | currency | valueCurrency | Line item total | 7.98 |
| Subtotal | currency | valueCurrency | Subtotal before tax | 45.50 |
| Tax | currency | valueCurrency | Sales tax amount | 3.64 |
| Tip | currency | valueCurrency | Tip/gratuity amount | 5.00 |
| Total | currency | valueCurrency | Final amount paid | 54.14 |
| PaymentMethod | string | valueString | How payment was made | Credit Card, Cash, Mobile Pay |
| CardNumber | string | valueString | Last 4 digits of card (masked) | ****1234 |
| ReceiptNumber | string | valueString | Receipt/transaction ID | REC-2024-789456 |

**Sample Response:**
```json
{
  "analyzeResult": {
    "documents": [
      {
        "docType": "receipt",
        "confidence": 0.96,
        "fields": {
          "MerchantName": {"valueString": "Target Store #2341", "confidence": 0.98},
          "TransactionDate": {"valueDate": "2024-01-20", "confidence": 0.99},
          "TransactionTime": {"valueTime": "14:30:00", "confidence": 0.97},
          "Items": {
            "valueArray": [
              {
                "valueObject": {
                  "Name": {"valueString": "Milk - Whole 1 Gallon", "confidence": 0.95},
                  "Quantity": {"valueNumber": 2, "confidence": 0.98},
                  "Price": {"valueCurrency": {"amount": 3.99, "currencySymbol": "$"}, "confidence": 0.96},
                  "TotalPrice": {"valueCurrency": {"amount": 7.98, "currencySymbol": "$"}, "confidence": 0.96}
                }
              }
            ]
          },
          "Subtotal": {"valueCurrency": {"amount": 45.50, "currencySymbol": "$"}, "confidence": 0.97},
          "Tax": {"valueCurrency": {"amount": 3.64, "currencySymbol": "$"}, "confidence": 0.96},
          "Total": {"valueCurrency": {"amount": 54.14, "currencySymbol": "$"}, "confidence": 0.97}
        }
      }
    ]
  }
}
```

#### ID Document Model (`prebuilt-idDocument`)

**Field Definitions:**

| Field Name | Field Type | Value Type | Description | Example |
|-----------|-----------|-----------|-----------|---------|
| DocumentType | string | valueString | Type of ID document | Driver's License, Passport, ID Card |
| FirstName | string | valueString | Given name | John |
| LastName | string | valueString | Family name | Smith |
| FullName | string | valueString | Complete legal name | John Smith |
| DateOfBirth | date | valueDate | Date of birth | 1985-06-15 |
| Sex | string | valueString | Gender (M/F) | M |
| Address | string | valueString | Residential address | 123 Main St, Apt 4B, City, ST 12345 |
| City | string | valueString | City of residence | Springfield |
| State | string | valueString | State/province | IL |
| PostalCode | string | valueString | ZIP/postal code | 62701 |
| Country | string | valueString | Country code or name | USA, US |
| DocumentNumber | string | valueString | License/ID number | L12345678 |
| IssueDate | date | valueDate | Document issue date | 2019-08-20 |
| ExpirationDate | date | valueDate | Document expiration date | 2025-08-20 |
| IssuingCountry | string | valueString | Country that issued document | United States |
| IssuingState | string | valueString | State/province that issued document | Illinois |
| Height | string | valueString | Height in feet/cm | 5'11" |
| EyeColor | string | valueString | Eye color | Blue |
| HairColor | string | valueString | Hair color | Brown |
| Endorsements | string | valueString | License endorsements | Commercial, Motorcycle |
| Restrictions | string | valueString | License restrictions | Corrective lenses required |

**Sample Response:**
```json
{
  "analyzeResult": {
    "documents": [
      {
        "docType": "idDocument",
        "confidence": 0.99,
        "fields": {
          "DocumentType": {"valueString": "Driver's License", "confidence": 0.99},
          "FirstName": {"valueString": "John", "confidence": 0.99},
          "LastName": {"valueString": "Smith", "confidence": 0.99},
          "DateOfBirth": {"valueDate": "1985-06-15", "confidence": 0.99},
          "Address": {"valueString": "123 Main St, Springfield, IL 62701", "confidence": 0.98},
          "DocumentNumber": {"valueString": "L12345678", "confidence": 0.99},
          "ExpirationDate": {"valueDate": "2025-08-20", "confidence": 0.99}
        }
      }
    ]
  }
}
```

#### Business Card Model (`prebuilt-businessCard`)

**Field Definitions:**

| Field Name | Field Type | Value Type | Description | Example |
|-----------|-----------|-----------|-----------|---------|
| ContactNames | array | valueArray | Array of contact person names | [{"firstName": "John", "lastName": "Smith"}] |
| CompanyNames | array | valueArray | Array of company names | ["Acme Corporation"] |
| PhoneNumbers | array | valueArray | Array of phone numbers | ["(555) 123-4567", "(555) 123-4568"] |
| Emails | array | valueArray | Array of email addresses | ["john@acme.com", "contact@acme.com"] |
| Websites | array | valueArray | Array of website URLs | ["https://www.acme.com"] |
| Addresses | array | valueArray | Array of physical addresses | ["123 Business Ave, City, ST 12345"] |
| JobTitles | array | valueArray | Array of job titles | ["Sales Manager", "Regional Director"] |
| Departments | array | valueArray | Array of department names | ["Sales", "Business Development"] |
| Fax | phone | valuePhoneNumber | Facsimile number | (555) 123-4599 |
| Website | string | valueString | Primary website URL | https://www.acme.com |
| MobilePhone | phone | valuePhoneNumber | Mobile/cell number | (555) 987-6543 |

**Sample Response:**
```json
{
  "analyzeResult": {
    "documents": [
      {
        "docType": "businessCard",
        "confidence": 0.97,
        "fields": {
          "ContactNames": {
            "valueArray": [
              {
                "valueObject": {
                  "FirstName": {"valueString": "John", "confidence": 0.98},
                  "LastName": {"valueString": "Smith", "confidence": 0.98}
                }
              }
            ]
          },
          "CompanyNames": {
            "valueArray": [{"valueString": "Acme Corporation", "confidence": 0.99}]
          },
          "JobTitles": {
            "valueArray": [{"valueString": "Sales Manager", "confidence": 0.97}]
          },
          "PhoneNumbers": {
            "valueArray": [{"valuePhoneNumber": "(555) 123-4567", "confidence": 0.98}]
          },
          "Emails": {
            "valueArray": [{"valueString": "john@acme.com", "confidence": 0.99}]
          },
          "Websites": {
            "valueArray": [{"valueString": "https://www.acme.com", "confidence": 0.98}]
          }
        }
      }
    ]
  }
}
```

#### W2 Tax Form Model (`prebuilt-taxUSW2`)

**Field Definitions:**

| Field Name | Field Type | Value Type | Description | Example |
|-----------|-----------|-----------|-----------|---------|
| W2FormVariant | string | valueString | Form variant (typically "W2") | W2 |
| EmployeeSSN | string | valueString | Employee Social Security Number (masked) | ***-**-4567 |
| EmployeeName | string | valueString | Employee's full legal name | John Smith |
| EmployeeAddress | string | valueString | Employee's address | 123 Main St, City, ST 12345 |
| EmployersEIN | string | valueString | Employer's EIN/Tax ID | 12-3456789 |
| EmployerName | string | valueString | Employer company name | ABC Corporation |
| EmployerAddress | string | valueString | Employer's address | 456 Business Ave, City, ST 67890 |
| TaxYear | number | valueNumber | Tax year the W2 covers | 2023 |
| WagesTipsOtherCompensation | currency | valueCurrency | Box 1: Total wages, tips, other compensation | 75000.00 |
| FederalIncomeTaxWithheld | currency | valueCurrency | Box 2: Federal income tax withheld | 12000.00 |
| SocialSecurityWages | currency | valueCurrency | Box 3: Social Security wages | 75000.00 |
| SocialSecurityTaxWithheld | currency | valueCurrency | Box 4: Social Security tax withheld | 4650.00 |
| MedicareWagesAndTips | currency | valueCurrency | Box 5: Medicare wages and tips | 75000.00 |
| MedicareTaxWithheld | currency | valueCurrency | Box 6: Medicare tax withheld | 1087.50 |
| SocialSecurityTipsReported | currency | valueCurrency | Box 7: Social Security tips reported | 500.00 |
| AllocatedTips | currency | valueCurrency | Box 8: Allocated tips | 0.00 |
| AdvancedEICPayment | currency | valueCurrency | Box 9: Advanced EIC payment | 0.00 |
| DependentCarePayments | currency | valueCurrency | Box 10: Dependent care payments | 0.00 |
| NonqualifiedPlans | currency | valueCurrency | Box 11: Non-qualified plans | 0.00 |
| Box12Items | array | valueArray | Box 12 items (various deductions) | [{"code": "D", "amount": 3000}] |
| StateIncomeTaxWithheld | currency | valueCurrency | State income tax withheld | 3000.00 |
| LocalIncomeTaxWithheld | currency | valueCurrency | Local income tax withheld | 500.00 |

**Sample Response:**
```json
{
  "analyzeResult": {
    "documents": [
      {
        "docType": "taxUSW2",
        "confidence": 0.98,
        "fields": {
          "W2FormVariant": {"valueString": "W2", "confidence": 0.99},
          "TaxYear": {"valueNumber": 2023, "confidence": 0.99},
          "EmployeeName": {"valueString": "John Smith", "confidence": 0.99},
          "EmployersEIN": {"valueString": "12-3456789", "confidence": 0.99},
          "EmployerName": {"valueString": "ABC Corporation", "confidence": 0.98},
          "WagesTipsOtherCompensation": {"valueCurrency": {"amount": 75000.00, "currencySymbol": "$"}, "confidence": 0.99},
          "FederalIncomeTaxWithheld": {"valueCurrency": {"amount": 12000.00, "currencySymbol": "$"}, "confidence": 0.98},
          "SocialSecurityWages": {"valueCurrency": {"amount": 75000.00, "currencySymbol": "$"}, "confidence": 0.99},
          "SocialSecurityTaxWithheld": {"valueCurrency": {"amount": 4650.00, "currencySymbol": "$"}, "confidence": 0.98}
        }
      }
    ]
  }
}
```

---

### 3. Custom Model Types and Training Strategies

#### Template Model
- **Best For:** Forms with consistent, fixed layout (templates)
- **Requirements:** 5-20 training documents recommended
- **Training Time:** 1-5 minutes
- **Accuracy:** High (95%+) for fixed layouts
- **Advantages:** Fast training, good for standardized documents
- **Disadvantages:** Fails if layout varies significantly
- **Use Case:** Company invoices, standard contracts, standardized forms

#### Neural Model
- **Best For:** Documents with varying layouts and structures
- **Requirements:** 20-100+ training documents recommended for best results
- **Training Time:** 15-60 minutes
- **Accuracy:** 85-95% for variable layouts
- **Advantages:** Handles layout variations, more flexible
- **Disadvantages:** Requires more training data, longer training time
- **Use Case:** Different vendor invoices, scanned documents, handwritten forms

#### Composed Model
- **Best For:** Combining multiple custom models or custom + prebuilt
- **Requirements:** Minimum 2 component models
- **Training Time:** < 1 minute (no retraining)
- **Maximum Components:** Up to 100 models
- **Use Case:** Process multiple document types in single request

#### REST API Example - Custom Model Training

```bash
# Build custom model
curl -X POST \
  "YOUR_ENDPOINT/documentintelligence/documentModels:build?api-version=2024-02-29-preview" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": "custom-invoice-model",
    "description": "Custom model for company-specific invoices",
    "build_mode": "template",
    "azure_blob_source": {
      "container_url": "https://yourstorage.blob.core.windows.net/training-docs",
      "prefix": "invoices/"
    }
  }'

# Response includes operation-location header with polling URL

# Get model info
curl -X GET \
  "YOUR_ENDPOINT/documentintelligence/documentModels/custom-invoice-model?api-version=2024-02-29-preview" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY"

# Response
{
  "model_id": "custom-invoice-model",
  "status": "ready",
  "description": "Custom model for company-specific invoices",
  "created_date_time": "2024-01-20T10:30:00Z",
  "document_types": {
    "invoice": {
      "field_schema": {
        "InvoiceNumber": {"type": "string"},
        "InvoiceDate": {"type": "date"},
        "VendorName": {"type": "string"},
        "InvoiceTotal": {"type": "currency"},
        "LineItems": {
          "type": "array",
          "items": {
            "Description": {"type": "string"},
            "Amount": {"type": "currency"}
          }
        }
      }
    }
  }
}

# Analyze with custom model
curl -X POST \
  "YOUR_ENDPOINT/documentintelligence/documentModels/custom-invoice-model:analyze?api-version=2024-02-29-preview" \
  -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" \
  -H "Content-Type: application/octet-stream" \
  --data-binary "@invoice.pdf"
```

---

### 4. Document Intelligence - Advanced Features

#### Feature: Layout Analysis

Extracts document structure including paragraphs, sections, tables, and visual elements.

```python
# Analyze layout
with open("document.pdf", "rb") as f:
    poller = client.begin_analyze_document(
        model_id="prebuilt-layout",
        document=f
    )

result = poller.result()

for page in result.pages:
    print(f"Page {page.page_number}:")
    print(f"  Width: {page.width}, Height: {page.height}")
    print(f"  Rotation angle: {page.angle}")
    
    # Paragraphs
    for paragraph in page.paragraphs or []:
        print(f"  Paragraph: {paragraph.content}")
    
    # Tables
    for table in page.tables or []:
        print(f"  Table: {table.row_count} rows, {table.column_count} columns")
        for cell in table.cells:
            print(f"    [{cell.row_index},{cell.column_index}]: {cell.content}")
```

#### Feature: Confidence Scores

All extracted fields include confidence scores (0-1) indicating extraction reliability.

```python
# Access confidence scores
for document in result.documents:
    for field_name, field_value in document.fields.items():
        confidence = field_value.confidence
        if confidence < 0.90:
            print(f"Low confidence ({confidence}) for {field_name}: {field_value.value}")
        elif confidence < 0.70:
            print(f"CRITICAL: Very low confidence ({confidence}) for {field_name} - REVIEW REQUIRED")
```

#### Feature: Table Extraction with Cell Analysis

```python
# Extract and analyze tables
for page in result.pages:
    for table in page.tables or []:
        print(f"Found table: {table.row_count} rows × {table.column_count} cols")
        
        # Get headers (usually first row)
        headers = []
        for cell in table.cells:
            if cell.row_index == 0:
                headers.append(cell.content)
        
        print(f"Headers: {headers}")
        
        # Get data rows
        for row_idx in range(1, table.row_count):
            row_data = []
            for col_idx in range(table.column_count):
                # Find cell at this position
                cell_content = next(
                    (cell.content for cell in table.cells 
                     if cell.row_index == row_idx and cell.column_index == col_idx),
                    ""
                )
                row_data.append(cell_content)
            print(f"Row {row_idx}: {row_data}")
```

---

## Video Indexer

### 1. Azure Video Indexer

**Service Description:**
Azure Video Indexer extracts insights from video and audio files including transcription, sentiment analysis, face recognition, and scene detection.

**Key Features:**
- Automatic transcription with speaker diarization
- Face detection and recognition
- Keyword extraction
- Sentiment analysis
- Scene detection
- Custom language models
- Content moderation

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Supported Video Formats** | MP4, MOV, WMV, AVI, FLV, MKV, WEBM |
| **Supported Audio Formats** | MP3, WAV, M4A, FLAC, OGG, AMR |
| **Max Video Duration** | No strict limit (tested up to 10+ hours) |
| **Max File Size** | 2000 MB (2 GB) |
| **Video Resolution** | 240p to 4K (1080p recommended) |
| **Processing Time** | 1-24 hours depending on length |
| **Indexing Accuracy** | 85-95% for transcription |
| **Face Recognition Accuracy** | 90-95% with good quality video |
| **Supported Languages** | 65+ languages |
| **Speaker Diarization** | Up to 10 speakers identified |
| **Keywords Extracted** | Up to 2000 per video |
| **Sentiment Analysis Granularity** | Per sentence/segment |
| **Content Moderation** | Adult, Racy, Violent content detection |
| **Custom Language Models** | Unlimited (with data) |
| **Video Retention** | 90 days (default, configurable) |
| **API Rate Limit** | 100 requests/minute |
| **Concurrent Uploads** | 10 videos per account |

#### Azure CLI Command

```bash
# Create Storage account for Video Indexer
az storage account create \
  --name myvideoindexerstorage \
  --resource-group myResourceGroup \
  --location eastus \
  --sku Standard_LRS

# Create Media Services account (prerequisite)
az ams account create \
  --name myMediaServicesAccount \
  --resource-group myResourceGroup \
  --storage-account myvideoindexerstorage \
  --location eastus

# Get storage key
az storage account keys list \
  --name myvideoindexerstorage \
  --resource-group myResourceGroup

# Note: Video Indexer API key is obtained from Azure portal
# after setting up the Media Services account
```

#### Python Code Example

```python
import requests
import time

api_key = "YOUR_API_KEY"
location = "YOUR_LOCATION"
account_id = "YOUR_ACCOUNT_ID"

# Upload and index video
def upload_video(video_file_path):
    url = f"https://api.videoindexer.ai/{location}/Accounts/{account_id}/Videos"
    
    params = {
        "accessToken": api_key,
        "name": "sample-video",
        "description": "Sample video for indexing",
        "privacy": "Private"
    }
    
    with open(video_file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, params=params, files=files)
    
    return response.json()

# Upload video
video_info = upload_video("sample.mp4")
video_id = video_info["id"]
print(f"Video uploaded: {video_id}")

# Wait for indexing to complete
def get_video_index(video_id):
    url = f"https://api.videoindexer.ai/{location}/Accounts/{account_id}/Videos/{video_id}/Index"
    
    params = {"accessToken": api_key}
    response = requests.get(url, params=params)
    
    index = response.json()
    
    if index["state"] == "Processed":
        return index
    else:
        print(f"Indexing in progress... ({index['processingProgress']}%)")
        return None

# Poll for indexing completion
while True:
    result = get_video_index(video_id)
    if result:
        break
    time.sleep(10)

# Extract insights
print("\nTranscript:")
for transcript in result["videos"][0]["insights"]["transcript"]:
    print(f"  {transcript['text']}")

print("\nKeywords:")
for keyword in result["videos"][0]["insights"]["keywords"]:
    print(f"  {keyword['text']} (confidence: {keyword['confidence']})")

print("\nSentiments:")
for sentiment in result["videos"][0]["insights"]["sentiments"]:
    print(f"  {sentiment['sentimentType']}: {sentiment['sentimentKey']}")

print("\nFaces detected:")
for face in result["videos"][0]["insights"]["faces"]:
    print(f"  Face ID: {face['id']}, Confidence: {face['confidence']}")
```

#### REST API Example

```bash
# Upload video
curl -X POST \
  "https://api.videoindexer.ai/YOUR_LOCATION/Accounts/YOUR_ACCOUNT_ID/Videos?accessToken=YOUR_TOKEN&name=sample" \
  -F "file=@video.mp4"

# Get video index
curl -X GET \
  "https://api.videoindexer.ai/YOUR_LOCATION/Accounts/YOUR_ACCOUNT_ID/Videos/VIDEO_ID/Index?accessToken=YOUR_TOKEN"

# Get video insights
curl -X GET \
  "https://api.videoindexer.ai/YOUR_LOCATION/Accounts/YOUR_ACCOUNT_ID/Videos/VIDEO_ID/Insights?accessToken=YOUR_TOKEN&language=en-US"
```

**Response (Simplified):**
```json
{
  "id": "video_id",
  "state": "Processed",
  "processingProgress": 100,
  "videos": [
    {
      "id": "video_id",
      "insights": {
        "transcript": [
          {
            "id": 1,
            "text": "Hello world",
            "confidence": 0.95,
            "speakerId": 1,
            "language": "en-US"
          }
        ],
        "keywords": [
          {
            "text": "cloud computing",
            "confidence": 0.87
          }
        ],
        "sentiments": [
          {
            "sentimentType": "Positive",
            "sentimentKey": "welcome"
          }
        ],
        "faces": [
          {
            "id": 1,
            "name": "Person Name",
            "confidence": 0.92
          }
        ]
      }
    }
  ]
}
```

---

## Azure AI Search

### 1. Azure AI Search (Cognitive Search)

**Service Description:**
Azure AI Search provides cloud search with AI capabilities for intelligent indexing and querying across structured and unstructured data.

**Key Features:**
- Full-text search with relevance tuning
- Vector search with semantic ranking
- Hybrid search combining keyword and vector approaches
- AI enrichment pipelines
- Faceted navigation
- Custom scoring profiles

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Maximum Indexes** | Unlimited (based on storage quota) |
| **Maximum Fields per Index** | 1,000 fields |
| **Field Name Length** | 128 characters max |
| **Index Size** | No specific limit (based on pricing tier) |
| **Documents per Index** | Unlimited |
| **Max Document Size** | 16 MB |
| **Batch Size (Upload)** | 1,000 documents per batch |
| **Requests per Second (Free Tier)** | 3 RPS |
| **Requests per Second (S1)** | 15 RPS |
| **Requests per Second (S2)** | 60 RPS |
| **Requests per Second (S3/S3HD)** | 200+ RPS |
| **Vector Dimensions** | Up to 3,072 dimensions |
| **Vector Search Algorithms** | HNSW, Exhaustive KNN |
| **Semantic Search Capacity** | 2-5 instances (tier dependent) |
| **Indexer Execution Timeout** | 24 hours |
| **Query Response Time** | <100 ms (typical) |
| **Facet Query Limit** | 10 faceted fields per query |
| **Filter Expression Complexity** | Up to 64 nested conditions |
| **Skillsets per Service** | Unlimited |
| **API Key Management** | Admin keys (full access) + Query keys (read-only) |

#### Azure CLI Command

```bash
# Create Azure AI Search service (Basic tier)
az search service create \
  --name myaisearch \
  --resource-group myResourceGroup \
  --sku basic \
  --location eastus

# Create with Standard tier
az search service create \
  --name myaisearchstandard \
  --resource-group myResourceGroup \
  --sku standard \
  --location eastus \
  --partition-count 1 \
  --replica-count 1

# Get admin key
az search admin-key show \
  --resource-group myResourceGroup \
  --service-name myaisearch

# Get query key
az search query-key list \
  --resource-group myResourceGroup \
  --service-name myaisearch

# Create query key
az search query-key create \
  --resource-group myResourceGroup \
  --service-name myaisearch \
  --name my-query-key

# Show service details
az search service show \
  --resource-group myResourceGroup \
  --name myaisearch

# Scale up service
az search service update \
  --resource-group myResourceGroup \
  --name myaisearch \
  --partition-count 2 \
  --replica-count 2
```

#### Python Code Example

```python
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import *
from azure.core.credentials import AzureKeyCredential

service_name = "YOUR_SERVICE_NAME"
admin_key = "YOUR_ADMIN_KEY"
endpoint = f"https://{service_name}.search.windows.net/"

# Create index
index_client = SearchIndexClient(endpoint=endpoint, credential=AzureKeyCredential(admin_key))

fields = [
    SimpleField(name="id", type=SearchFieldDataType.String, key=True),
    SearchableField(name="title", type=SearchFieldDataType.String, analyzer_name="en.microsoft"),
    SearchableField(name="content", type=SearchFieldDataType.String, analyzer_name="en.microsoft"),
    SimpleField(name="category", type=SearchFieldDataType.String, facetable=True),
    SimpleField(name="tags", type=SearchFieldDataType.Collection(SearchFieldDataType.String), facetable=True),
    SearchField(
        name="embedding",
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
        searchable=True,
        vector_search_dimensions=1536,
        vector_search_profile_name="myHnswProfile"
    )
]

vector_search_config = VectorSearch(
    algorithms=[HnswAlgorithmConfiguration(name="myHnsw")],
    profiles=[VectorSearchProfile(name="myHnswProfile", algorithm_configuration_name="myHnsw")]
)

index = SearchIndex(
    name="my-index",
    fields=fields,
    vector_search=vector_search_config
)

result = index_client.create_index(index)
print(f"Index '{result.name}' created")

# Index documents
search_client = SearchClient(endpoint=endpoint, index_name="my-index", credential=AzureKeyCredential(admin_key))

documents = [
    {
        "id": "1",
        "title": "Azure Search Documentation",
        "content": "Learn how to use Azure Search for full-text search",
        "category": "Documentation",
        "tags": ["azure", "search", "documentation"]
    },
    {
        "id": "2",
        "title": "Python SDK Tutorial",
        "content": "Guide for using Python SDK with Azure Search",
        "category": "Tutorial",
        "tags": ["python", "sdk", "tutorial"]
    }
]

result = search_client.upload_documents(documents=documents)
print(f"{len(result)} documents uploaded")

# Search documents
search_results = search_client.search(
    search_text="Azure Search",
    select=["id", "title", "content"],
    top=10
)

print("\nSearch Results:")
for result in search_results:
    print(f"  Title: {result['title']}")
    print(f"  Score: {result['@search.score']}")

# Faceted search
results = search_client.search(
    search_text="*",
    facets=["category", "tags", "sentiment"],
    top=0
)

facets = results.get_facets()
print(f"\nCategory facets: {facets['category']}")
print(f"Tag facets: {facets['tags']}")
print(f"Sentiment facets: {facets['sentiment']}")

# Vector search
import numpy as np

# Simulate embedding (in real scenario, use a model to generate embeddings)
query_vector = np.random.rand(1536).tolist()

results = search_client.search(
    search_text=None,
    vector_queries=[
        RawVectorQuery(vector=query_vector, k=10, fields="embedding")
    ],
    select=["id", "title"]
)

print("\nVector Search Results:")
for result in results:
    print(f"  Title: {result['title']}")
    print(f"  Score: {result['@search.score']}")

# Search with enriched fields
enriched_results = search_client.search(
    search_text="machine learning",
    filter="sentiment eq 'positive' and language eq 'en'",
    select=["id", "title", "content", "sentiment", "entities", "keyPhrases"],
    top=10
)

print("\nEnriched Search Results:")
for result in enriched_results:
    print(f"  Title: {result['title']}")
    print(f"  Sentiment: {result.get('sentiment', 'N/A')}")
    print(f"  Entities: {result.get('entities', [])}")
    print(f"  Key Phrases: {result.get('keyPhrases', [])}")
```

#### REST API Example

```bash
# Create or update index
curl -X PUT \
  "https://YOUR_SERVICE_NAME.search.windows.net/indexes/my-index?api-version=2024-05-01-preview" \
  -H "api-key: YOUR_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-index",
    "fields": [
      {"name": "id", "type": "Edm.String", "key": true},
      {"name": "title", "type": "Edm.String", "searchable": true},
      {"name": "content", "type": "Edm.String", "searchable": true},
      {"name": "category", "type": "Edm.String", "filterable": true, "facetable": true}
    ]
  }'

# Index documents
curl -X POST \
  "https://YOUR_SERVICE_NAME.search.windows.net/indexes/my-index/docs/index?api-version=2024-05-01-preview" \
  -H "api-key: YOUR_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "value": [
      {
        "@search.action": "upload",
        "id": "1",
        "title": "Document Title",
        "content": "Document content",
        "category": "Category"
      }
    ]
  }'

# Search documents
curl -X GET \
  "https://YOUR_SERVICE_NAME.search.windows.net/indexes/my-index/docs/search?api-version=2024-05-01-preview&search=Azure+Search&select=id,title&top=10" \
  -H "api-key: YOUR_QUERY_KEY"
```

---

### 2. Azure AI Search - Field Enrichment Schema

**Field Enrichment** enables AI-powered extraction of additional metadata and structured information during document indexing using cognitive skills.

#### Enrichment Architecture

```json
{
  "name": "my-enrichment-pipeline",
  "description": "Pipeline for text enrichment using cognitive skills",
  "skills": [],
  "outputs": [],
  "cognitiveServices": {
    "description": "Cognitive Services multi-service resource",
    "@odata.type": "#Microsoft.Azure.Search.CognitiveServicesByKey",
    "key": "YOUR_COGNITIVE_SERVICES_KEY"
  }
}
```

#### Enrichment Field Schema Definitions

**Text Analysis Enrichment Fields:**

| Field Name | Data Type | Source Skill | Description | Example |
|------------|-----------|--------------|-------------|---------|
| sentiment | Edm.String | Sentiment | Overall sentiment (positive/negative/neutral) | "positive" |
| sentimentScore | Edm.Double | Sentiment | Sentiment confidence score (0-1) | 0.92 |
| keyPhrases | Collection(Edm.String) | Key Phrase | Extracted important phrases | ["Azure Search", "AI enrichment"] |
| entities | Collection(Edm.String) | Named Entity | Recognized named entities | ["Microsoft", "Azure"] |
| entityCategories | Collection(Edm.String) | Named Entity | Entity categories | ["Organization", "Location"] |
| language | Edm.String | Language Detection | Detected language code | "en" |
| languageConfidence | Edm.Double | Language Detection | Language detection confidence | 0.98 |

**Image Analysis Enrichment Fields:**

| Field Name | Data Type | Source Skill | Description | Example |
|------------|-----------|--------------|-------------|---------|
| imageTags | Collection(Edm.String) | Image Analysis | Auto-generated tags | ["outdoor", "nature", "mountain"] |
| imageCaption | Edm.String | Image Analysis | Generated image description | "A mountain landscape at sunset" |
| imageObjects | Collection(Edm.ComplexType) | Object Detection | Detected objects with bounding boxes | [{"name": "tree", "confidence": 0.95}] |
| imageFaces | Collection(Edm.ComplexType) | Face Detection | Detected faces with attributes | [{"age": 32, "gender": "male"}] |
| imageColors | Collection(Edm.String) | Color Analysis | Dominant colors | ["blue", "green", "brown"] |

**Document Processing Enrichment Fields:**

| Field Name | Data Type | Source Skill | Description | Example |
|------------|-----------|--------------|-------------|---------|
| ocrText | Edm.String | OCR | Extracted text from images | "Invoice #12345" |
| tables | Collection(Edm.ComplexType) | Table Recognition | Extracted table structure | [{"rows": 5, "cols": 4}] |
| metadata_storage_path | Edm.String | Built-in | Document source path | "https://storage.blob.core.windows.net/..." |
| metadata_storage_name | Edm.String | Built-in | Document filename | "invoice.pdf" |
| normalized_images | Collection(Edm.ComplexType) | Image Normalization | Normalized image metadata | [{"width": 1024, "height": 768}] |

**Semantic Enrichment Fields:**

| Field Name | Data Type | Source Skill | Description | Example |
|------------|-----------|--------------|-------------|---------|
| semanticSummary | Edm.String | Summarization | AI-generated summary | "Document discusses AI trends..." |
| translatedText | Edm.String | Translation | Translated content | "Esto es una traducción" |
| mergedText | Edm.String | Text Merge | Combined enriched text | Merged from multiple sources |
| customEntities | Collection(Edm.String) | Custom Entity | Domain-specific entities | ["CPaaS", "SaaS", "PaaS"] |

#### Skillset Definition Example

```python
from azure.search.documents.indexes.models import (
    SearchIndexerSkillset,
    InputFieldMappingEntry,
    OutputFieldMappingEntry,
    EntityRecognitionSkill,
    KeyPhraseExtractionSkill,
    SentimentSkill,
    LanguageDetectionSkill,
    ImageAnalysisSkill,
    OcrSkill,
    MergeSkill
)

# Define skillset with multiple enrichment skills
skillset = SearchIndexerSkillset(
    name="enrichment-skillset",
    description="Skillset for AI enrichment of documents",
    skills=[
        # Language Detection
        LanguageDetectionSkill(
            inputs=[InputFieldMappingEntry(name="text", source="/document/content")],
            outputs=[OutputFieldMappingEntry(name="languageCode", target_name="language")],
            context="/document"
        ),
        # Named Entity Recognition
        EntityRecognitionSkill(
            inputs=[InputFieldMappingEntry(name="text", source="/document/content")],
            outputs=[
                OutputFieldMappingEntry(name="entities", target_name="entities"),
                OutputFieldMappingEntry(name="persons", target_name="persons")
            ],
            context="/document",
            model_version="latest"
        ),
        # Key Phrase Extraction
        KeyPhraseExtractionSkill(
            inputs=[InputFieldMappingEntry(name="text", source="/document/content")],
            outputs=[OutputFieldMappingEntry(name="keyPhrases", target_name="keyPhrases")],
            context="/document",
            max_key_phrase_count=10
        ),
        # Sentiment Analysis
        SentimentSkill(
            inputs=[InputFieldMappingEntry(name="text", source="/document/content")],
            outputs=[
                OutputFieldMappingEntry(name="sentiment", target_name="sentiment"),
                OutputFieldMappingEntry(name="confidenceScores", target_name="sentimentScore")
            ],
            context="/document"
        ),
        # Image Analysis (if processing images)
        ImageAnalysisSkill(
            inputs=[InputFieldMappingEntry(name="image_data", source="/document/normalized_images/*")],
            outputs=[
                OutputFieldMappingEntry(name="tags", target_name="imageTags"),
                OutputFieldMappingEntry(name="description", target_name="imageCaption")
            ],
            context="/document/normalized_images/*",
            visual_features=["tags", "description", "faces"]
        ),
        # Merge enriched fields
        MergeSkill(
            inputs=[
                InputFieldMappingEntry(name="text", source="/document/content"),
                InputFieldMappingEntry(name="itemsToInsert", source="/document/keyPhrases/*")
            ],
            outputs=[OutputFieldMappingEntry(name="mergedText", target_name="mergedText")],
            context="/document",
            insert_at_end=True
        )
    ]
)
```

#### Index Definition with Enriched Fields

```python
index = SearchIndex(
    name="enriched-documents",
    fields=[
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="title", type=SearchFieldDataType.String),
        SearchableField(name="content", type=SearchFieldDataType.String),
        
        # Enriched fields
        SimpleField(name="language", type=SearchFieldDataType.String, facetable=True),
        SearchableField(name="entities", type=SearchFieldDataType.Collection(SearchFieldDataType.String), facetable=True),
        SearchableField(name="persons", type=SearchFieldDataType.Collection(SearchFieldDataType.String)),
        SearchableField(name="keyPhrases", type=SearchFieldDataType.Collection(SearchFieldDataType.String), facetable=True),
        SimpleField(name="sentiment", type=SearchFieldDataType.String, facetable=True),
        SimpleField(name="sentimentScore", type=SearchFieldDataType.Double),
        SearchableField(name="imageTags", type=SearchFieldDataType.Collection(SearchFieldDataType.String)),
        SearchableField(name="imageCaption", type=SearchFieldDataType.String),
        
        # Metadata
        SimpleField(name="metadata_storage_path", type=SearchFieldDataType.String),
        SimpleField(name="metadata_storage_name", type=SearchFieldDataType.String),
        SimpleField(name="processed_date", type=SearchFieldDataType.DateTimeOffset)
    ]
)
```

#### Indexer with Field Mappings

```python
from azure.search.documents.indexes.models import SearchIndexer, FieldMapping
from datetime import timedelta

indexer = SearchIndexer(
    name="my-indexer",
    data_source_name="my-data-source",
    target_index_name="enriched-documents",
    skillset_name="enrichment-skillset",
    
    # Field mappings from source to index
    field_mappings=[
        FieldMapping(source_field_name="id", target_field_name="id"),
        FieldMapping(source_field_name="title", target_field_name="title"),
        FieldMapping(source_field_name="body_content", target_field_name="content")
    ],
    
    # Output field mappings from enrichment skills
    output_field_mappings=[
        FieldMapping(source_field_name="/document/language", target_field_name="language"),
        FieldMapping(source_field_name="/document/sentiment", target_field_name="sentiment"),
        FieldMapping(source_field_name="/document/sentimentScore", target_field_name="sentimentScore"),
        FieldMapping(source_field_name="/document/entities", target_field_name="entities"),
        FieldMapping(source_field_name="/document/persons", target_field_name="persons"),
        FieldMapping(source_field_name="/document/keyPhrases", target_field_name="keyPhrases"),
        FieldMapping(source_field_name="/document/imageTags", target_field_name="imageTags"),
        FieldMapping(source_field_name="/document/imageCaption", target_field_name="imageCaption")
    ],
    
    schedule=SearchIndexingSchedule(interval=timedelta(days=1)),
    parameters=SearchIndexerParameters(
        batch_size=100,
        max_failed_items_per_batch=5,
        configuration=SearchIndexerConfiguration(index_content_deletion_detection_policy=None)
    )
)
```

#### Sample Enriched Document Structure

```json
{
  "id": "doc-001",
  "title": "Azure Search Implementation Guide",
  "content": "Azure Search provides powerful full-text search capabilities...",
  "language": "en",
  "sentiment": "positive",
  "sentimentScore": 0.87,
  "entities": ["Azure", "Microsoft", "Search"],
  "persons": ["John Smith"],
  "keyPhrases": ["full-text search", "AI capabilities", "cognitive skills"],
  "imageTags": ["technology", "cloud", "data"],
  "imageCaption": "Cloud infrastructure and data processing",
  "metadata_storage_path": "https://storage.blob.core.windows.net/docs/guide.pdf",
  "metadata_storage_name": "guide.pdf",
  "processed_date": "2024-01-20T10:30:00Z",
  "@search.score": 2.5
}
```

#### Enrichment Best Practices

1. **Skill Ordering**: Place language detection first to support language-specific skills
2. **Conditional Enrichment**: Use conditions to enrich only relevant fields
3. **Performance**: Use batching and async operations for large documents
4. **Cost Management**: Only enable skills you need to minimize API calls
5. **Error Handling**: Configure max_failed_items to handle skill failures gracefully
6. **Debugging**: Use "@search.highlight" to verify extraction accuracy
7. **Field Mapping**: Map enriched fields to filterable/facetable fields for better search experience

#### REST API - Skillset and Indexer Creation

```bash
# Create skillset
curl -X PUT \
  "https://YOUR_SERVICE_NAME.search.windows.net/skillsets/enrichment-skillset?api-version=2024-05-01-preview" \
  -H "api-key: YOUR_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "enrichment-skillset",
    "description": "Skillset for document enrichment",
    "skills": [
      {
        "@odata.type": "#Microsoft.Skills.Text.LanguageDetectionSkill",
        "inputs": [
          {"name": "text", "source": "/document/content"}
        ],
        "outputs": [
          {"name": "languageCode", "targetName": "language"}
        ]
      },
      {
        "@odata.type": "#Microsoft.Skills.Text.SentimentSkill",
        "inputs": [
          {"name": "text", "source": "/document/content"}
        ],
        "outputs": [
          {"name": "sentiment", "targetName": "sentiment"},
          {"name": "confidenceScores", "targetName": "sentimentScore"}
        ]
      },
      {
        "@odata.type": "#Microsoft.Skills.Text.KeyPhraseExtractionSkill",
        "inputs": [
          {"name": "text", "source": "/document/content"}
        ],
        "outputs": [
          {"name": "keyPhrases", "targetName": "keyPhrases"}
        ]
      }
    ]
  }'

# Create indexer
curl -X PUT \
  "https://YOUR_SERVICE_NAME.search.windows.net/indexers/my-indexer?api-version=2024-05-01-preview" \
  -H "api-key: YOUR_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-indexer",
    "dataSourceName": "my-data-source",
    "targetIndexName": "enriched-documents",
    "skillsetName": "enrichment-skillset",
    "fieldMappings": [
      {"sourceFieldName": "id", "targetFieldName": "id"},
      {"sourceFieldName": "title", "targetFieldName": "title"}
    ],
    "outputFieldMappings": [
      {"sourceFieldName": "/document/language", "targetFieldName": "language"},
      {"sourceFieldName": "/document/sentiment", "targetFieldName": "sentiment"},
      {"sourceFieldName": "/document/keyPhrases", "targetFieldName": "keyPhrases"}
    ]
  }'
```

---**Response:**
```json
{
  "@odata.context": "https://YOUR_SERVICE_NAME.search.windows.net/indexes('my-index')/$metadata#docs(*)",
  "value": [
    {
      "@search.score": 2.5164525,
      "id": "1",
      "title": "Azure Search Documentation"
    }
  ]
}
```

---

## Azure AI Foundry

### 1. Azure AI Foundry - Chat Models and Agent-to-Agent Communication

**Service Description:**
Azure AI Foundry provides a unified platform for building, deploying, and managing AI applications including chat models, agents, and multi-agent orchestration with agent-to-agent communication.

**Key Features:**
- Large Language Model (LLM) hosting and inference
- Chat completions API
- Agent framework for autonomous agents
- Multi-agent orchestration and coordination
- Agent-to-agent communication and collaboration
- Function calling and tool integration
- Semantic kernel integration
- Model deployment and versioning
- Content safety and responsible AI

**Service Limitations:**

| Limitation | Details |
|-----------|---------|
| **Max Context Window** | 128k tokens (varies by model) |
| **Max Output Tokens** | 4k tokens per completion |
| **Rate Limits (Free)** | 10 calls/min, 6 calls/minute per deployment |
| **Rate Limits (Standard)** | 100 calls/min, 30 calls/minute per deployment |
| **Supported Models** | GPT-4, GPT-4 Turbo, GPT-3.5-turbo, Mistral, Llama |
| **Agents per Project** | Unlimited |
| **Agent Memory** | Up to 1 GB for conversational history |
| **Concurrent Agents** | 1000+ with proper resource allocation |
| **Function Calls per Request** | Up to 10 parallel function calls |
| **Tool Integration** | 50+ built-in tools, custom tools via plugins |
| **Model Fine-tuning** | GPT-3.5-turbo, Llama 2 supported |
| **Deployment Regions** | 20+ regions globally |
| **Token Pricing** | Per 1k tokens (input/output) |
| **API Version** | 2024-05-01-preview and later |

#### Azure CLI Command

```bash
# Create AI Foundry Hub
az ai hub create \
  --name myAIHub \
  --resource-group myResourceGroup \
  --location eastus

# Create AI Project
az ai project create \
  --name myAIProject \
  --hub-name myAIHub \
  --resource-group myResourceGroup

# Deploy model
az ai model deploy \
  --name gpt-4 \
  --version 1.0 \
  --project myAIProject \
  --hub-name myAIHub \
  --resource-group myResourceGroup

# Get deployment endpoints
az ai model deployment list \
  --project myAIProject \
  --hub-name myAIHub \
  --resource-group myResourceGroup
```

#### Python Code Example - Chat Models

```python
from azure.ai.generative.models import ChatCompletionClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI

# Initialize client
client = AzureOpenAI(
    api_key="YOUR_API_KEY",
    api_version="2024-05-01-preview",
    azure_endpoint="YOUR_ENDPOINT"
)

# Simple chat completion
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant specializing in Azure services."
        },
        {
            "role": "user",
            "content": "Explain Azure AI Foundry in 3 sentences."
        }
    ],
    temperature=0.7,
    max_tokens=500
)

print("Assistant:", response.choices[0].message.content)

# Chat with function calling
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "What's the weather in Seattle today?"
        }
    ],
    tools=tools,
    tool_choice="auto"
)

# Handle tool calls
if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        print(f"Function: {tool_call.function.name}")
        print(f"Arguments: {tool_call.function.arguments}")
```

#### Python Code Example - Agent Framework

```python
from semantic_kernel import Kernel
from semantic_kernel.agents import AgentGroupChat, ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.functions.kernel_function_decorator import kernel_function

# Create kernel
kernel = Kernel()

# Add Azure OpenAI service
service = AzureChatCompletion(
    deployment_name="gpt-4",
    endpoint="YOUR_ENDPOINT",
    api_key="YOUR_API_KEY"
)
kernel.add_service(service)

# Define agent with tools
class WeatherAgent:
    @kernel_function(description="Get current weather")
    def get_weather(self, location: str) -> str:
        return f"Weather in {location}: Sunny, 72°F"

# Create agents
weather_agent = ChatCompletionAgent(
    kernel=kernel,
    name="WeatherAgent",
    instructions="You are a weather expert. Answer questions about weather.",
    service_id="default"
)

assistant_agent = ChatCompletionAgent(
    kernel=kernel,
    name="AssistantAgent",
    instructions="You are a helpful AI assistant.",
    service_id="default"
)

# Agent-to-agent communication
chat = AgentGroupChat(agents=[weather_agent, assistant_agent])

# Start conversation
response = await chat.invoke(
    input="What's the weather in Seattle?"
)

print(response)

# Multi-agent orchestration
class TaskOrchestrator:
    async def execute_task(self, task: str):
        # Route task to appropriate agent
        if "weather" in task.lower():
            agent = weather_agent
        else:
            agent = assistant_agent
        
        result = await agent.invoke(task)
        return result

orchestrator = TaskOrchestrator()
result = await orchestrator.execute_task("Tell me about weather patterns")
```

#### Agent-to-Agent Communication Schema

```json
{
  "agent": {
    "id": "weather-agent-001",
    "name": "WeatherAgent",
    "role": "Weather Information Provider",
    "capabilities": ["weather_lookup", "forecast_generation"]
  },
  "communication": {
    "protocol": "REST API or DirectCommunication",
    "format": "JSON",
    "message": {
      "type": "REQUEST|RESPONSE|NOTIFICATION",
      "sender_id": "assistant-agent-001",
      "receiver_id": "weather-agent-001",
      "action": "get_weather",
      "parameters": {
        "location": "Seattle",
        "days": 5
      },
      "correlation_id": "corr-12345",
      "timestamp": "2024-01-20T10:30:00Z"
    },
    "response": {
      "status": "success",
      "data": {
        "location": "Seattle",
        "current": {
          "temperature": 72,
          "condition": "Sunny",
          "humidity": 65
        },
        "forecast": [
          {
            "date": "2024-01-21",
            "high": 75,
            "low": 62,
            "condition": "Cloudy"
          }
        ]
      },
      "metadata": {
        "execution_time_ms": 245,
        "confidence": 0.95
      }
    }
  }
}
```

#### REST API Example

```bash
# Chat completion
curl -X POST \
  "YOUR_ENDPOINT/openai/deployments/gpt-4/chat/completions?api-version=2024-05-01-preview" \
  -H "api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful AI assistant."
      },
      {
        "role": "user",
        "content": "Explain Azure AI Foundry."
      }
    ],
    "temperature": 0.7,
    "max_tokens": 500
  }'

# Function calling
curl -X POST \
  "YOUR_ENDPOINT/openai/deployments/gpt-4/chat/completions?api-version=2024-05-01-preview" \
  -H "api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the weather in Seattle?"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "Get weather for a location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {"type": "string"}
            },
            "required": ["location"]
          }
        }
      }
    ]
  }'

# Agent health check
curl -X GET \
  "YOUR_ENDPOINT/agents/agent-001/health" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

#### ARM Template for AI Foundry Hub

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "aiHubName": {
      "type": "string",
      "defaultValue": "myAIHub",
      "metadata": {"description": "Name of AI Foundry Hub"}
    },
    "location": {
      "type": "string",
      "defaultValue": "eastus",
      "metadata": {"description": "Location for resources"}
    }
  },
  "resources": [
    {
      "type": "Microsoft.MachineLearningServices/workspaces",
      "apiVersion": "2024-01-01-preview",
      "name": "[parameters('aiHubName')]",
      "location": "[parameters('location')]",
      "kind": "Hub",
      "properties": {
        "displayName": "[parameters('aiHubName')]",
        "description": "AI Foundry Hub for chat and agents",
        "allowPublicAccessWhenBehindVnet": false
      }
    }
  ],
  "outputs": {
    "hubId": {
      "type": "string",
      "value": "[resourceId('Microsoft.MachineLearningServices/workspaces', parameters('aiHubName'))]"
    }
  }
}
```

#### Bicep Template for AI Foundry

```bicep
param aiHubName string = 'myAIHub'
param location string = 'eastus'
param environment string = 'production'

resource aiHub 'Microsoft.MachineLearningServices/workspaces@2024-01-01-preview' = {
  name: aiHubName
  location: location
  kind: 'Hub'
  properties: {
    displayName: aiHubName
    description: 'AI Foundry Hub with chat and agent capabilities'
    tags: {
      environment: environment
      purpose: 'ai-agents'
    }
    allowPublicAccessWhenBehindVnet: false
  }
}

resource aiProject 'Microsoft.MachineLearningServices/workspaces@2024-01-01-preview' = {
  name: '${aiHubName}-project'
  location: location
  kind: 'Project'
  properties: {
    displayName: '${aiHubName}-project'
    hubResourceId: aiHub.id
  }
  dependsOn: [aiHub]
}

output hubResourceId string = aiHub.id
output projectResourceId string = aiProject.id
```

---

## Model Context Protocol (MCP)

### 1. MCP Communication and Integration

**Service Description:**
Model Context Protocol (MCP) is a standardized protocol for AI models to communicate with external systems, tools, and services. It enables secure, typed communication between language models and applications.

**Key Features:**
- Standardized message protocol for AI-tool communication
- Bidirectional request/response pattern
- Resource discovery and management
- Prompt and tool definition
- Error handling and validation
- Transport layer abstraction
- Server and client architecture

**Implementation Requirements:**

| Component | Details |
|-----------|---------|
| **MCP Server** | Exposes tools and resources to clients |
| **MCP Client** | Requests tools and resources from servers |
| **Message Format** | JSON-RPC 2.0 |
| **Transport** | stdio, HTTP, WebSocket, custom |
| **Authentication** | API keys, OAuth, custom tokens |
| **Error Handling** | Standard JSON-RPC error codes |
| **Supported Languages** | Python, TypeScript, Go, Rust, etc. |
| **Schema Validation** | JSON Schema for requests/responses |

#### Python Code Example - MCP Server

```python
from mcp.server import Server
from mcp.types import Tool, TextContent, ToolInput
import json

class MCPServer:
    def __init__(self):
        self.server = Server("weather-mcp-server")
        self.setup_tools()
    
    def setup_tools(self):
        # Define available tools
        weather_tool = Tool(
            name="get_weather",
            description="Get current weather for a location",
            inputSchema={
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature unit"
                    }
                },
                "required": ["location"]
            }
        )
        
        self.server.register_tool(weather_tool, self.handle_weather)
    
    def handle_weather(self, tool_input: ToolInput) -> TextContent:
        location = tool_input.arguments.get("location")
        unit = tool_input.arguments.get("unit", "fahrenheit")
        
        # Simulate weather data
        weather_data = {
            "location": location,
            "temperature": 72,
            "unit": unit,
            "condition": "Sunny",
            "humidity": 65,
            "windSpeed": 10
        }
        
        return TextContent(
            type="text",
            text=json.dumps(weather_data, indent=2)
        )
    
    async def run(self):
        await self.server.start()

# Run server
if __name__ == "__main__":
    server = MCPServer()
    import asyncio
    asyncio.run(server.run())
```

#### Python Code Example - MCP Client

```python
from mcp.client import Client
from mcp.types import CallToolRequest
import json

class MCPClient:
    def __init__(self, server_endpoint: str):
        self.client = Client("chat-client")
        self.server_endpoint = server_endpoint
    
    async def connect(self):
        await self.client.connect(self.server_endpoint)
    
    async def call_tool(self, tool_name: str, arguments: dict):
        """Call a tool on the MCP server"""
        request = CallToolRequest(
            name=tool_name,
            arguments=arguments
        )
        
        response = await self.client.call_tool(request)
        return response
    
    async def list_tools(self):
        """List available tools from MCP server"""
        tools = await self.client.list_tools()
        return tools
    
    async def example_workflow(self):
        # Connect to server
        await self.connect()
        
        # List available tools
        tools = await self.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")
        
        # Call weather tool
        result = await self.call_tool("get_weather", {
            "location": "Seattle",
            "unit": "fahrenheit"
        })
        
        print(f"Weather data: {result.content}")

# Usage
if __name__ == "__main__":
    client = MCPClient("http://localhost:8000")
    import asyncio
    asyncio.run(client.example_workflow())
```

#### MCP Protocol Message Schema

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "Seattle",
      "unit": "fahrenheit"
    }
  },
  "id": 1
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "result": {
    "type": "text",
    "text": "{\"location\": \"Seattle\", \"temperature\": 72, \"condition\": \"Sunny\"}"
  },
  "id": 1
}
```

#### REST API Example - MCP Integration

```bash
# Connect to MCP server
curl -X POST \
  "http://YOUR_SERVER:8000/mcp/connect" \
  -H "Content-Type: application/json" \
  -d '{
    "serverAddress": "http://weather-service:8000",
    "authentication": {
      "type": "api_key",
      "token": "YOUR_MCP_TOKEN"
    }
  }'

# List available tools
curl -X GET \
  "http://YOUR_SERVER:8000/mcp/tools" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Call MCP tool
curl -X POST \
  "http://YOUR_SERVER:8000/mcp/tools/call" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "toolName": "get_weather",
    "arguments": {
      "location": "Seattle"
    }
  }'
```

---

## Code Interceptor

### 1. Code Interceptor for Request/Response Monitoring

**Service Description:**
Code Interceptor is an Azure feature for intercepting, logging, and transforming API requests and responses in real-time for debugging, monitoring, and compliance purposes.

**Key Features:**
- Request/response interception
- Content transformation and filtering
- Request/response logging
- Performance monitoring
- Security policy enforcement
- Error tracking and analysis
- Custom middleware support
- Header and body manipulation

#### Python Code Example - Code Interceptor Middleware

```python
from typing import Callable, Any
import json
import logging
from datetime import datetime
import hashlib

class CodeInterceptor:
    def __init__(self, log_sensitive_data: bool = False):
        self.logger = logging.getLogger(__name__)
        self.log_sensitive_data = log_sensitive_data
        self.request_history = []
        self.response_history = []
    
    def log_request(self, method: str, url: str, headers: dict, body: Any = None) -> str:
        """Intercept and log incoming request"""
        request_id = hashlib.md5(
            f"{datetime.now().isoformat()}".encode()
        ).hexdigest()[:8]
        
        request_log = {
            "request_id": request_id,
            "timestamp": datetime.now().isoformat(),
            "method": method,
            "url": url,
            "headers": self._filter_headers(headers),
            "body_size": len(json.dumps(body)) if body else 0
        }
        
        if self.log_sensitive_data and body:
            request_log["body"] = body
        
        self.request_history.append(request_log)
        self.logger.info(f"Request: {json.dumps(request_log)}")
        
        return request_id
    
    def log_response(self, request_id: str, status_code: int, headers: dict, 
                     body: Any = None, latency_ms: float = 0) -> None:
        """Intercept and log outgoing response"""
        response_log = {
            "request_id": request_id,
            "timestamp": datetime.now().isoformat(),
            "status_code": status_code,
            "headers": self._filter_headers(headers),
            "latency_ms": latency_ms,
            "body_size": len(json.dumps(body)) if body else 0
        }
        
        if self.log_sensitive_data and body:
            response_log["body"] = body
        
        self.response_history.append(response_log)
        self.logger.info(f"Response: {json.dumps(response_log)}")
    
    def intercept_request(self, func: Callable) -> Callable:
        """Decorator for request interception"""
        async def wrapper(*args, **kwargs):
            method = kwargs.get("method", "GET")
            url = kwargs.get("url", "")
            headers = kwargs.get("headers", {})
            body = kwargs.get("data", None)
            
            request_id = self.log_request(method, url, headers, body)
            
            # Modify request if needed
            kwargs["request_id"] = request_id
            
            return await func(*args, **kwargs)
        
        return wrapper
    
    def intercept_response(self, func: Callable) -> Callable:
        """Decorator for response interception"""
        async def wrapper(*args, request_id: str = None, **kwargs):
            start_time = datetime.now()
            
            # Execute original function
            response = await func(*args, **kwargs)
            
            latency = (datetime.now() - start_time).total_seconds() * 1000
            
            # Log response
            if response:
                self.log_response(
                    request_id or "unknown",
                    response.get("status_code", 200),
                    response.get("headers", {}),
                    response.get("body"),
                    latency
                )
            
            return response
        
        return wrapper
    
    def _filter_headers(self, headers: dict) -> dict:
        """Filter sensitive headers"""
        sensitive_headers = {
            "authorization", "api-key", "x-api-key",
            "password", "secret", "token", "bearer"
        }
        
        filtered = {}
        for key, value in headers.items():
            if key.lower() in sensitive_headers:
                filtered[key] = "***REDACTED***"
            else:
                filtered[key] = value
        
        return filtered
    
    def get_request_trace(self, request_id: str) -> dict:
        """Retrieve full request trace"""
        request = next(
            (r for r in self.request_history if r["request_id"] == request_id),
            None
        )
        response = next(
            (r for r in self.response_history if r["request_id"] == request_id),
            None
        )
        
        return {"request": request, "response": response}

# Usage example
interceptor = CodeInterceptor(log_sensitive_data=False)

@interceptor.intercept_request
async def send_request(method: str, url: str, headers: dict, data: Any = None, **kwargs):
    # Actual HTTP request logic
    return {"status": "sent"}

@interceptor.intercept_response
async def receive_response(status_code: int = 200, **kwargs):
    # Actual response handling
    return {
        "status_code": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": {"message": "Success"}
    }
```

#### Code Interceptor REST API Integration

```python
from azure.core.pipeline import Pipeline
from azure.core.pipeline.policies import HTTPLoggingPolicy

class AzureCodeInterceptor:
    def __init__(self, endpoint: str, api_key: str):
        self.endpoint = endpoint
        self.api_key = api_key
        self.interceptor = CodeInterceptor(log_sensitive_data=False)
    
    def create_pipeline_with_interception(self):
        """Create Azure SDK pipeline with code interception"""
        policies = [
            HTTPLoggingPolicy(
                allowed_header_names={"content-type", "accept"},
                logging_enable=True
            )
        ]
        
        pipeline = Pipeline(transport=None, policies=policies)
        return pipeline
    
    async def execute_with_interception(self, method: str, url: str, 
                                       headers: dict = None, body: Any = None):
        """Execute request with full interception"""
        headers = headers or {}
        headers["Authorization"] = f"Bearer {self.api_key}"
        
        # Log request
        request_id = self.interceptor.log_request(method, url, headers, body)
        
        # TODO: Execute actual HTTP request
        # response = await self.make_request(...)
        
        # Log response
        self.interceptor.log_response(
            request_id,
            status_code=200,
            headers={"Content-Type": "application/json"},
            body={"success": True},
            latency_ms=125
        )
        
        return self.interceptor.get_request_trace(request_id)
```

#### REST API Example - Code Interceptor

```bash
# Enable request/response interception
curl -X POST \
  "YOUR_ENDPOINT/interceptor/enable" \
  -H "api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "interceptionLevel": "FULL",
    "logSensitiveData": false,
    "transformations": [
      {
        "type": "HEADER_FILTER",
        "pattern": "Authorization|api-key",
        "action": "REDACT"
      }
    ]
  }'

# Get request trace
curl -X GET \
  "YOUR_ENDPOINT/interceptor/traces/{requestId}" \
  -H "api-key: YOUR_API_KEY"

# Response
{
  "requestId": "abc12345",
  "request": {
    "timestamp": "2024-01-20T10:30:00Z",
    "method": "POST",
    "url": "/api/chat/completions",
    "headers": {
      "Authorization": "***REDACTED***",
      "Content-Type": "application/json"
    }
  },
  "response": {
    "timestamp": "2024-01-20T10:30:00.245Z",
    "statusCode": 200,
    "latencyMs": 245,
    "headers": {
      "Content-Type": "application/json"
    }
  }
}
```

#### ARM Template for Code Interceptor Configuration

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "resources": [
    {
      "type": "Microsoft.ApiManagement/service/policies",
      "apiVersion": "2021-08-01",
      "name": "myApim/global",
      "properties": {
        "value": "<policies>\n<inbound>\n<log-to-eventhub logger-id=\"eventhub-logger\">\n@{\n  var requestBody = context.Request.Body?.As<string>(preserveContent: true);\n  return new JObject(\n    new JProperty(\"request-id\", context.RequestId),\n    new JProperty(\"timestamp\", DateTime.UtcNow),\n    new JProperty(\"method\", context.Request.Method),\n    new JProperty(\"url\", context.Request.Url.ToString()),\n    new JProperty(\"body\", requestBody)\n  ).ToString();\n}\n</log-to-eventhub>\n</inbound>\n</policies>"
      }
    }
  ]
}
```

#### Bicep Template for Code Interceptor

```bicep
param apiManagementName string = 'myApim'
param eventHubName string = 'interceptorHub'
param location string = 'eastus'

resource eventHub 'Microsoft.EventHub/namespaces/eventhubs@2021-11-01' = {
  name: '${apiManagementName}/${eventHubName}'
  location: location
  properties: {
    messageRetentionInDays: 7
    partitionCount: 2
  }
}

resource logger 'Microsoft.ApiManagement/service/loggers@2021-08-01' = {
  name: '${apiManagementName}/eventhub-logger'
  properties: {
    loggerType: 'eventhub'
    description: 'Event Hub logger for code interception'
    credentials: {
      name: eventHubName
      connectionString: 'YOUR_CONNECTION_STRING'
    }
    isBuffered: true
  }
}

output eventHubId string = eventHub.id
output loggerId string = logger.id
```

---

## Infrastructure as Code

### ARM Template Example

**Complete ARM Template for AI Services:**

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "projectName": {
      "type": "string",
      "metadata": {
        "description": "Name of the project"
      }
    },
    "location": {
      "type": "string",
      "defaultValue": "[resourceGroup().location]",
      "metadata": {
        "description": "Azure region for resources"
      }
    },
    "skuName": {
      "type": "string",
      "defaultValue": "S0",
      "allowedValues": ["S0", "S1", "S2"],
      "metadata": {
        "description": "SKU for cognitive services"
      }
    }
  },
  "variables": {
    "uniqueSuffix": "[uniqueString(resourceGroup().id)]",
    "cognitiveServicesAccountName": "[concat(parameters('projectName'), 'ai', variables('uniqueSuffix'))]",
    "searchServiceName": "[concat(parameters('projectName'), 'search', variables('uniqueSuffix'))]",
    "storageAccountName": "[concat(parameters('projectName'), 'storage', variables('uniqueSuffix'))]"
  },
  "resources": [
    {
      "type": "Microsoft.CognitiveServices/accounts",
      "apiVersion": "2021-10-01",
      "name": "[variables('cognitiveServicesAccountName')]",
      "location": "[parameters('location')]",
      "kind": "CognitiveServices",
      "sku": {
        "name": "[parameters('skuName')]"
      },
      "properties": {
        "apiProperties": {
          "statisticsEnabled": true
        }
      }
    },
    {
      "type": "Microsoft.Search/searchServices",
      "apiVersion": "2020-08-01",
      "name": "[variables('searchServiceName')]",
      "location": "[parameters('location')]",
      "sku": {
        "name": "basic"
      },
      "properties": {
        "replicaCount": 1,
        "partitionCount": 1,
        "hostingMode": "default"
      }
    },
    {
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2021-04-01",
      "name": "[variables('storageAccountName')]",
      "location": "[parameters('location')]",
      "kind": "StorageV2",
      "sku": {
        "name": "Standard_LRS"
      },
      "properties": {
        "accessTier": "Hot"
      }
    }
  ],
  "outputs": {
    "cognitiveServicesEndpoint": {
      "type": "string",
      "value": "[reference(resourceId('Microsoft.CognitiveServices/accounts', variables('cognitiveServicesAccountName')), '2021-10-01').endpoint]"
    },
    "searchServiceEndpoint": {
      "type": "string",
      "value": "[concat('https://', variables('searchServiceName'), '.search.windows.net')]"
    },
    "storageAccountName": {
      "type": "string",
      "value": "[variables('storageAccountName')]"
    }
  }
}
```

**Deployment:**
```bash
az deployment group create \
  --resource-group myResourceGroup \
  --template-file template.json \
  --parameters projectName=myproject location=eastus skuName=S0
```

---

### Bicep Template Example

**Complete Bicep Template for AI Services:**

```bicep
param projectName string
param location string = resourceGroup().location
@allowed([
  'S0'
  'S1'
  'S2'
])
param skuName string = 'S0'
param environment string = 'dev'

var uniqueSuffix = uniqueString(resourceGroup().id)
var cognitiveServicesAccountName = '${projectName}ai${uniqueSuffix}'
var searchServiceName = '${projectName}search${uniqueSuffix}'
var storageAccountName = '${projectName}storage${uniqueSuffix}'
var keyVaultName = '${projectName}kv${uniqueSuffix}'

// Cognitive Services Account
resource cognitiveServices 'Microsoft.CognitiveServices/accounts@2021-10-01' = {
  name: cognitiveServicesAccountName
  location: location
  kind: 'CognitiveServices'
  sku: {
    name: skuName
  }
  properties: {
    apiProperties: {
      statisticsEnabled: true
    }
  }
  tags: {
    environment: environment
    project: projectName
  }
}

// Search Service
resource searchService 'Microsoft.Search/searchServices@2020-08-01' = {
  name: searchServiceName
  location: location
  sku: {
    name: 'basic'
  }
  properties: {
    replicaCount: 1
    partitionCount: 1
    hostingMode: 'default'
  }
  tags: {
    environment: environment
    project: projectName
  }
}

// Storage Account
resource storageAccount 'Microsoft.Storage/storageAccounts@2021-04-01' = {
  name: storageAccountName
  location: location
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
  properties: {
    accessTier: 'Hot'
  }
  tags: {
    environment: environment
    project: projectName
  }
}

// Key Vault for secrets
resource keyVault 'Microsoft.KeyVault/vaults@2021-06-01-preview' = {
  name: keyVaultName
  location: location
  properties: {
    enabledForDeployment: true
    enabledForTemplateDeployment: true
    enableRbacAuthorization: false
    tenantId: subscription().tenantId
    sku: {
      family: 'A'
      name: 'standard'
    }
    accessPolicies: []
  }
  tags: {
    environment: environment
    project: projectName
  }
}

// Store Cognitive Services key in Key Vault
resource cognitiveServicesKeySecret 'Microsoft.KeyVault/vaults/secrets@2021-06-01-preview' = {
  parent: keyVault
  name: 'CognitiveServicesKey'
  properties: {
    value: cognitiveServices.listKeys().key1
  }
}

// Store Search Service key in Key Vault
resource searchServiceKeySecret 'Microsoft.KeyVault/vaults/secrets@2021-06-01-preview' = {
  parent: keyVault
  name: 'SearchServiceKey'
  properties: {
    value: searchService.listAdminKeys().primaryKey
  }
}

// Outputs
output cognitiveServicesEndpoint string = cognitiveServices.properties.endpoint
output cognitiveServicesAccountName string = cognitiveServices.name
output searchServiceEndpoint string = 'https://${searchService.name}.search.windows.net'
output searchServiceName string = searchService.name
output storageAccountName string = storageAccount.name
output keyVaultName string = keyVault.name
```

**Deployment:**
```bash
az deployment group create \
  --resource-group myResourceGroup \
  --template-file main.bicep \
  --parameters projectName=myproject location=eastus skuName=S0 environment=prod
```

---

## Azure CLI Commands - Service Creation

### Prerequisites
```bash
# Login to Azure
az login

# Set default subscription
az account set --subscription "YOUR_SUBSCRIPTION_ID"

# Create resource group (required for all services)
az group create \
  --name myResourceGroup \
  --location eastus
```

---

### 1. Computer Vision Service

```bash
# Create Computer Vision account
az cognitiveservices account create \
  --name myComputerVision \
  --resource-group myResourceGroup \
  --kind ComputerVision \
  --sku S1 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myComputerVision \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myComputerVision \
  --resource-group myResourceGroup \
  --query properties.endpoint

# Delete service (when done)
az cognitiveservices account delete \
  --name myComputerVision \
  --resource-group myResourceGroup
```

---

### 2. Custom Vision Service

```bash
# Create Custom Vision Training account
az cognitiveservices account create \
  --name myCustomVisionTraining \
  --resource-group myResourceGroup \
  --kind CustomVision.Training \
  --sku F0 \
  --location eastus \
  --yes

# Create Custom Vision Prediction account
az cognitiveservices account create \
  --name myCustomVisionPrediction \
  --resource-group myResourceGroup \
  --kind CustomVision.Prediction \
  --sku F0 \
  --location eastus \
  --yes

# Get training key
az cognitiveservices account keys list \
  --name myCustomVisionTraining \
  --resource-group myResourceGroup

# Get prediction key
az cognitiveservices account keys list \
  --name myCustomVisionPrediction \
  --resource-group myResourceGroup

# List Custom Vision projects
az cognitiveservices account list \
  --resource-group myResourceGroup \
  --query "[?kind=='CustomVision.Training']"
```

---

### 3. Content Moderator Service

```bash
# Create Content Moderator account
az cognitiveservices account create \
  --name myContentModerator \
  --resource-group myResourceGroup \
  --kind ContentModerator \
  --sku S0 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myContentModerator \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myContentModerator \
  --resource-group myResourceGroup \
  --query properties.endpoint

# Update account (e.g., change SKU)
az cognitiveservices account update \
  --name myContentModerator \
  --resource-group myResourceGroup \
  --sku S1
```

---

### 4. Text Analytics Service

```bash
# Create Text Analytics account
az cognitiveservices account create \
  --name myTextAnalytics \
  --resource-group myResourceGroup \
  --kind TextAnalytics \
  --sku S \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myTextAnalytics \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myTextAnalytics \
  --resource-group myResourceGroup \
  --query properties.endpoint

# Regenerate keys
az cognitiveservices account keys regenerate \
  --name myTextAnalytics \
  --resource-group myResourceGroup \
  --key-name key1
```

---

### 5. LUIS (Language Understanding) Service

```bash
# Create LUIS Authoring account
az cognitiveservices account create \
  --name myLuisAuthoring \
  --resource-group myResourceGroup \
  --kind LUIS.Authoring \
  --sku F0 \
  --location westus \
  --yes

# Create LUIS Prediction account
az cognitiveservices account create \
  --name myLuisPrediction \
  --resource-group myResourceGroup \
  --kind LUIS \
  --sku S0 \
  --location eastus \
  --yes

# Get authoring key
az cognitiveservices account keys list \
  --name myLuisAuthoring \
  --resource-group myResourceGroup

# Get prediction key
az cognitiveservices account keys list \
  --name myLuisPrediction \
  --resource-group myResourceGroup

# Export LUIS app
az cognitiveservices account keys list \
  --name myLuisAuthoring \
  --resource-group myResourceGroup \
  --query "key1"
```

---

### 6. Translator Service

```bash
# Create Translator account
az cognitiveservices account create \
  --name myTranslator \
  --resource-group myResourceGroup \
  --kind TextTranslation \
  --sku S1 \
  --location global \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myTranslator \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myTranslator \
  --resource-group myResourceGroup \
  --query properties.endpoint

# Create Translator for Document Translation
az cognitiveservices account create \
  --name myDocTranslator \
  --resource-group myResourceGroup \
  --kind TextTranslation \
  --sku S1 \
  --location eastus \
  --yes
```

---

### 7. Speech Services

```bash
# Create Speech account
az cognitiveservices account create \
  --name mySpeech \
  --resource-group myResourceGroup \
  --kind SpeechServices \
  --sku S0 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name mySpeech \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name mySpeech \
  --resource-group myResourceGroup \
  --query properties.endpoint

# List all Speech accounts
az cognitiveservices account list \
  --resource-group myResourceGroup \
  --query "[?kind=='SpeechServices']"

# Show Speech account details
az cognitiveservices account show \
  --name mySpeech \
  --resource-group myResourceGroup
```

---

### 8. Document Intelligence Service

```bash
# Create Document Intelligence account
az cognitiveservices account create \
  --name myDocumentIntelligence \
  --resource-group myResourceGroup \
  --kind FormRecognizer \
  --sku S0 \
  --location eastus \
  --yes

# Get API key
az cognitiveservices account keys list \
  --name myDocumentIntelligence \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myDocumentIntelligence \
  --resource-group myResourceGroup \
  --query properties.endpoint

# Create with advanced options
az cognitiveservices account create \
  --name myAdvancedFormRecognizer \
  --resource-group myResourceGroup \
  --kind FormRecognizer \
  --sku S0 \
  --location eastus \
  --public-network-access Enabled \
  --yes
```

---

### 9. Video Indexer Service

```bash
# Note: Video Indexer is managed through portal/API, not directly through az cli
# But you can create a Media Services account that supports it

# Create Media Services account (prerequisite)
az group create \
  --name myMediaResourceGroup \
  --location eastus

az storage account create \
  --name mystorageaccount \
  --resource-group myMediaResourceGroup

az ams account create \
  --name myMediaServicesAccount \
  --resource-group myMediaResourceGroup \
  --storage-account mystorageaccount \
  --location eastus

# Create Storage account for Video Indexer
az storage account create \
  --name myvideoindexerstorage \
  --resource-group myResourceGroup \
  --location eastus \
  --sku Standard_LRS

# Get storage key
az storage account keys list \
  --name myvideoindexerstorage \
  --resource-group myResourceGroup
```

---

### 10. Azure AI Search Service

```bash
# Create Azure AI Search service
az search service create \
  --name myaisearch \
  --resource-group myResourceGroup \
  --sku basic \
  --location eastus

# Alternative: Create with Standard tier
az search service create \
  --name myaisearchstandard \
  --resource-group myResourceGroup \
  --sku standard \
  --location eastus \
  --partition-count 1 \
  --replica-count 1

# Get admin key
az search admin-key show \
  --resource-group myResourceGroup \
  --service-name myaisearch

# Get query key
az search query-key list \
  --resource-group myResourceGroup \
  --service-name myaisearch

# Create query key
az search query-key create \
  --resource-group myResourceGroup \
  --service-name myaisearch \
  --name my-query-key

# Delete query key
az search query-key delete \
  --resource-group myResourceGroup \
  --service-name myaisearch \
  --key-id my-query-key

# Show service details
az search service show \
  --resource-group myResourceGroup \
  --name myaisearch

# List all Search services
az search service list \
  --resource-group myResourceGroup

# Scale up service
az search service update \
  --resource-group myResourceGroup \
  --name myaisearch \
  --partition-count 2 \
  --replica-count 2
```

---

### 11. Key Vault (For Storing Service Keys)

```bash
# Create Key Vault
az keyvault create \
  --resource-group myResourceGroup \
  --name myKeyVault \
  --location eastus

# Store Computer Vision key in Key Vault
az keyvault secret set \
  --vault-name myKeyVault \
  --name ComputerVisionKey \
  --value "YOUR_COMPUTER_VISION_KEY"

# Store Speech key
az keyvault secret set \
  --vault-name myKeyVault \
  --name SpeechKey \
  --value "YOUR_SPEECH_KEY"

# Store Text Analytics key
az keyvault secret set \
  --vault-name myKeyVault \
  --name TextAnalyticsKey \
  --value "YOUR_TEXT_ANALYTICS_KEY"

# Retrieve secret
az keyvault secret show \
  --vault-name myKeyVault \
  --name ComputerVisionKey

# List all secrets
az keyvault secret list \
  --vault-name myKeyVault

# Delete secret
az keyvault secret delete \
  --vault-name myKeyVault \
  --name ComputerVisionKey
```

---

### 12. Application Insights (For Monitoring)

```bash
# Create Application Insights
az monitor app-insights component create \
  --app myAppInsights \
  --location eastus \
  --resource-group myResourceGroup \
  --application-type web

# Link to Cognitive Services
az cognitiveservices account update \
  --name myComputerVision \
  --resource-group myResourceGroup \
  --api-properties StatisticsEnabled=true

# Get instrumentation key
az monitor app-insights component show \
  --app myAppInsights \
  --resource-group myResourceGroup \
  --query instrumentationKey
```

---

### Complete Deployment Script

```bash
#!/bin/bash

# Set variables
RG_NAME="myAIResourceGroup"
LOCATION="eastus"
PROJECT_NAME="myaiproject"

# Create resource group
echo "Creating resource group..."
az group create \
  --name $RG_NAME \
  --location $LOCATION

# Create Computer Vision
echo "Creating Computer Vision..."
az cognitiveservices account create \
  --name ${PROJECT_NAME}-vision \
  --resource-group $RG_NAME \
  --kind ComputerVision \
  --sku S1 \
  --location $LOCATION \
  --yes

# Create Text Analytics
echo "Creating Text Analytics..."
az cognitiveservices account create \
  --name ${PROJECT_NAME}-text \
  --resource-group $RG_NAME \
  --kind TextAnalytics \
  --sku S \
  --location $LOCATION \
  --yes

# Create Speech Services
echo "Creating Speech Services..."
az cognitiveservices account create \
  --name ${PROJECT_NAME}-speech \
  --resource-group $RG_NAME \
  --kind SpeechServices \
  --sku S0 \
  --location $LOCATION \
  --yes

# Create Azure AI Search
echo "Creating Azure AI Search..."
az search service create \
  --name ${PROJECT_NAME}-search \
  --resource-group $RG_NAME \
  --sku standard \
  --location $LOCATION

# Create Key Vault
echo "Creating Key Vault..."
az keyvault create \
  --resource-group $RG_NAME \
  --name ${PROJECT_NAME}-kv \
  --location $LOCATION

# Get keys and store in Key Vault
echo "Retrieving and storing keys..."
CV_KEY=$(az cognitiveservices account keys list \
  --name ${PROJECT_NAME}-vision \
  --resource-group $RG_NAME \
  --query key1 -o tsv)

az keyvault secret set \
  --vault-name ${PROJECT_NAME}-kv \
  --name ComputerVisionKey \
  --value $CV_KEY

# Create Application Insights
echo "Creating Application Insights..."
az monitor app-insights component create \
  --app ${PROJECT_NAME}-insights \
  --location $LOCATION \
  --resource-group $RG_NAME \
  --application-type web

echo "Deployment completed!"

# Display summary
echo -e "\n=== Deployment Summary ==="
echo "Resource Group: $RG_NAME"
echo "Location: $LOCATION"
az cognitiveservices account list \
  --resource-group $RG_NAME \
  --query "[].{Name:name, Kind:kind}"

az search service list \
  --resource-group $RG_NAME \
  --query "[].{Name:name, Sku:sku.name}"
```

---

### Useful Azure CLI Commands for Management

```bash
# List all AI services in resource group
az cognitiveservices account list \
  --resource-group myResourceGroup

# Get service details
az cognitiveservices account show \
  --name myComputerVision \
  --resource-group myResourceGroup

# List service locations
az cognitiveservices account list-kinds

# Check SKU availability
az cognitiveservices account list-skus \
  --kind ComputerVision

# Delete all services in resource group
az cognitiveservices account list \
  --resource-group myResourceGroup \
  --query "[].name" -o tsv | \
  xargs -I {} az cognitiveservices account delete \
  --name {} \
  --resource-group myResourceGroup \
  --yes

# Export service configuration
az cognitiveservices account show \
  --name myComputerVision \
  --resource-group myResourceGroup \
  --output json > backup.json

# Clean up (delete entire resource group)
az group delete \
  --name myResourceGroup \
  --yes --no-wait
```

---

## Authentication and Authorization

### Azure Credentials Configuration

```python
from azure.identity import DefaultAzureCredential, ClientSecretCredential
from azure.core.credentials import AzureKeyCredential

# Method 1: Using Default Azure Credentials (recommended for development)
credentials = DefaultAzureCredential()

# Method 2: Using Service Principal
credentials = ClientSecretCredential(
    tenant_id="YOUR_TENANT_ID",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET"
)

# Method 3: Using API Key (for some services)
credentials = AzureKeyCredential(key="YOUR_API_KEY")
```

---

## Best Practices and Patterns

### 1. Error Handling

```python
from azure.core.exceptions import HttpResponseError
from azure.cognitiveservices.vision.computervision.models import ComputerVisionErrorException

try:
    result = client.analyze_image_in_stream(image_data, visual_features)
except HttpResponseError as e:
    print(f"Error: {e.status_code}")
    print(f"Message: {e.message}")
except ComputerVisionErrorException as e:
    print(f"Computer Vision Error: {e}")
```

### 2. Rate Limiting and Retry Logic

```python
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(wait=wait_exponential(multiplier=1, min=2, max=10), stop=stop_after_attempt(3))
def call_api_with_retry():
    return client.analyze_image_in_stream(image_data, visual_features)

try:
    result = call_api_with_retry()
except Exception as e:
    print(f"Failed after retries: {e}")
```

### 3. Batch Processing

```python
def batch_process_documents(documents, batch_size=10):
    results = []
    
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]
        
        try:
            batch_results = client.analyze_sentiment(documents=batch, language="en")
            results.extend(batch_results)
        except HttpResponseError as e:
            print(f"Error processing batch {i//batch_size}: {e}")
    
    return results
```

---

## Common API Response Codes

| Status Code | Description |
|------------|-------------|
| 200 | Success |
| 201 | Created |
| 202 | Accepted (Async operation) |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 429 | Rate Limited |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

---

## Quick Reference

### Service Endpoints

```
Computer Vision: https://{region}.api.cognitive.microsoft.com/
Text Analytics: https://{region}.api.cognitive.microsoft.com/
LUIS: https://{region}.api.cognitive.microsoft.com/
Translator: https://api.cognitive.microsofttranslator.com/
Speech STT: https://{region}.stt.speech.microsoft.com/
Speech TTS: https://{region}.tts.speech.microsoft.com/
Document Intelligence: https://{region}.api.cognitive.microsoft.com/
Azure AI Search: https://{resource-name}.search.windows.net/
```

### Common Imports

```python
# Vision
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

# NLP
from azure.ai.textanalytics import TextAnalyticsClient
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient

# Speech
import azure.cognitiveservices.speech as speechsdk

# Document Intelligence
from azure.ai.documentintelligence import DocumentIntelligenceClient

# Search
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient

# Authentication
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
```

---

## Sample Complete Application

### End-to-End Document Processing Pipeline

```python
import os
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.textanalytics import TextAnalyticsClient
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential

class DocumentProcessingPipeline:
    def __init__(self, subscription_key, endpoint, search_endpoint, search_key, search_index):
        self.doc_client = DocumentIntelligenceClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(subscription_key)
        )
        
        self.text_client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(subscription_key)
        )
        
        self.search_client = SearchClient(
            endpoint=search_endpoint,
            index_name=search_index,
            credential=AzureKeyCredential(search_key)
        )
    
    def extract_content(self, document_path):
        """Extract content from document using Document Intelligence"""
        with open(document_path, "rb") as f:
            poller = self.doc_client.begin_analyze_document(
                model_id="prebuilt-layout",
                document=f
            )
        
        result = poller.result()
        
        extracted_data = {
            "content": result.content,
            "pages": len(result.pages),
            "tables": [],
            "key_value_pairs": []
        }
        
        return extracted_data
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of extracted text"""
        response = self.text_client.analyze_sentiment(
            documents=[text],
            language="en"
        )[0]
        
        return {
            "sentiment": response.sentiment,
            "positive": response.confidence_scores.positive,
            "neutral": response.confidence_scores.neutral,
            "negative": response.confidence_scores.negative
        }
    
    def extract_entities(self, text):
        """Extract entities from text"""
        response = self.text_client.recognize_entities(
            documents=[text],
            language="en"
        )[0]
        
        entities = [
            {"text": entity.text, "type": entity.category}
            for entity in response.entities
        ]
        
        return entities
    
    def index_document(self, doc_id, title, content, entities):
        """Index processed document in Azure AI Search"""
        document = {
            "id": doc_id,
            "title": title,
            "content": content,
            "entities": entities,
            "indexed_at": os.urandom(16).hex()
        }
        
        result = self.search_client.upload_documents(documents=[document])
        
        return result
    
    def process_document(self, document_path, doc_id, title):
        """Complete pipeline: extract -> analyze -> index"""
        print(f"Processing: {document_path}")
        
        # Extract content
        extracted = self.extract_content(document_path)
        print(f"  Extracted {extracted['pages']} pages")
        
        # Analyze sentiment
        sentiment = self.analyze_sentiment(extracted["content"])
        print(f"  Sentiment: {sentiment['sentiment']}")
        
        # Extract entities
        entities = self.extract_entities(extracted["content"])
        print(f"  Entities found: {len(entities)}")
        
        # Index document
        self.index_document(doc_id, title, extracted["content"], entities)
        print(f"  Document indexed")
        
        return {
            "extracted": extracted,
            "sentiment": sentiment,
            "entities": entities
        }

# Usage
if __name__ == "__main__":
    subscription_key = "YOUR_SUBSCRIPTION_KEY"
    endpoint = "YOUR_ENDPOINT"
    search_endpoint = "YOUR_SEARCH_ENDPOINT"
    search_key = "YOUR_SEARCH_KEY"
    search_index = "documents"
    
    pipeline = DocumentProcessingPipeline(
        subscription_key,
        endpoint,
        search_endpoint,
        search_key,
        search_index
    )
    
    result = pipeline.process_document(
        "document.pdf",
        "doc_001",
        "Sample Document"
    )
    
    print("\nProcessing complete:")
    print(f"  Sentiment: {result['sentiment']['sentiment']}")
    print(f"  Entities: {len(result['entities'])}")
```

---

## Summary Table of Services

| Service | Primary Use | Authentication | Response Time |
|---------|------------|-----------------|-----------------|
| Computer Vision | Image analysis | API Key / Managed Identity | <1 sec |
| Custom Vision | Custom image models | API Key | <1 sec |
| Content Moderator | Content filtering | API Key | <1 sec |
| Text Analytics | NLP tasks | API Key | <1 sec |
| LUIS | Intent/Entity recognition | API Key | <1 sec |
| Translator | Machine translation | API Key | <1 sec |
| Speech STT | Audio to text | API Key | Variable |
| Speech TTS | Text to speech | API Key | Variable |
| Document Intelligence | Document extraction | API Key | Variable |
| Video Indexer | Video analysis | API Key | 2-24 hours |
| Azure AI Search | Intelligent search | API Key | <1 sec |

---

## Comprehensive Service Limitations Reference

### Rate Limits by Tier

**Free Tier Characteristics:**
- Limited API calls (typically 1-20 per minute)
- Monthly quota restrictions (usually 1K-10K transactions)
- Single region only
- No SLA guarantees
- Good for development/testing

**Standard/Premium Tiers:**
- Higher throughput (10-200+ requests/sec)
- Pay-as-you-go or commitment plans
- Multiple regions available
- SLA guarantees (99.9-99.95%)
- Priority support

### Common Limitations Across Services

**Quota Limits:**
```
Free Tier:
- Computer Vision: 20 calls/min, 5K transactions/month
- Text Analytics: 100 calls/min, 5K records/month
- Speech: 1,000 minutes/month
- Document Intelligence: 2 transactions/min, 500 pages/month

Standard Tier:
- Typically 10-100x higher than Free tier
- Can be increased via support request
- No monthly quota (pay per transaction)
```

**Processing Limits:**
```
Request Timeout: 30-90 seconds (varies by service)
Max Batch Size: 10-1000 items (depends on service)
Max File Size: 2-4 MB for images, up to 2 GB for videos
Concurrent Connections: 10-100+ (tier-dependent)
```

**Data Retention:**
```
- Customer data: Generally not retained by Microsoft
- Logs: 30 days in Application Insights (default)
- Training data: Retained for model improvement (can be disabled)
```

### Pricing Considerations for Limits

**Free Tier vs. Paid:**
| Aspect | Free | Paid |
|--------|------|------|
| Monthly Cost | $0 | $0.001-$10+ per transaction |
| Rate Limit | 1-20 calls/min | 10-200 calls/sec |
| Support | Community | Professional |
| SLA | None | 99.9% uptime |
| Scalability | Limited | Unlimited |

**Avoiding Rate Limit Errors:**
1. Implement exponential backoff retry logic
2. Use batch processing where available
3. Cache results appropriately
4. Monitor usage with Application Insights
5. Plan for peak load scenarios
6. Consider upgrading tier during high-demand periods

### Storage and Quota Management

**Index/Document Limits:**
- Computer Vision: Unlimited images (per pricing tier)
- Custom Vision: 500 tags, unlimited images per tag
- Document Intelligence: 500 pages per document
- Azure AI Search: Unlimited documents (storage-based)
- Video Indexer: Based on subscription storage quota

**Model Limits:**
- Custom Vision: 10 active models per project
- Document Intelligence: Unlimited custom models
- Speech: 10 custom models concurrently
- LUIS: 500 intents, 500 entities per app

### Regional Availability

**Most Available (50+ regions):**
- Computer Vision
- Text Analytics
- Speech Services
- Azure AI Search

**Limited Regions (5-20):**
- Custom Vision
- LUIS
- Document Intelligence
- Video Indexer

**Always check regional availability** before choosing subscription location, especially for Custom Vision and Video Indexer.

### Performance and Reliability

**Expected Response Times:**
```
Real-time Services (<1 sec):
- Computer Vision: 100-500ms
- Text Analytics: 200-800ms
- LUIS: 300-1000ms
- Translator: 300-1500ms
- Search: 50-200ms

Batch Services (Variable):
- Document Intelligence: 10-60 sec per document
- Video Indexer: 1-24 hours per video
- Batch Speech: 2-5x real-time duration
```

**Reliability Metrics:**
- SLA Uptime: 99.9% - 99.95% (Standard tiers)
- Recovery Time Objective (RTO): <15 minutes
- Recovery Point Objective (RPO): <5 minutes

### Cost Optimization Tips

1. **Use Free Tier for Development**
   - Test APIs and build solutions
   - Move to Standard when in production

2. **Batch Processing**
   - Use batch endpoints for batch transcription
   - Combine multiple documents in single requests where possible

3. **Caching**
   - Cache sentiment analysis results
   - Cache translation results (transliteration)
   - Use Azure Cache for Redis for frequent queries

4. **Commitment Plans**
   - 1-year or 3-year commitments offer discounts
   - Available for major services (Speech, Translator, etc.)
   - Locked pricing regardless of consumption

5. **Regional Pricing**
   - Prices vary by region
   - Consider multi-region deployment for cost optimization

### Monitoring Limits

**Use Application Insights to monitor:**
- API call count and frequency
- Error rates and types
- Response times
- Quota consumption
- Cost tracking

```python
# Example: Monitor API usage with Application Insights
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler())
logger.warning(f"API call count: {api_call_count}")
```

---

## Bounding Box Concepts and Implementation

### 1. What is a Bounding Box?

**Definition:**
A bounding box is a rectangular region that precisely locates and encloses an object, person, text, or region of interest in an image. It's fundamental to computer vision tasks like object detection, face detection, and document understanding.

**Key Components:**

| Component | Description |
|-----------|------------|
| **X-coordinate (left)** | Pixel distance from left edge of image |
| **Y-coordinate (top)** | Pixel distance from top edge of image |
| **Width** | Horizontal extent of bounding box |
| **Height** | Vertical extent of bounding box |
| **Confidence Score** | Probability (0-1) that detection is correct |
| **Class Label** | Object type (person, apple, face, text) |

**Coordinate Systems:**

| Format | Representation | Example |
|--------|----------------|---------|
| **(x, y, width, height)** | Top-left position + dimensions | (100, 50, 200, 150) |
| **(x1, y1, x2, y2)** | Top-left and bottom-right corners | (100, 50, 300, 200) |
| **Normalized (0-1)** | Proportional to image dimensions | (0.1, 0.05, 0.3, 0.2) |

### 2. Bounding Box Use Cases in Azure AI

**Object Detection:**
Locate and identify multiple objects (cars, people, animals, products) in images

**Face Detection:**
Identify and outline human faces in photos for analysis or blurring

**Document Processing:**
Locate text blocks, tables, and form fields in scanned documents

**Person Detection:**
Find and track people in images or video frames

**Custom Vision:**
Detect domain-specific objects in training and prediction

### 3. Python Code Example - Working with Bounding Boxes

```python
from PIL import Image, ImageDraw
from typing import List, Tuple
import json

class BoundingBox:
    def __init__(self, x: float, y: float, width: float, height: float, 
                 label: str = "", confidence: float = 1.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.confidence = confidence
    
    def get_coordinates(self) -> Tuple[float, float, float, float]:
        """Get (x1, y1, x2, y2) format"""
        return (
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height
        )
    
    def to_normalized(self, image_width: int, image_height: int) -> dict:
        """Convert to normalized coordinates (0-1 range)"""
        return {
            "left": self.x / image_width,
            "top": self.y / image_height,
            "width": self.width / image_width,
            "height": self.height / image_height
        }
    
    def to_pixel(self, image_width: int, image_height: int) -> dict:
        """Convert normalized coordinates to pixels"""
        return {
            "x": int(self.x * image_width),
            "y": int(self.y * image_height),
            "width": int(self.width * image_width),
            "height": int(self.height * image_height)
        }

class BoundingBoxVisualizer:
    def __init__(self, image_path: str):
        self.image = Image.open(image_path)
        self.draw = ImageDraw.Draw(self.image)
    
    def draw_boxes(self, boxes: List[BoundingBox], color: str = "cyan", width: int = 3):
        """Draw bounding boxes on image"""
        for box in boxes:
            # Get corner coordinates
            x1, y1, x2, y2 = box.get_coordinates()
            
            # Draw rectangle
            self.draw.rectangle([x1, y1, x2, y2], outline=color, width=width)
            
            # Draw label with confidence
            if box.label:
                label_text = f"{box.label} ({box.confidence:.2f})"
                self.draw.text((x1, y1 - 10), label_text, fill=color)
    
    def save(self, output_path: str):
        """Save annotated image"""
        self.image.save(output_path)
        print(f"Annotated image saved to {output_path}")

# Usage Example
def process_object_detection():
    """Example with detected objects"""
    
    # Sample detections (from Azure Vision API)
    detections = [
        BoundingBox(x=100, y=50, width=150, height=200, label="person", confidence=0.95),
        BoundingBox(x=300, y=100, width=100, height=100, label="dog", confidence=0.87),
        BoundingBox(x=450, y=80, width=120, height=140, label="person", confidence=0.92)
    ]
    
    # Visualize
    visualizer = BoundingBoxVisualizer("image.jpg")
    visualizer.draw_boxes(detections)
    visualizer.save("annotated_image.jpg")

# Convert between formats
def normalize_coordinates(pixel_box: dict, image_width: int, image_height: int) -> dict:
    """Convert pixel coordinates to normalized (0-1)"""
    return {
        "left": pixel_box["x"] / image_width,
        "top": pixel_box["y"] / image_height,
        "right": (pixel_box["x"] + pixel_box["width"]) / image_width,
        "bottom": (pixel_box["y"] + pixel_box["height"]) / image_height
    }

def denormalize_coordinates(normalized_box: dict, image_width: int, image_height: int) -> dict:
    """Convert normalized coordinates to pixel"""
    return {
        "x": int(normalized_box["left"] * image_width),
        "y": int(normalized_box["top"] * image_height),
        "width": int((normalized_box["right"] - normalized_box["left"]) * image_width),
        "height": int((normalized_box["bottom"] - normalized_box["top"]) * image_height)
    }
```

### 4. Intersection over Union (IoU) - Bounding Box Metrics

**IoU Calculation:**
Measures overlap between predicted and ground-truth bounding boxes (0-1, higher is better)

```python
def calculate_iou(box1: BoundingBox, box2: BoundingBox) -> float:
    """Calculate Intersection over Union between two bounding boxes"""
    
    # Get coordinates
    x1_min, y1_min, x1_max, y1_max = box1.get_coordinates()
    x2_min, y2_min, x2_max, y2_max = box2.get_coordinates()
    
    # Calculate intersection
    inter_x_min = max(x1_min, x2_min)
    inter_y_min = max(y1_min, y2_min)
    inter_x_max = min(x1_max, x2_max)
    inter_y_max = min(y1_max, y2_max)
    
    # Check if there's overlap
    if inter_x_max < inter_x_min or inter_y_max < inter_y_min:
        return 0.0
    
    # Calculate areas
    intersection_area = (inter_x_max - inter_x_min) * (inter_y_max - inter_y_min)
    box1_area = box1.width * box1.height
    box2_area = box2.width * box2.height
    union_area = box1_area + box2_area - intersection_area
    
    # IoU = Intersection / Union
    return intersection_area / union_area if union_area > 0 else 0.0

# Usage
predicted_box = BoundingBox(100, 50, 150, 200, "person")
ground_truth_box = BoundingBox(110, 60, 140, 190, "person")
iou = calculate_iou(predicted_box, ground_truth_box)
print(f"IoU: {iou:.4f}")  # Higher IoU = better detection accuracy
```

### 5. Bounding Boxes in Azure Services

#### Azure Computer Vision - Object Detection

```python
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

def detect_objects_with_boxes(image_path: str, client: ComputerVisionClient):
    """Detect objects and get bounding boxes"""
    
    with open(image_path, "rb") as image_data:
        results = client.analyze_image_in_stream(
            image_data,
            visual_features=[VisualFeatureTypes.objects]
        )
    
    # Process detected objects
    boxes = []
    for obj in results.objects:
        box = BoundingBox(
            x=obj.rectangle.x,
            y=obj.rectangle.y,
            width=obj.rectangle.w,
            height=obj.rectangle.h,
            label=obj.object_property,
            confidence=obj.confidence
        )
        boxes.append(box)
        print(f"Object: {obj.object_property} - Confidence: {obj.confidence:.2f}")
        print(f"  Position: ({obj.rectangle.x}, {obj.rectangle.y})")
        print(f"  Size: {obj.rectangle.w}x{obj.rectangle.h}")
    
    return boxes
```

#### Azure Face API - Face Detection

```python
from azure.ai.vision.face import FaceClient
from azure.core.credentials import AzureKeyCredential

def detect_faces_with_boxes(image_path: str, face_client: FaceClient):
    """Detect faces and get bounding boxes"""
    
    with open(image_path, "rb") as image_data:
        detected_faces = face_client.detect(image_content=image_data.read())
    
    boxes = []
    for i, face in enumerate(detected_faces):
        rect = face.face_rectangle
        box = BoundingBox(
            x=rect.left,
            y=rect.top,
            width=rect.width,
            height=rect.height,
            label=f"Face {i+1}",
            confidence=1.0
        )
        boxes.append(box)
        print(f"Face {i+1}: x={rect.left}, y={rect.top}, size={rect.width}x{rect.height}")
    
    return boxes
```

#### Custom Vision - Object Detection

```python
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

def detect_custom_objects(image_path: str, prediction_client: CustomVisionPredictionClient,
                         project_id: str, model_name: str):
    """Detect objects using Custom Vision model"""
    
    with open(image_path, "rb") as image_data:
        results = prediction_client.detect_image(
            project_id,
            model_name,
            image_data
        )
    
    boxes = []
    for prediction in results.predictions:
        if prediction.probability > 0.5:  # Confidence threshold
            # Normalize to pixel coordinates
            box = BoundingBox(
                x=prediction.bounding_box.left,
                y=prediction.bounding_box.top,
                width=prediction.bounding_box.width,
                height=prediction.bounding_box.height,
                label=prediction.tag_name,
                confidence=prediction.probability
            )
            boxes.append(box)
    
    return boxes
```

### 6. Bounding Box REST API Response Format

**Azure Computer Vision Response:**

```json
{
  "objects": [
    {
      "rectangle": {
        "x": 100,
        "y": 50,
        "w": 150,
        "h": 200
      },
      "object": "person",
      "confidence": 0.95
    },
    {
      "rectangle": {
        "x": 300,
        "y": 100,
        "w": 100,
        "h": 100
      },
      "object": "dog",
      "confidence": 0.87
    }
  ]
}
```

**Azure Face API Response:**

```json
{
  "faceId": "f7edddc4-6c88-4d66-9a45-6f944ea409f0",
  "faceRectangle": {
    "top": 50,
    "left": 100,
    "width": 150,
    "height": 200
  },
  "faceAttributes": {
    "age": 28.3,
    "gender": "male",
    "emotion": {
      "anger": 0,
      "contempt": 0,
      "disgust": 0,
      "fear": 0,
      "happiness": 1,
      "neutral": 0,
      "sadness": 0,
      "surprise": 0
    }
  }
}
```

**Custom Vision Response:**

```json
{
  "predictions": [
    {
      "tagName": "apple",
      "probability": 0.92,
      "boundingBox": {
        "left": 0.1,
        "top": 0.2,
        "width": 0.3,
        "height": 0.4
      }
    }
  ]
}
```

### 7. Best Practices for Bounding Boxes

| Practice | Details |
|----------|---------|
| **Confidence Threshold** | Filter out low-confidence detections (typically 0.5+) |
| **Non-Maximum Suppression (NMS)** | Remove overlapping boxes, keep highest confidence |
| **Input Normalization** | Normalize coordinates if needed (0-1 range) |
| **Aspect Ratio** | Maintain object proportions for accurate localization |
| **Multiple Scales** | Test different image resolutions for better detection |
| **Annotation Clarity** | Use distinct colors and clear labels for visualization |
| **Performance Metrics** | Use IoU to evaluate detection accuracy |

---

## Azure AI Models

### 1. Large Language Models (LLMs)

#### GPT-4

**Model Overview:**
GPT-4 is the latest generation language model from OpenAI, featuring improved reasoning, longer context window, and multimodal capabilities (text and vision).

**Model Capabilities:**

| Capability | Details |
|-----------|---------|
| **Context Window** | 8K tokens (base) or 32K tokens (extended) or 128K tokens (turbo) |
| **Input Tokens** | $0.03 per 1K tokens |
| **Output Tokens** | $0.06 per 1K tokens |
| **Max Tokens** | 4,096 output tokens per request |
| **Multimodal** | Yes - vision capabilities included |
| **Training Data** | Up to April 2024 |
| **Reasoning** | Advanced (step-by-step logic) |
| **Code Generation** | Excellent (multiple languages) |
| **Knowledge** | 128K context window for document understanding |

**Python Code Example - GPT-4 Usage:**

```python
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_key="YOUR_API_KEY",
    api_version="2024-05-01-preview",
    azure_endpoint="YOUR_ENDPOINT"
)

# Simple text completion
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are an expert AI engineer. Provide concise, technical answers."
        },
        {
            "role": "user",
            "content": "Explain neural networks in 3 sentences."
        }
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)

# GPT-4 with vision capability
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/image.jpg"
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)

# Complex reasoning with GPT-4
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": """
            I have 5 apples and 3 oranges. I give 2 apples to a friend.
            Then I buy 4 more apples. How many apples and oranges do I have now?
            Show your step-by-step reasoning.
            """
        }
    ],
    temperature=0.5,
    max_tokens=1000
)

print(response.choices[0].message.content)
```

**REST API Example - GPT-4:**

```bash
curl -X POST \
  "YOUR_ENDPOINT/openai/deployments/gpt-4/chat/completions?api-version=2024-05-01-preview" \
  -H "api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful AI assistant."
      },
      {
        "role": "user",
        "content": "What is Azure AI Foundry?"
      }
    ],
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 0.95
  }'

# Response
{
  "id": "chatcmpl-8mkAtJmXpQ...",
  "object": "chat.completion",
  "created": 1704067200,
  "model": "gpt-4",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Azure AI Foundry is a unified platform..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 150,
    "total_tokens": 175
  }
}
```

---

#### GPT-3.5 Turbo

**Model Overview:**
GPT-3.5 Turbo is a fast, cost-effective language model optimized for chat and general text tasks with good quality-to-cost ratio.

**Model Capabilities:**

| Capability | Details |
|-----------|---------|
| **Context Window** | 4K tokens (standard) or 16K tokens (extended) |
| **Input Tokens** | $0.005 per 1K tokens |
| **Output Tokens** | $0.015 per 1K tokens |
| **Max Tokens** | 4,096 output tokens |
| **Multimodal** | Limited (text only in some deployments) |
| **Speed** | Fastest response time (~200ms) |
| **Cost** | 10x cheaper than GPT-4 |
| **Training Data** | Up to April 2024 |

**Python Code Example - GPT-3.5 Turbo:**

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="YOUR_API_KEY",
    api_version="2024-05-01-preview",
    azure_endpoint="YOUR_ENDPOINT"
)

# Fast chat completion
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Generate 5 creative product names for an AI-powered chatbot."
        }
    ],
    temperature=0.8,
    max_tokens=300
)

print(response.choices[0].message.content)

# Streaming response
stream_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Write a haiku about Azure cloud services."
        }
    ],
    stream=True
)

for chunk in stream_response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")

# Function calling for tool use
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What's the weather in Seattle?"}],
    tools=tools,
    tool_choice="auto"
)

if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        print(f"Tool: {tool_call.function.name}")
        print(f"Args: {tool_call.function.arguments}")
```

---

### 2. Image Generation Models

#### DALL-E 3

**Model Overview:**
DALL-E 3 generates high-quality, photorealistic images from text descriptions with improved prompt understanding and safety.

**Model Capabilities:**

| Capability | Details |
|-----------|---------|
| **Image Sizes** | 1024x1024, 1024x1792, 1792x1024 pixels |
| **Quality** | Standard or HD (2x generation time) |
| **Cost (Standard)** | $0.080 per image (1024x1024) |
| **Cost (HD)** | $0.160 per image (1024x1024) |
| **Generation Time** | 60-90 seconds (standard), 120+ seconds (HD) |
| **Styles** | Vivid, Natural, Realistic, Artistic |
| **Prompt Understanding** | Natural language descriptions |
| **Edit Mode** | Inpainting and outpainting |

**Python Code Example - DALL-E 3:**

```python
from openai import AzureOpenAI
import requests
from PIL import Image
from io import BytesIO

client = AzureOpenAI(
    api_key="YOUR_API_KEY",
    api_version="2024-05-01-preview",
    azure_endpoint="YOUR_ENDPOINT"
)

# Generate image
response = client.images.generate(
    model="dall-e-3",
    prompt="A futuristic city skyline with flying cars and neon lights, cinematic lighting",
    size="1024x1024",
    quality="standard",
    n=1,
    style="vivid"
)

# Get image URL
image_url = response.data[0].url
print(f"Generated image: {image_url}")

# Download and save image
img_response = requests.get(image_url)
img = Image.open(BytesIO(img_response.content))
img.save("generated_image.png")

# Generate HD image
response = client.images.generate(
    model="dall-e-3",
    prompt="A serene mountain landscape with crystal clear lake reflecting the sky",
    size="1024x1024",
    quality="hd",
    n=1,
    style="natural"
)

print(f"HD Image: {response.data[0].url}")

# Batch generation
prompts = [
    "A steampunk robot in a mechanical factory",
    "Underwater bioluminescent creatures",
    "A cozy bookshop in Victorian era"
]

for prompt in prompts:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    print(f"Generated: {prompt}")
```

**REST API Example - DALL-E 3:**

```bash
# Generate image
curl -X POST \
  "YOUR_ENDPOINT/openai/images/generations?api-version=2024-05-01-preview" \
  -H "api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A serene landscape with mountains and lake",
    "size": "1024x1024",
    "quality": "standard",
    "n": 1,
    "style": "natural"
  }'

# Response
{
  "created": 1704067200,
  "data": [
    {
      "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/img-...",
      "revised_prompt": "A serene landscape with mountains and lake, high quality..."
    }
  ]
}
```

---

### 3. Video Generation Models

#### Azure Video Generation (Synthesia/Runway Integration)

**Model Overview:**
Video generation creates short videos from text descriptions, combining generative AI with video synthesis for marketing, training, and content creation.

**Model Capabilities:**

| Capability | Details |
|-----------|---------|
| **Video Length** | 5-60 seconds |
| **Resolution** | 720p, 1080p, 4K |
| **Frame Rate** | 24fps, 30fps, 60fps |
| **Format** | MP4, WebM, MOV |
| **Cost** | $0.10-0.50 per second |
| **Generation Time** | 2-5 minutes per video |
| **AI Avatars** | Multiple languages and personas |
| **Background Support** | Real backgrounds or AI-generated |
| **Audio Generation** | Text-to-speech with emotion |

**Python Code Example - Video Generation:**

```python
import requests
import json
import time

class VideoGenerator:
    def __init__(self, api_key: str, endpoint: str):
        self.api_key = api_key
        self.endpoint = endpoint
    
    def generate_video(self, prompt: str, duration: int = 30, 
                       resolution: str = "1080p") -> str:
        """Generate video from text prompt"""
        
        url = f"{self.endpoint}/video/generate"
        headers = {
            "api-key": self.api_key,
            "Content-Type": "application/json"
        }
        
        payload = {
            "prompt": prompt,
            "duration": duration,
            "resolution": resolution,
            "framerate": 30,
            "format": "mp4"
        }
        
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        
        return result.get("video_id")
    
    def get_video_status(self, video_id: str) -> dict:
        """Get video generation status"""
        
        url = f"{self.endpoint}/video/{video_id}/status"
        headers = {"api-key": self.api_key}
        
        response = requests.get(url, headers=headers)
        return response.json()
    
    def wait_for_completion(self, video_id: str, max_wait: int = 300) -> str:
        """Wait for video generation to complete"""
        
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            status = self.get_video_status(video_id)
            
            if status["status"] == "completed":
                return status["download_url"]
            elif status["status"] == "failed":
                raise Exception(f"Video generation failed: {status['error']}")
            
            time.sleep(5)
        
        raise TimeoutError("Video generation timed out")

# Usage
generator = VideoGenerator(
    api_key="YOUR_API_KEY",
    endpoint="YOUR_ENDPOINT"
)

# Generate marketing video
video_id = generator.generate_video(
    prompt="A professional product demo showing cloud computing benefits with business metrics and charts",
    duration=60,
    resolution="1080p"
)

# Wait for completion
video_url = generator.wait_for_completion(video_id)
print(f"Video ready: {video_url}")

# Generate training video
video_id = generator.generate_video(
    prompt="Step-by-step tutorial: How to deploy applications to Azure cloud using simple animations",
    duration=45,
    resolution="720p"
)
```

---

### 4. Speech Models (Text-to-Speech)

#### Azure Speech Synthesis (TTS) Models

**Model Overview:**
Neural Text-to-Speech converts text to natural-sounding speech with multiple voices, languages, and emotional styles.

**Model Capabilities:**

| Capability | Details |
|-----------|---------|
| **Voices** | 400+ neural voices across 140+ languages |
| **Emotions** | Joyful, Sad, Angry, Fearful, Neutral, Surprised |
| **Styles** | Conversation, Newscast, Cheerful, Sad, Angry |
| **Audio Formats** | MP3, WAV, OPUS, OGG, FLAC |
| **Sample Rate** | 8kHz to 48kHz |
| **Streaming** | Real-time streaming support |
| **Cost** | $16.00 per 1M characters (standard) |
| **Speed Control** | 0.5x to 2.0x |

**Python Code Example - TTS:**

```python
import azure.cognitiveservices.speech as speechsdk
import os

def text_to_speech_with_emotion(text: str, voice_name: str = "en-US-AriaNeural", 
                                emotion: str = "joyful"):
    """Convert text to speech with emotional expression"""
    
    speech_config = speechsdk.SpeechConfig(
        subscription=os.environ.get('SPEECH_KEY'),
        region=os.environ.get('SPEECH_REGION')
    )
    
    # Configure audio output
    audio_config = speechsdk.audio.AudioOutputConfig(
        filename="output.mp3"
    )
    
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config
    )
    
    # SSML for emotion and style
    ssml_string = f"""
    <speak version='1.0' xml:lang='en-US'>
        <voice xml:lang='en-US' name='{voice_name}'>
            <mstts:express-as style='{emotion}'>
                {text}
            </mstts:express-as>
        </voice>
    </speak>
    """
    
    result = synthesizer.speak_ssml_async(ssml_string).get()
    
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to output.mp3")
    else:
        print(f"Error: {result.error_details}")

# Usage with different emotions
text_to_speech_with_emotion(
    text="Welcome to Azure AI services! We're excited to help you build amazing applications.",
    voice_name="en-US-AriaNeural",
    emotion="joyful"
)

# Different voice and style
text_to_speech_with_emotion(
    text="The quarterly earnings have exceeded all projections.",
    voice_name="en-US-GuyNeural",
    emotion="newscast"
)

# Real-time streaming
def speech_synthesis_streaming(text: str) -> bytes:
    """Real-time speech streaming"""
    
    speech_config = speechsdk.SpeechConfig(
        subscription=os.environ.get('SPEECH_KEY'),
        region=os.environ.get('SPEECH_REGION')
    )
    
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config
    )
    
    result = synthesizer.speak_text_async(text).get()
    
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        return result.audio_data
```

---

### 5. Translator Models

#### Azure Translator Service

**Model Overview:**
Neural Machine Translation (NMT) models support 130+ languages with high-quality translations and language detection.

**Model Capabilities:**

| Capability | Details |
|-----------|---------|
| **Languages Supported** | 130+ languages |
| **Translation Quality** | Neural (high) vs Phrase-based (standard) |
| **Transliteration** | Convert scripts (e.g., Arabic to Latin) |
| **Sentence Alignment** | Identify parallel sentences |
| **Language Detection** | Auto-detect source language |
| **Cost** | $15.00 per 1M characters (standard) |
| **APIs** | REST, Python SDK |
| **Batch Processing** | Document translation jobs |
| **Custom Translator** | Fine-tune models for domain-specific content |

**Python Code Example - Translator:**

```python
import requests
import json
from typing import List, Dict

class AzureTranslator:
    def __init__(self, api_key: str, region: str):
        self.api_key = api_key
        self.region = region
        self.endpoint = "https://api.cognitive.microsofttranslator.com"
    
    def translate_text(self, text: str, target_language: str, 
                       source_language: str = "auto") -> str:
        """Translate text to target language"""
        
        url = f"{self.endpoint}/translate"
        params = {
            "api-version": "3.0",
            "from": source_language,
            "to": target_language
        }
        
        headers = {
            "Ocp-Apim-Subscription-Key": self.api_key,
            "Content-Type": "application/json",
            "X-ClientTraceId": str(__import__('uuid').uuid4())
        }
        
        body = [{"Text": text}]
        
        response = requests.post(
            url,
            params=params,
            headers=headers,
            json=body
        )
        
        result = response.json()
        return result[0]["translations"][0]["text"]
    
    def detect_language(self, text: str) -> Dict:
        """Detect language of text"""
        
        url = f"{self.endpoint}/detect"
        params = {"api-version": "3.0"}
        
        headers = {
            "Ocp-Apim-Subscription-Key": self.api_key,
            "Content-Type": "application/json"
        }
        
        body = [{"Text": text}]
        
        response = requests.post(
            url,
            params=params,
            headers=headers,
            json=body
        )
        
        result = response.json()
        return {
            "language": result[0]["language"],
            "score": result[0].get("score", 1.0)
        }
    
    def translate_batch(self, texts: List[str], target_language: str) -> List[str]:
        """Translate multiple texts"""
        
        translations = []
        for text in texts:
            translated = self.translate_text(text, target_language)
            translations.append(translated)
        
        return translations

# Usage
translator = AzureTranslator(
    api_key="YOUR_API_KEY",
    region="eastus"
)

# Single translation
english_text = "Welcome to Azure AI services"
spanish = translator.translate_text(english_text, "es")
print(f"Spanish: {spanish}")

# Detect language
detected = translator.detect_language("Hola mundo")
print(f"Detected: {detected['language']} (confidence: {detected['score']})")

# Batch translation
texts = [
    "Hello, how are you?",
    "What is your name?",
    "Welcome to Azure"
]
french_translations = translator.translate_batch(texts, "fr")
for original, translated in zip(texts, french_translations):
    print(f"{original} -> {translated}")
```

**REST API Example - Translator:**

```bash
# Translate text
curl -X POST \
  "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=es" \
  -H "Ocp-Apim-Subscription-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '[{"Text": "Hello, welcome to Azure AI services"}]'

# Response
[
  {
    "translations": [
      {
        "text": "Hola, bienvenido a los servicios de IA de Azure",
        "to": "es"
      }
    ]
  }
]

# Detect language
curl -X POST \
  "https://api.cognitive.microsofttranslator.com/detect?api-version=3.0" \
  -H "Ocp-Apim-Subscription-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '[{"Text": "Bonjour"}]'

# Response
[
  {
    "language": "fr",
    "score": 1.0,
    "isTranslationSupported": true,
    "isTransliterationSupported": false
  }
]
```

---

### Model Selection Guide

| Use Case | Recommended Model | Reasoning |
|----------|-------------------|-----------|
| **General Chat** | GPT-3.5 Turbo | Fast, cost-effective, suitable for most applications |
| **Complex Reasoning** | GPT-4 | Better logic, code generation, and multimodal |
| **Image Generation** | DALL-E 3 | Highest quality, best prompt understanding |
| **Video Content** | Azure Video Gen | Professional quality for marketing/training |
| **Speech Output** | Neural TTS | 400+ voices, emotional expression, multiple languages |
| **Speech Input** | Speech STT | 125+ languages, real-time transcription |
| **Language Translation** | Translator | 130+ language pairs, batch processing |
| **Cost Optimization** | GPT-3.5 Turbo | 10x cheaper than GPT-4 |
| **Real-time Apps** | GPT-3.5 Turbo + Streaming | Low latency responses |
| **Enterprise** | GPT-4 + Custom Models | Fine-tuning for domain expertise |

---

## Certificate Exam Tips

1. **Know the service limits and quotas** for each cognitive service
2. **Understand pricing models** - Per transaction vs. Commitment plans
3. **Master authentication methods** - Key-based vs. Token-based
4. **Practice error handling** - Know common error codes
5. **Understand compliance** - Data privacy and regulatory requirements
6. **Know deployment patterns** - ARM, Bicep, and containerization
7. **Practice with real data** - Build end-to-end solutions
8. **Understand monitoring** - Application Insights integration
9. **Know scaling strategies** - Regions, replicas, and partitions
10. **Understand best practices** - Caching, batching, and optimization

---

## Additional Resources

- [Azure AI Services Documentation](https://learn.microsoft.com/en-us/azure/ai-services/)
- [Azure AI 102 Exam](https://learn.microsoft.com/en-us/certifications/exams/ai-102)
- [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)
- [Azure Samples on GitHub](https://github.com/Azure-Samples)
- [Microsoft Learn AI Learning Path](https://learn.microsoft.com/en-us/training/browse/?roles=ai-engineer)

