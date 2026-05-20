from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import logging
import sys
import os

# ---------------- PATH SETUP ----------------

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from models.utils import predict_disease

# ---------------- LOGGING SETUP ----------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- FASTAPI APP ----------------

app = FastAPI(

    title="MediChain API",

    description="""
    Privacy-Preserving Healthcare AI API
    for Clinical Note Disease Prediction
    """,

    version="1.0.0"
)

# ---------------- REQUEST MODEL ----------------

class ClinicalNote(BaseModel):

    note: str

# ---------------- ROOT ENDPOINT ----------------

@app.get("/")
def home():

    logging.info("Home endpoint accessed")

    return {

        "message": "MediChain API Running Successfully",
        "status": "active",
        "timestamp": str(datetime.now())

    }

# ---------------- HEALTH CHECK ----------------

@app.get("/health")
def health_check():

    logging.info("Health check endpoint accessed")

    return {

        "system": "healthy",
        "model_status": "loaded",
        "api_status": "running"

    }

# ---------------- PREDICTION ENDPOINT ----------------

@app.post("/predict")
def predict(note_data: ClinicalNote):

    try:

        # Input validation
        if note_data.note.strip() == "":

            logging.warning("Empty clinical note received")

            raise HTTPException(

                status_code=400,

                detail="Clinical note cannot be empty"

            )

        # Generate prediction
        prediction, confidence = predict_disease(
            note_data.note
        )

        logging.info(
            f"Prediction generated: {prediction}"
        )

        # Response
        return {

            "clinical_note": note_data.note,

            "prediction": prediction,

            "confidence": round(confidence, 2),

            "hospital_ai_status": "active",

            "privacy_layer": "enabled",

            "timestamp": str(datetime.now())

        }

    except Exception as e:

        logging.error(f"Prediction Error: {str(e)}")

        raise HTTPException(

            status_code=500,

            detail=f"Internal Server Error: {str(e)}"

        )