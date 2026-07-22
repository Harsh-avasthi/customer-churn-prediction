import streamlit as st

# ---------------------------------------
# Page Config
# ---------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# ---------------------------------------
# Load CSS
# ---------------------------------------

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------------------------------
# Header
# ---------------------------------------

st.title("ℹ️ About Customer Churn Prediction Platform")

st.caption("Industry-Level Machine Learning Project")

st.markdown("---")

# ======================================
# Project Overview
# ======================================

st.subheader("🚀 Project Overview")

st.info("""

Customer Churn Prediction Platform is an AI-powered application that helps telecom companies identify customers who are likely to leave the company.

The platform predicts customer churn using a trained Machine Learning model and provides actionable business recommendations to improve customer retention.

""")

st.markdown("---")

# ======================================
# Project Workflow
# ======================================

st.subheader("⚙️ Project Workflow")

st.success("""

1️⃣ Customer Data Collection

⬇

2️⃣ Data Cleaning & Preprocessing

⬇

3️⃣ Feature Engineering

⬇

4️⃣ Machine Learning Model Training

⬇

5️⃣ Model Evaluation

⬇

6️⃣ Customer Prediction

⬇

7️⃣ Business Recommendation

⬇

8️⃣ Customer Retention Strategy

""")

st.markdown("---")

# ======================================
# Technologies
# ======================================

st.subheader("🛠 Technologies Used")

tech = {
    "Programming Language": "Python",
    "Machine Learning": "Scikit-Learn",
    "Data Processing": "Pandas, NumPy",
    "Visualization": "Plotly",
    "Web Framework": "Streamlit",
    "Model Format": "Joblib (.pkl)"
}

st.table(tech)

st.markdown("---")

# ======================================
# Features
# ======================================

st.subheader("✨ Key Features")

st.success("""

✅ Customer Churn Prediction

✅ Batch Prediction

✅ Interactive Analytics Dashboard

✅ Business Insights

✅ AI Retention Strategy

✅ Model Performance Dashboard

✅ Download Prediction Results

✅ Interactive Charts

✅ Responsive UI

""")

st.markdown("---")

# ======================================
# Folder Structure
# ======================================

st.subheader("📁 Project Structure")

st.code("""
Customer_Churn_Prediction/
│
├── app.py
├── config.py
├── utils.py
├── charts.py
├── style.css
├── churn_model.pkl
├── preprocessor.pkl
├── requirements.txt
│
├── pages/
│   ├── 2_Prediction.py
│   ├── 3_Analytics.py
│   ├── 4_Batch_Prediction.py
│   ├── 5_Model_Performance.py
│   ├── 6_Business_Insights.py
│   ├── 7_Settings.py
│   └── 8_About.py
""")

st.markdown("---")

# ======================================
# Future Improvements
# ======================================

st.subheader("🚀 Future Enhancements")

st.warning("""

🔹 SHAP Explainability

🔹 XGBoost / LightGBM Models

🔹 Real-Time Database Integration

🔹 User Authentication

🔹 Email Alerts

🔹 Docker Deployment

🔹 Cloud Deployment

🔹 REST API Integration

🔹 Auto Model Retraining

""")

st.markdown("---")

# ======================================
# Developer
# ======================================

st.subheader("👨‍💻 Developer")

st.success("""

Name : Harsh

Role : Data Science & Machine Learning Enthusiast

Project :

Customer Churn Prediction Platform

Tools :

Python

Streamlit

Scikit-Learn

Plotly

Pandas

NumPy

""")

st.markdown("---")

st.caption("© 2026 Customer Churn Prediction Platform | Built with ❤️ using Python & Streamlit")