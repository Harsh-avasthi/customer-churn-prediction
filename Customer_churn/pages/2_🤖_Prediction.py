# ==========================================================
# Customer Churn Prediction Platform v3.0
# Prediction Page - Fixed Version
# ==========================================================

import streamlit as st
import pandas as pd
import sys
import os

from utils import (
    predict_customer,
    risk_level,
    recommendation
)

from charts import probability_gauge

# ----------------------------------------------------------
# Page Config
# ----------------------------------------------------------

st.set_page_config(
    page_title="Customer Prediction",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------------------------------
# Load CSS
# ----------------------------------------------------------

try:
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except FileNotFoundError:
    pass

# ----------------------------------------------------------
# Header
# ----------------------------------------------------------

st.title("🤖 Customer Churn Prediction")

st.caption(
    "Predict whether a customer is likely to churn using the trained Machine Learning model."
)

st.markdown("---")

# ----------------------------------------------------------
# Customer Information
# ----------------------------------------------------------

st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)

# ==========================================================
# COLUMN 1
# ==========================================================

with col1:

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

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

# ==========================================================
# COLUMN 2
# ==========================================================

with col2:

    PhoneService = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    MultipleLines = st.selectbox(
        "Multiple Lines",
        [
            "Yes",
            "No",
            "No phone service"
        ]
    )

    InternetService = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    OnlineSecurity = st.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    OnlineBackup = st.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

# ==========================================================
# COLUMN 3
# ==========================================================

with col3:

    DeviceProtection = st.selectbox(
        "Device Protection",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    TechSupport = st.selectbox(
        "Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    StreamingTV = st.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    StreamingMovies = st.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    Contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

# ----------------------------------------------------------
# Billing Information
# ----------------------------------------------------------

st.markdown("---")

st.subheader("💳 Billing Information")

left, right = st.columns(2)

with left:

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

with right:

    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=500.0,
        value=70.0,
        step=0.5
    )

    TotalCharges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=100000.0,
        value=1000.0,
        step=10.0
    )

st.markdown("---")

# ----------------------------------------------------------
# Predict Button
# ----------------------------------------------------------

predict_btn = st.button(
    "🚀 Predict Customer",
    use_container_width=True
)

# ==========================================================
# Prediction Logic
# ==========================================================

if predict_btn:

    # DataFrame creation with exact names and types matching training data
    input_df = pd.DataFrame({
        "gender": [str(gender)],
        "SeniorCitizen": [int(SeniorCitizen)],
        "Partner": [str(Partner)],
        "Dependents": [str(Dependents)],
        "tenure": [int(tenure)],
        "PhoneService": [str(PhoneService)],
        "MultipleLines": [str(MultipleLines)],
        "InternetService": [str(InternetService)],
        "OnlineSecurity": [str(OnlineSecurity)],
        "OnlineBackup": [str(OnlineBackup)],
        "DeviceProtection": [str(DeviceProtection)],
        "TechSupport": [str(TechSupport)],
        "StreamingTV": [str(StreamingTV)],
        "StreamingMovies": [str(StreamingMovies)],
        "Contract": [str(Contract)],
        "PaperlessBilling": [str(PaperlessBilling)],
        "PaymentMethod": [str(PaymentMethod)],
        "MonthlyCharges": [float(MonthlyCharges)],
        "TotalCharges": [float(TotalCharges)]
    })

    try:
        with st.spinner("🔄 AI is analyzing customer data..."):
            pred, prob = predict_customer(input_df)

        st.success("✅ Prediction Completed Successfully")

        # ======================================================
        # KPI Cards
        # ======================================================

        st.markdown("---")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Prediction",
                "🚨 Churn" if pred == 1 else "✅ Stay"
            )

        with c2:
            st.metric(
                "Probability",
                f"{prob*100:.2f}%"
            )

        with c3:
            st.metric(
                "Risk Level",
                risk_level(prob)
            )

        # ======================================================
        # Customer Summary
        # ======================================================

        st.markdown("---")

        st.subheader("👤 Customer Summary")

        s1, s2, s3 = st.columns(3)

        with s1:
            st.info(f"""
**Gender**

{gender}

**Senior Citizen**

{SeniorCitizen}

**Partner**

{Partner}
""")

        with s2:
            st.info(f"""
**Internet**

{InternetService}

**Contract**

{Contract}

**Payment**

{PaymentMethod}
""")

        with s3:
            st.info(f"""
**Tenure**

{tenure} Months

**Monthly**

₹ {MonthlyCharges:.2f}

**Total**

₹ {TotalCharges:.2f}
""")

        # ======================================================
        # Gauge Chart
        # ======================================================

        st.markdown("---")

        st.subheader("📊 Churn Probability")

        try:
            st.plotly_chart(
                probability_gauge(prob),
                use_container_width=True
            )
        except Exception:
            pass

        # ======================================================
        # Risk Score
        # ======================================================

        st.subheader("📈 Risk Score")

        st.progress(float(prob))

        st.write(f"**{prob*100:.2f}%**")

        # ======================================================
        # Risk Status
        # ======================================================

        st.markdown("---")

        if prob < 0.30:
            st.success(f"""
### 🟢 LOW RISK

Probability : {prob*100:.2f}%

Customer is expected to stay.
""")

        elif prob < 0.70:
            st.warning(f"""
### 🟡 MEDIUM RISK

Probability : {prob*100:.2f}%

Customer requires attention.
""")

        else:
            st.error(f"""
### 🔴 HIGH RISK

Probability : {prob*100:.2f}%

Customer is likely to churn.
""")

        # ======================================================
        # AI Recommendation
        # ======================================================

        st.markdown("---")

        st.subheader("🤖 AI Retention Strategy")

        if prob < 0.30:
            st.success("""
### 🟢 Recommended Actions

✅ Continue Current Services

🎁 Loyalty Rewards

📧 Thank You Email

⭐ Upsell Premium Plan

💳 Cross Sell Services
""")

        elif prob < 0.70:
            st.warning("""
### 🟡 Recommended Actions

💰 Offer 10% Discount

📞 Contact Customer

🛠 Improve Service

📄 Recommend Annual Plan

🎁 Personalized Offers
""")

        else:
            st.error("""
### 🔴 Recommended Actions

🚨 Immediate Retention Call

💸 Offer 20% Discount

🛡 Premium Support

👨‍💼 Relationship Manager

📅 Long Term Contract
""")

        # ======================================================
        # Business Recommendation
        # ======================================================

        st.markdown("---")

        st.subheader("💼 Business Recommendation")

        st.info(recommendation(prob))

        # ======================================================
        # Prediction History
        # ======================================================

        st.markdown("---")

        history = pd.DataFrame({
            "Prediction": [
                "Churn" if pred == 1 else "Stay"
            ],
            "Probability": [
                round(prob*100, 2)
            ],
            "Risk": [
                risk_level(prob)
            ]
        })

        st.subheader("📋 Prediction History")

        st.dataframe(
            history,
            use_container_width=True
        )

        # ======================================================
        # Download Result
        # ======================================================

        csv = history.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Prediction",
            data=csv,
            file_name="prediction_result.csv",
            mime="text/csv",
            use_container_width=True
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")
