# 🚀 Sentiment Analysis API & Docker Deployment

This project demonstrates the deployment of a trained Deep Learning Sentiment Analysis model as a REST API using **Flask** and **Docker**.

The API accepts a movie review as input and predicts whether the sentiment is **Positive** or **Negative**, along with the prediction confidence.

---

## 📌 Project Overview

The trained sentiment analysis model was developed using Deep Learning and saved as a Keras model.

For deployment, the model and tokenizer are integrated into a Flask API. The application is then containerized using Docker, making it easy to run the API in a consistent environment.

### Technologies Used

- Python
- TensorFlow / Keras
- Flask
- Docker
- GitHub
- Git LFS

---

## ✨ Features

- 🧠 Deep Learning-based sentiment classification
- 🌐 REST API using Flask
- 📩 Accepts text reviews through a POST request
- 📊 Predicts Positive or Negative sentiment
- 📈 Returns prediction confidence
- 🐳 Docker containerization
- 💾 Large trained model stored using Git LFS

---

## 📂 Project Structure

```text
Alfido-Tech-Internship-TASK3/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── sentiment_model.keras
├── tokenizer.pkl
├── .dockerignore
├── .gitattributes
└── README.md
```
## File Description

File	                 Description
app.py	               Flask API application for sentiment prediction
Dockerfile	           Instructions for building the Docker image
requirements.txt	     Required Python dependencies
sentiment_model.keras	 Trained Deep Learning sentiment analysis model
tokenizer.pkl	         Saved tokenizer used to preprocess text
.dockerignore	         Files excluded from the Docker image
.gitattributes	       Git LFS configuration for the model file
README.md	             Project documentation
## 🚀 How to Run the Project
### 1. Clone the Repository

Clone the GitHub repository:
```bash
git clone https://github.com/BHAVANA-132/Alfido-Tech-Internship-TASK3.git
```
Navigate to the project folder:
```bash
cd Alfido-Tech-Internship-TASK3
```
## 🐳 Run Using Docker
### 2. Build the Docker Image

Make sure Docker Desktop is installed and running.

Build the Docker image using:
```bash
docker build -t sentiment-api .
```
### 3. Run the Docker Container

Run the container using:
```bash
docker run -p 5000:5000 sentiment-api
```
The Flask API will now be available at:
```bash
http://localhost:5000
```
## 🌐 API Usage
### Home Endpoint

Open the following URL in your browser:
```bash
http://localhost:5000
```
### Response
```
{
    "endpoint": "/predict",
    "message": "Sentiment Analysis API is running!"
}
```
## 🔮 Sentiment Prediction

The /predict endpoint accepts a movie review and returns the predicted sentiment and confidence.

### Endpoint
```bash
POST /predict
```
### Request Format

Send a JSON request containing a review field.
```bash
{
    "review": "This movie was absolutely fantastic! I loved every moment of it."
}
```
## 🧪 Testing the API
### Using PowerShell

Run the following command:
```bash
Invoke-RestMethod -Uri http://localhost:5000/predict -Method Post -ContentType "application/json" -Body '{"review":"This movie was absolutely fantastic! I loved every moment of it."}'
```
### Example Response
```
review     : This movie was absolutely fantastic! I loved every moment of it.
sentiment  : Positive
confidence : 74.54
```
### Example Prediction
```
Review:

This movie was absolutely fantastic! I loved every moment of it.

Predicted Sentiment: Positive

Confidence: 74.54%
```

## 📊 API Workflow
```
User Input
    │
    ▼
Flask REST API
    │
    ▼
Text Preprocessing
    │
    ▼
Tokenizer
    │
    ▼
Deep Learning Model
    │
    ▼
Sentiment Prediction
    │
    ▼
Positive / Negative
    │
    ▼
Confidence Score
```
## 🐳 Docker Workflow
```
Application Files
       │
       ▼
Dockerfile
       │
       ▼
Docker Build
       │
       ▼
sentiment-api Image
       │
       ▼
Docker Container
       │
       ▼
Flask API
       │
       ▼
http://localhost:5000
```
## 📸 Demo

The deployed API was tested successfully using Docker.

### Sample Prediction
```
Review:
This movie was absolutely fantastic! I loved every moment of it.

Sentiment:
Positive

Confidence:
74.54%
```

## 📦 Model Files

The following files are required for the API to work:

sentiment_model.keras

This is the trained Deep Learning model used for sentiment classification.

tokenizer.pkl

This file contains the saved tokenizer used to convert text reviews into sequences that can be processed by the trained model.

The model file is managed using Git Large File Storage (Git LFS).

## 🛠️ Requirements
Python 3.12
Docker Desktop
Git
Git LFS

## 🎯 Project Outcome

This project successfully demonstrates how to:

Deploy a trained Deep Learning model as a REST API
Create an inference endpoint using Flask
Containerize a Machine Learning application using Docker
Build and run a Docker image
Test model predictions through an API
Store a large Machine Learning model in GitHub using Git LFS

## 👩‍💻 Author

PALLA BHAVANA

GitHub:
https://github.com/BHAVANA-132

## ⭐ Conclusion

The Sentiment Analysis model has been successfully deployed as a Flask REST API and containerized using Docker. The API can receive movie reviews and return sentiment predictions with confidence scores.
