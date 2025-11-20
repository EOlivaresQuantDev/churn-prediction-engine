import pandas as pd
import joblib
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. Initialize FastAPI App
app = FastAPI(
    title="Churn Prediction Engine",
    description="API to predict customer churn based on purchase behavior",
    version="1.0.0"
)

# 2. Define the Input Data Schema (Validation)
# This must match the columns your model expects!
class CustomerInput(BaseModel):
    frequency: int
    monetary_value: float
    avg_days_between_orders: float

# 3. Load the Model at Startup
# We need to find the path relative to this file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'churn_model.pkl')

try:
    model = joblib.load(MODEL_PATH)
    print(f"✅ Model loaded successfully from: {MODEL_PATH}")
except FileNotFoundError:
    print("❌ Error: Model file not found. Run Phase 4 first.")
    model = None

# 4. Define Endpoints

@app.get("/")
def home():
    """Health Check Endpoint"""
    return {"status": "online", "message": "Churn Prediction API is running! 🚀"}

@app.post("/predict")
def predict_churn(data: CustomerInput):
    """
    Receives customer data and returns churn probability.
    """
    if not model:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    # Convert input data (JSON) to DataFrame (what the model expects)
    input_df = pd.DataFrame([data.dict()])
    
    # Make Prediction
    # probability returns [prob_class_0, prob_class_1]
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1] # Probability of Churn (Class 1)
    
    # Human readable response
    result = "Churn (Risk)" if prediction == 1 else "Active (Safe)"
    
    return {
        "prediction": int(prediction),
        "probability_churn": round(float(probability), 4),
        "status": result,
        "input_received": data
    }
