import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.utils import predict_disease


# Page configuration
st.set_page_config(
    page_title="MediChain",
    page_icon="🩺",
    layout="centered"
)

# Title
st.title("🩺 MediChain")
st.subheader("Privacy-Preserving Healthcare AI Platform")

# Description
st.write("""
Analyze clinical notes using Machine Learning and NLP.
""")

# Text input
clinical_note = st.text_area(
    "Enter Clinical Note",
    height=150
)

# Predict button
if st.button("Predict Disease"):

    if clinical_note.strip() == "":
        st.warning("Please enter a clinical note.")

    else:

        prediction, confidence = predict_disease(clinical_note)

        st.success("Prediction Complete")

        st.markdown("## Prediction Result")

        st.write(f"### Predicted Disease Category: `{prediction}`")

        st.write(f"### Confidence Score: `{confidence:.2f}%`")

        # Confidence progress bar
        st.progress(min(int(confidence), 100))