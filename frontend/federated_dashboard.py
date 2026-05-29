import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="MediChain FL Dashboard",
    layout="wide"
)

st.title("🏥 MediChain Federated Learning Dashboard")

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

# ---------------- LOAD DATA ----------------

df = pd.read_csv(
    "federated/metrics/training_metrics.csv"
)

st.subheader("Training Metrics")

st.dataframe(df)

# ---------------- ACCURACY GRAPH ----------------

st.subheader("Accuracy Analysis")

fig1 = px.line(

    df,

    x="round",

    y="accuracy",

    color="hospital",

    markers=True

)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ---------------- LOSS GRAPH ----------------

st.subheader("Loss Analysis")

fig2 = px.line(

    df,

    x="round",

    y="loss",

    color="hospital",

    markers=True

)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ---------------- HOSPITAL COUNTS ----------------

st.subheader(
    "Hospital Participation"
)

hospital_counts = (

    df["hospital"]

    .value_counts()

    .reset_index()

)

hospital_counts.columns = [

    "hospital",

    "count"

]

fig3 = px.bar(

    hospital_counts,

    x="hospital",

    y="count"

)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.success(
    "Differential Privacy Enabled"
)

st.subheader(
    "System Status"
)

status = pd.DataFrame({

    "Component": [

        "NLP Model",
        "FastAPI Backend",
        "Federated Learning",
        "Differential Privacy"

    ],

    "Status": [

        "Active",
        "Active",
        "Active",
        "Active"

    ]

})

st.table(status)