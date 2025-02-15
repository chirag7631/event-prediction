from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained XGBoost model
model = joblib.load("alert_prediction_xgboost.pkl")

# Define router
router = APIRouter()

# Define request body structure
class AlertRequest(BaseModel):
    message_key: str
    description: str

# API endpoint for XGBoost Alert Prediction
@router.post("/predict")
def predict_alert(request: AlertRequest):
    # Convert input to DataFrame
    input_data = pd.DataFrame([{
        "message key": request.message_key,
        "description": request.description
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]  # Get first prediction

    # Return response
    return {"alert_created": int(prediction)}  # Convert to int (0 or 1)
