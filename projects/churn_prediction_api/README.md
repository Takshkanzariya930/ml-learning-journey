# Customer Churn Prediction API

An end-to-end machine learning application for predicting customer churn using classification models, deployed with FastAPI, Streamlit, Docker, and Render.

---

# Live Demo

API + Streamlit App:

https://churn-prediction-api-g2s5.onrender.com/

---

# Project Overview

This project predicts whether a customer is likely to churn based on account, billing, and service-related information.

The goal was not only to train a model, but also to:

* optimize decision thresholds
* analyze failure patterns
* deploy the model as a usable API
* build a simple frontend for interaction

---

# Features

* Customer churn prediction using machine learning
* Real-time inference through FastAPI
* Interactive frontend using Streamlit
* Dockerized deployment
* Threshold optimization using Precision–Recall analysis
* Error analysis and business-oriented evaluation

---

# Tech Stack

## Machine Learning

* Python
* Pandas
* NumPy
* scikit-learn
* XGBoost

## Backend

* FastAPI
* Pydantic

## Frontend

* Streamlit

## Deployment

* Docker
* Render

---

# Dataset

The project uses a telecom customer churn dataset containing:

* customer demographics
* contract details
* billing information
* internet services
* payment methods

Target variable:

* `Churn Value`

  * 1 → customer churned
  * 0 → customer retained

---

# Data Preparation

Key preprocessing steps:

* removed leakage features
* converted billing columns to numeric
* handled missing values
* encoded categorical variables
* engineered billing-related features

Leakage columns removed:

* `Churn Label`
* `Churn Score`
* `Churn Reason`
* `CLTV`

---

# Models Evaluated

| Model               | Precision | Recall | F1   | ROC-AUC |
| ------------------- | --------- | ------ | ---- | ------- |
| Logistic Regression | 0.64      | 0.60   | 0.62 | 0.843   |
| Random Forest       | 0.64      | 0.52   | 0.57 | 0.826   |
| XGBoost             | 0.63      | 0.56   | 0.59 | 0.843   |

Selected model:

* Logistic Regression

Reason:

* comparable ROC-AUC
* higher recall
* simpler and more interpretable

---

# Threshold Optimization

Default threshold (`0.5`) was not optimal for churn prediction.

Using Precision–Recall analysis, threshold was adjusted to:

```python
threshold = 0.3
```

Result:

* Recall improved significantly
* More churn-risk customers identified
* Acceptable precision tradeoff

---

# API Endpoints

## Root Endpoint

```http
GET /
```

Returns API status.

---

## Prediction Endpoint

```http
POST /predict
```

Example request:

```json
{
  "tenure": 2,
  "monthly_charges": 70,
  "total_charges": 140,
  "contract": "Month-to-month",
  "internet_service": "Fiber optic"
}
```

Example response:

```json
{
  "churn_probability": 0.74,
  "prediction": 1
}
```

---

# Running Locally

## Clone Repository

```bash
git clone https://github.com/Takshkanzariya930/ml-learning-journey/tree/57c6339bd3bff55bf5757df835fcb5761d8fd3f8/projects/credit_default_prediction
cd churn_prediction_api
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run FastAPI

```bash
uvicorn app.main:app --reload
```

## Run Streamlit

```bash
streamlit run frontend.py
```

---

# Docker

Build image:

```bash
docker build -t churn-api .
```

Run container:

```bash
docker run -p 8000:8000 churn-api
```

---

# Key Learnings

This project reinforced several practical ML concepts:

* threshold tuning can matter more than changing models
* error analysis is critical for improvement
* deployment introduces challenges beyond notebook workflows
* evaluation metrics must align with business objectives

---

# Future Improvements

* probability calibration
* automated monitoring
* model versioning
* improved feature engineering
* CI/CD integration

---

# Repository Structure

```text
app/
models/
frontend.py
Dockerfile
requirements.txt
README.md
```

---

# Conclusion

This project combines:

* machine learning
* backend engineering
* deployment workflows

to build a complete end-to-end churn prediction system rather than a notebook-only model.
