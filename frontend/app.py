import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
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

from models.entity_extractor import extract_symptoms
from models.clinical_reasoning import generate_observation

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="MediChain",
    page_icon="🏥",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- SIDEBAR ----------------

st.sidebar.title("MediChain")

st.sidebar.success("Healthcare AI Active")
st.sidebar.success("Federated Learning Enabled")
st.sidebar.success("Differential Privacy Enabled")
st.sidebar.success("Clinical Intelligence Enabled")

hospital = st.sidebar.selectbox(
    "Select Hospital",
    [
        "Hospital A",
        "Hospital B",
        "Hospital C"
    ]
)

# ---------------- HEADER ----------------

st.title("🏥 MediChain")
st.subheader(
    "Privacy-Preserving Healthcare AI Platform"
)

# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Active Hospitals",
        "3"
    )

with col2:
    st.metric(
        "Privacy Status",
        "Enabled"
    )

with col3:
    st.metric(
        "Privacy Budget (ε)",
        "0.5"
    )

st.divider()

# ---------------- INPUT ----------------

clinical_note = st.text_area(
    "Enter Clinical Note",
    height=150,
    placeholder="Patient reports chest pain and shortness of breath..."
)

predict_button = st.button(
    "Predict Disease"
)

# ---------------- PREDICTION ----------------

if predict_button:

    if clinical_note.strip() == "":

        st.error(
            "Please enter a clinical note."
        )

    else:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={
                    "note": clinical_note
                }
            )

            result = response.json()

            prediction = result["prediction"]
            confidence = result["confidence"]

            # ---------------- PREDICTION RESULT ----------------

            st.subheader(
                "Prediction Result"
            )

            st.success(
                f"Predicted Disease Category: {prediction}"
            )

            st.write(
                f"Confidence Score: {confidence:.2f}%"
            )

            st.progress(
                min(
                    int(confidence),
                    100
                )
            )

            # ---------------- SYMPTOM EXTRACTION ----------------

            symptoms = extract_symptoms(
                clinical_note
            )

            st.subheader(
                "Detected Symptoms"
            )

            if symptoms:

                for symptom in symptoms:

                    st.success(symptom)

            else:

                st.info(
                    "No symptoms detected."
                )

            # ---------------- AI OBSERVATION ----------------

            observation = generate_observation(
                symptoms
            )

            st.subheader(
                "AI Observation"
            )

            st.warning(
                observation
            )

            # ---------------- HISTORY ----------------

            st.session_state.history.append(
                {
                    "Timestamp": str(
                        datetime.now()
                    )[:19],
                    "Hospital": hospital,
                    "Prediction": prediction,
                    "Confidence": confidence
                }
            )

        except Exception as e:

            st.error(
                f"Backend Error: {str(e)}"
            )

# ---------------- HISTORY ----------------

if st.session_state.history:

    st.divider()

    st.subheader(
        "Prediction History"
    )

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

    # ---------------- ANALYTICS ----------------

    st.subheader(
        "Prediction Analytics"
    )

    prediction_counts = (
        history_df["Prediction"]
        .value_counts()
        .reset_index()
    )

    prediction_counts.columns = [
        "Prediction",
        "Count"
    ]

    fig = px.bar(
        prediction_counts,
        x="Prediction",
        y="Count",
        title="Disease Prediction Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ---------------- CLEAR HISTORY ----------------

    if st.button(
        "Clear Prediction History"
    ):
        st.session_state.history = []
        st.rerun()