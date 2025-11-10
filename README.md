    
# DevOps Implementation for Predictive Recall Management System

## Project Overview
RecallRiskPredictor is an AI-driven predictive recall platform for the automotive industry. It predicts vehicles at high risk of recall by analyzing manufacturing data and global component failure insights.  

This repository contains the complete DevOps setup for the system, including Docker, Kubernetes deployments, CI/CD pipelines, monitoring, and alerting.

---

## Repository Structure

```

.
├── .github/workflows/       # CI/CD GitHub Actions pipelines
├── Dockerfile               # Docker build for API
├── requirements.txt         # Python dependencies
├── app.py                   # Flask API code
├── train_model.py           # Model training script
├── recall_risk_model.pkl    # Trained recall prediction model
├── deployment.yaml          # Kubernetes deployment files
├── service.yaml             # Kubernetes services
├── prometheus-values.yaml   # Prometheus configuration
├── grafana-nodeport.yaml    # Grafana deployment
├── alert.rules.yaml         # Prometheus alert rules
├── nodeport-service.yaml    # NodePort services
├── retrain-cron.yaml        # CronJobs for model retraining
├── api_tests.py             # API test scripts
├── vehicle_data.csv         # Sample dataset
└── README.md                # Project documentation


---

## Installation & Setup

### Prerequisites
- Docker  
- Kubernetes (Minikube or Cloud)  
- Python 3.x  
- Git  

### Steps

1. Clone the Repository
   bash
git clone https://github.com/Lalithya15/devops-intern.git
cd devops-intern


2. Build Docker Image

   bash
docker build -t recallrisk-api .


3.  Locally (Optional)

  bash
docker run -p 5000:5000 recallrisk-api


4. Deploy on Kubernetes

  bash
kubectl apply -f recallrisk-deployment.yaml
kubectl apply -f recallrisk-service.yaml
kubectl apply -f nodeport-service.yaml
kubectl apply -f grafana-nodeport.yaml
kubectl apply -f prometheus-values.yaml
kubectl apply -f alert.rules.yaml
kubectl apply -f retrain-cron.yaml


5. Access the API

  bash
curl http:localhost:5000


6. Monitoring Dashboards

Prometheus:http://localhost:9090
Grafana:http://localhost:3000



## Running Tests

  bash
python api_tests.py
python test_api.py


Tests validate API endpoints and model predictions.

---

## CI/CD

* Automated pipelines are configured in .github/workflows/ci-cd.yaml
* Pipeline steps:

  * Build Docker image
  * Run API tests
  * Deploy to Kubernetes
  * Trigger model retraining CronJobs






