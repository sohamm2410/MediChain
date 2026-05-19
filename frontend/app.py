import streamlit as st
import pandas as pd
import requests

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="MediChain",
    page_icon="🩺",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- SIDEBAR ----------------

st.sidebar.title("🩺 MediChain")

st.sidebar.markdown("## About")

st.sidebar.info("""
MediChain is a privacy-preserving healthcare AI platform
designed for rare disease detection using:
- NLP
- Machine Learning
- Federated Learning
- Differential Privacy
""")

st.sidebar.markdown("---")

st.sidebar.subheader("System Status")

st.sidebar.success("ML Model Active")
st.sidebar.success("Backend API Connected")
st.sidebar.success("Federated Simulation Ready")

st.sidebar.markdown("---")

hospital = st.sidebar.selectbox(
    "Select Hospital",
    [
        "Hospital A",
        "Hospital B",
        "Hospital C"
    ]
)

# ---------------- TITLE ----------------

st.title("🩺 MediChain")

st.subheader(
    "Privacy-Preserving Healthcare AI Platform"
)

# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Hospitals Connected",
    "3"
)

col2.metric(
    "Models Running",
    "1"
)

col3.metric(
    "Predictions Made",
    len(st.session_state.history)
)

# ---------------- ABOUT EXPANDER ----------------

with st.expander("About MediChain"):

    st.write("""
    MediChain is an AI-powered healthcare platform
    for clinical note analysis and disease prediction.

    Current Features:
    - NLP-based disease prediction
    - Confidence score analysis
    - Healthcare analytics dashboard
    - FastAPI backend integration

    Upcoming Features:
    - Federated Learning
    - Differential Privacy
    - BioBERT Integration
    """)

# ---------------- INPUT SECTION ----------------

st.markdown("---")

st.subheader("Clinical Note Analysis")

clinical_note = st.text_area(
    "Enter Clinical Note",
    placeholder="Example: Patient reports chest pain and shortness of breath...",
    height=180
)

# ---------------- PREDICTION BUTTON ----------------

if st.button("Predict Disease"):

    if clinical_note.strip() == "":

        st.warning("Please enter a clinical note.")

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

            # Save prediction history
            st.session_state.history.append({

                "Hospital": hospital,
                "Clinical Note": clinical_note,
                "Prediction": prediction,
                "Confidence": confidence

            })

            # ---------------- RESULT SECTION ----------------

            st.success("Prediction Completed Successfully")

            st.markdown("---")

            st.subheader("Prediction Result")

            result_col1, result_col2 = st.columns(2)

            with result_col1:

                st.info(
                    f"Predicted Disease: {prediction}"
                )

            with result_col2:

                st.info(
                    f"Confidence Score: {confidence:.2f}%"
                )

            st.progress(min(int(confidence), 100))

        except Exception as e:

            st.error("Backend API connection failed.")

            st.code(str(e))

# ---------------- HISTORY SECTION ----------------

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

# ---------------- ANALYTICS SECTION ----------------

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

# ---------------- CLEAR BUTTON ----------------

st.markdown("---")

if st.button("Clear Prediction History"):

    st.session_state.history = []

    st.success("Prediction history cleared.")

# ---------------- FOOTER ----------------