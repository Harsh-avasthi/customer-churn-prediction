import streamlit as st
import joblib
import pandas as pd


# Load trained pipeline model
model = joblib.load("churn_model.pkl")


# App Title
st.title("🚀 Customer Churn Prediction System")

st.write("Enter Customer Details")


# Input Features

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)


SeniorCitizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)


Partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)


Dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)


tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    max_value=100,
    value=12
)


PhoneService = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)


MultipleLines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)


InternetService = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)


OnlineSecurity = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)


OnlineBackup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)


DeviceProtection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)


TechSupport = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)


StreamingTV = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)


StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)


Contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)


PaperlessBilling = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)


PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)


MonthlyCharges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)


TotalCharges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)



# Prediction

if st.button("🔮 Predict Churn"):


    input_data = pd.DataFrame({

        "gender": [gender],
        "SeniorCitizen": [SeniorCitizen],
        "Partner": [Partner],
        "Dependents": [Dependents],
        "tenure": [tenure],
        "PhoneService": [PhoneService],
        "MultipleLines": [MultipleLines],
        "InternetService": [InternetService],
        "OnlineSecurity": [OnlineSecurity],
        "OnlineBackup": [OnlineBackup],
        "DeviceProtection": [DeviceProtection],
        "TechSupport": [TechSupport],
        "StreamingTV": [StreamingTV],
        "StreamingMovies": [StreamingMovies],
        "Contract": [Contract],
        "PaperlessBilling": [PaperlessBilling],
        "PaymentMethod": [PaymentMethod],
        "MonthlyCharges": [MonthlyCharges],
        "TotalCharges": [TotalCharges]

    })


    # Prediction through pipeline

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)[0][1]


    st.subheader("📊 Prediction Result")


    if prediction[0] == 1:

        st.error("⚠️ Customer will Churn")

    else:

        st.success("✅ Customer will Stay")


    st.info(
        f"Churn Probability: {round(probability*100,2)}%"
    )


    # Risk Level

    if probability < 0.3:

        risk = "Low Risk 🟢"

    elif probability < 0.7:

        risk = "Medium Risk 🟡"

    else:

        risk = "High Risk 🔴"


    st.write(
        "Customer Risk Level:",
        risk
    )