from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os

# Add parent directory to path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from models.utils import predict_disease

# Create FastAPI app
app = FastAPI()

# Request schema
class ClinicalNote(BaseModel):
    note: str

# Root endpoint
@app.get("/")
def home():

    return {
        "message": "MediChain API Running Successfully"
    }

# Prediction endpoint
@app.post("/predict")
def predict(note_data: ClinicalNote):

    prediction, confidence = predict_disease(note_data.note)

    return {

        "clinical_note": note_data.note,
        "prediction": prediction,
        "confidence": round(confidence, 2)

    }