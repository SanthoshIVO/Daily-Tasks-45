from fastapi import APIRouter, HTTPException
from schemas import InsuranceRequest, InsuranceResponse
import joblib
import pandas as pd

router = APIRouter(prefix="/insurance", tags=["ML Insurance"])

# Global variables to hold the loaded model and preprocessor
model = None
preprocessor = None

def load_assets():
    global model, preprocessor
    model = joblib.load('D:/pysp1/Notes/FastAPI/files/projects/ai_portfolio/models/insurance_model.joblib')
    preprocessor = joblib.load('D:/pysp1/Notes/FastAPI/files/projects/ai_portfolio/models/preprocessor.joblib')

@router.post("/predict", response_model=InsuranceResponse)
def predict_charges(data: InsuranceRequest):
    if model is None or preprocessor is None:
        raise HTTPException(status_code=503, detail="Model not loaded yet")
    
    # Convert input to DataFrame
    df = pd.DataFrame([data.model_dump()])
    
    # Preprocess and Predict
    processed_data = preprocessor.transform(df)
    prediction = model.predict(processed_data)[0]
    
    return InsuranceResponse(predicted_charges=float(prediction))
