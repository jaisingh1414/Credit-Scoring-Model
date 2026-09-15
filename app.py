import streamlit as st
import joblib
import pandas as pd


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Credit Risk Predictor",
    page_icon="💳",
    layout="wide"
)


# -----------------------------
# Load Model
# -----------------------------

model = joblib.load("models/credit_risk_model_compressed.pkl")


# -----------------------------
# Title
# -----------------------------

st.title("💳 Credit Risk Prediction System")

st.write(
    "Enter the applicant's financial and personal information "
    "to predict their credit risk."
)

st.divider()


# -----------------------------
# Input Section
# -----------------------------

st.subheader("📋 Applicant Information")

col1, col2 = st.columns(2)


# Left column
with col1:

    person_age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

    person_income = st.number_input(
        "Annual Income",
        min_value=0,
        value=60000
    )

    person_emp_length = st.number_input(
        "Employment Length (years)",
        min_value=0.0,
        max_value=50.0,
        value=5.0
    )

    loan_amnt = st.number_input(
        "Loan Amount",
        min_value=0,
        value=5000
    )

    loan_int_rate = st.number_input(
        "Interest Rate (%)",
        min_value=0.0,
        max_value=30.0,
        value=8.0
    )

    loan_percent_income = st.number_input(
        "Loan Percent of Income",
        min_value=0.0,
        max_value=1.0,
        value=0.08
    )


# Right column
with col2:

    cb_person_cred_hist_length = st.number_input(
        "Credit History Length (years)",
        min_value=0,
        max_value=30,
        value=6
    )

    person_home_ownership = st.selectbox(
        "Home Ownership",
        ["RENT", "OWN", "MORTGAGE", "OTHER"]
    )

    loan_intent = st.selectbox(
        "Loan Intent",
        [
            "PERSONAL",
            "EDUCATION",
            "MEDICAL",
            "VENTURE",
            "HOMEIMPROVEMENT",
            "DEBTCONSOLIDATION"
        ]
    )

    loan_grade = st.selectbox(
        "Loan Grade",
        ["A", "B", "C", "D", "E", "F", "G"]
    )

    cb_person_default_on_file = st.selectbox(
        "Previous Default on File",
        ["N", "Y"]
    )


st.divider()


# -----------------------------
# Create Input DataFrame
# -----------------------------

input_data = pd.DataFrame({
    "person_age": [person_age],
    "person_income": [person_income],
    "person_home_ownership": [person_home_ownership],
    "person_emp_length": [person_emp_length],
    "loan_intent": [loan_intent],
    "loan_grade": [loan_grade],
    "loan_amnt": [loan_amnt],
    "loan_int_rate": [loan_int_rate],
    "loan_percent_income": [loan_percent_income],
    "cb_person_default_on_file": [cb_person_default_on_file],
    "cb_person_cred_hist_length": [cb_person_cred_hist_length]
})


# -----------------------------
# Prediction
# -----------------------------

if st.button("🔍 Predict Credit Risk", use_container_width=True):

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.divider()

    st.subheader("📊 Prediction Result")

    if prediction == 1:

        st.error("⚠️ HIGH CREDIT RISK")

    else:

        st.success("✅ LOW CREDIT RISK")

    st.metric(
        "Default Probability",
        f"{probability:.2%}"
    )

    st.progress(float(probability))


# -----------------------------
# Disclaimer
# -----------------------------

st.divider()

st.caption(
    "⚠️ This application is an educational machine-learning project. "
    "Predictions should not be used as the sole basis for real financial decisions."
)