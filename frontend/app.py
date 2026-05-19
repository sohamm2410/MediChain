import streamlit as st
import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from models.utils import predict_disease

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="MediChain",
    page_icon="🩺",
    layout="centered"
)

# ---------------- SESSION STATE ----------------

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- SIDEBAR ----------------

st.sidebar.title("About")

st.sidebar.info("""
MediChain is a privacy-preserving healthcare AI platform
designed for rare disease detection using NLP,
Federated Learning, and Differential Privacy.
""")

st.sidebar.markdown("---")

st.sidebar.subheader("System Status")

st.sidebar.success("Model Active")
st.sidebar.success("Federated Server Simulated")
st.sidebar.success("Privacy Layer Ready")

# ---------------- MAIN TITLE ----------------

st.title("🩺 MediChain")

st.subheader("Privacy-Preserving Healthcare AI Platform")

# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

col1.metric("Models Loaded", "1")
col2.metric("Hospitals Connected", "3")
col3.metric("Predictions Today", len(st.session_state.history))

# ---------------- ABOUT SECTION ----------------

with st.expander("About MediChain"):

    st.write("""
    MediChain is an AI-powered healthcare platform designed
    for clinical note analysis and disease prediction using
    Natural Language Processing (NLP).

    Future versions will include:
    - Federated Learning
    - Differential Privacy
    - BioBERT Integration
    - Multi-Hospital AI Training
    """)

# ---------------- HOSPITAL SELECTOR ----------------

hospital = st.selectbox(
    "Select Hospital",
    [
        "Hospital A",
        "Hospital B",
        "Hospital C"
    ]
)

# ---------------- DESCRIPTION ----------------

st.write("""
Analyze clinical notes using Machine Learning and NLP.
""")

# ---------------- TEXT INPUT ----------------

clinical_note = st.text_area(
    "Enter Clinical Note",
    height=150
)

# ---------------- PREDICTION BUTTON ----------------

if st.button("Predict Disease"):

    if clinical_note.strip() == "":

        st.warning("Please enter a clinical note.")

    else:

        prediction, confidence = predict_disease(clinical_note)

        # Save prediction history
        st.session_state.history.append({

            "Hospital": hospital,
            "Clinical Note": clinical_note,
            "Prediction": prediction,
            "Confidence": round(confidence, 2)

        })

        st.success("Prediction Complete")

        st.markdown("## Prediction Result")

        st.write(
            f"### Predicted Disease Category: `{prediction}`"
        )

        st.write(
            f"### Confidence Score: `{confidence:.2f}%`"
        )

        # Progress Bar
        st.progress(min(int(confidence), 100))

# ---------------- PREDICTION HISTORY ----------------

if len(st.session_state.history) > 0:

    st.markdown("---")

    st.subheader("Prediction History")

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

# ---------------- ANALYTICS ----------------

if len(st.session_state.history) > 0:

    st.markdown("---")

    st.subheader("Prediction Analytics")

    analytics_df = pd.DataFrame(
        st.session_state.history
    )

    disease_counts = analytics_df[
        "Prediction"
    ].value_counts()

    st.bar_chart(disease_counts)

# ---------------- CLEAR HISTORY ----------------

if st.button("Clear Prediction History"):

    st.session_state.history = []

    st.success("History Cleared")

