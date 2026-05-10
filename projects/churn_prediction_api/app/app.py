from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib
from model.models import UserInput, APIOutput
import pandas as pd

model = joblib.load("model/churn_model.joblib")

app = FastAPI()

@app.get("/")
def home():
  return {"message": "Churn Prediction API"}

@app.get("/health")
def health_check():
  return {
    "status": "OK",
  }

@app.post("/predict", response_model=APIOutput)
def PredictChurn(data: UserInput):
    
    input_df = pd.DataFrame({'Gender': [data.Gender],
                    'Senior Citizen': [data.Senior_Citizen],
                    'Partner': [data.Partner],
                    'Dependents': [data.Dependents],
                    'Tenure Months' : [data.Tenure_Months],
                    'Phone Service': [data.Phone_Service],
                    'Multiple Lines': [data.Multiple_Lines],
                    'Internet Service': [data.Internet_Service],
                    'Online Security': [data.Online_Security],
                    'Online Backup': [data.Online_Backup],
                    'Device Protection': [data.Device_Protection],
                    'Tech Support': [data.Tech_Support],
                    'Streaming TV': [data.Streaming_TV],
                    'Streaming Movies': [data.Streaming_Movies],
                    'Contract': [data.Contract],
                    'Paperless Billing': [data.Paperless_Billing],
                    'Payment Method': [data.Payment_Method],
                    'Monthly Charges': [data.Monthly_Charges],
                    'Total Charges': [data.Total_Charges]
                })
    
    prediction = model.predict(input_df)[0]
    prediction_probability = model.predict_proba(input_df)
    
    if prediction == 0:
      prediction = "No-Churn"
      prediction_probability = prediction_probability[0, 0]
    else:
      prediction = "Churn"
      prediction_probability = prediction_probability[0, 1]
    
    return {"Prediction" : prediction, "Confidence": prediction_probability}