import streamlit as st
import platform
import sklearn
import pandas
import plotly
import streamlit

# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

# ----------------------------------
# Load CSS
# ----------------------------------

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------------------------------
# Header
# ----------------------------------

st.title("⚙️ Project Settings")

st.caption("Application Information & Configuration")

st.markdown("---")

# ==================================
# Project Information
# ==================================

st.subheader("📌 Project Information")

c1, c2 = st.columns(2)

with c1:

    st.info("""
### 🚀 Project

Customer Churn Prediction Platform

Version : 2.0

Status : Production Ready

Type : Machine Learning
""")

with c2:

    st.success("""
### 🤖 Model

Algorithm : Random Forest

Target : Customer Churn

Prediction : Binary Classification

Deployment : Streamlit
""")

st.markdown("---")

# ==================================
# Dataset Information
# ==================================

st.subheader("📂 Dataset Details")

dataset = {

    "Dataset Name":"Telecom Customer Churn",

    "Rows":"237,503",

    "Features":"19",

    "Target":"Churn",

    "Missing Values":"Handled",

    "Encoding":"Completed",

    "Scaling":"Pipeline Based"

}

st.table(dataset)

st.markdown("---")

# ==================================
# System Information
# ==================================

st.subheader("💻 System Information")

system = {

    "Python Version": platform.python_version(),

    "Operating System": platform.system(),

    "Platform": platform.platform(),

    "Processor": platform.processor()

}

st.table(system)

st.markdown("---")

# ==================================
# Libraries
# ==================================

st.subheader("📦 Installed Libraries")

library = {

    "Streamlit": streamlit.__version__,

    "Pandas": pandas.__version__,

    "Scikit Learn": sklearn.__version__,

    "Plotly": plotly.__version__

}

st.table(library)

st.markdown("---")

# ==================================
# Features
# ==================================

st.subheader("✨ Application Features")

st.success("""

✅ Customer Prediction

✅ Batch Prediction

✅ Analytics Dashboard

✅ Business Insights

✅ Model Performance

✅ AI Recommendation

✅ CSV Download

✅ Interactive Charts

""")

st.markdown("---")

# ==================================
# Theme
# ==================================

st.subheader("🎨 Theme")

st.info("""

Dark Theme

Responsive Layout

Glassmorphism UI

Interactive Charts

Modern Dashboard

""")

st.markdown("---")

# ==================================
# Developer
# ==================================

st.subheader("👨‍💻 Developer")

st.success("""

Name : Harsh

Role : Data Science & Machine Learning

Project : Customer Churn Prediction Platform

Technology :

Python

Streamlit

Scikit-Learn

Plotly

Pandas

NumPy

""")

st.markdown("---")

st.caption("Customer Churn Prediction Platform © 2026")