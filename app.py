import streamlit as st
import pandas as pd
from config import *

# ---------------------------
# Page Config
# ---------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Load CSS
# ---------------------------

try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# ---------------------------
# Multi-page Navigation Setup
# ---------------------------

pages = {
    "Overview": [
        st.Page("app.py", title="Dashboard", icon="🏠")
    ],
    "Prediction & Analytics": [
        st.Page("pages/2_🤖_Prediction.py", title="Prediction", icon="🤖"),
        st.Page("pages/3_📊_Analytics.py", title="Analytics", icon="📊"),
        st.Page("pages/4_Batch_Prediction.py", title="Batch Prediction", icon="📂")
    ],
    "Insights & Model": [
        st.Page("pages/5_Model_Performance.py", title="Model Performance", icon="📉"),
        st.Page("pages/6_Business_Insights.py", title="Business Insights", icon="💼"),
        st.Page("pages/7_Settings.py", title="Settings", icon="⚙️"),
        st.Page("pages/8_About.py", title="About", icon="ℹ️")
    ]
}

pg = st.navigation(pages)

# ---------------------------
# Sidebar (Shared Elements)
# ---------------------------

with st.sidebar:
    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=80)
    st.title("Customer Churn")
    st.caption("Prediction Platform v2.0")
    st.markdown("---")
    st.success("🟢 Model Loaded")
    st.info(f"""
**Model**

{MODEL_NAME}

Accuracy : {MODEL_ACCURACY}
""")
    st.markdown("---")
    st.write("### 📌 Quick Stats")
    st.metric("Customers", TOTAL_CUSTOMERS)
    st.metric("Churn", CHURN_RATE)
    st.metric("Retention", RETENTION)

# Run the selected page
pg.run()

# ---------------------------
# Header (Main Dashboard Content)
# ---------------------------

st.title("🚀 Customer Churn Prediction Platform")
st.caption("AI Powered Customer Retention Dashboard")
st.markdown("---")

# ---------------------------
# KPI Cards
# ---------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("👥 Customers", TOTAL_CUSTOMERS)

with c2:
    st.metric("🎯 Accuracy", MODEL_ACCURACY)

with c3:
    st.metric("⚠ Churn Rate", CHURN_RATE)

with c4:
    st.metric("💚 Retention", RETENTION)

st.markdown("---")

# ---------------------------
# Welcome
# ---------------------------

left, right = st.columns([2, 1])

with left:
    st.markdown("""
## 👋 Welcome

This application predicts customer churn using Machine Learning.

### Features

- 🤖 Customer Prediction

- 📊 Interactive Dashboard

- 📈 Analytics

- 📂 Batch Prediction

- 📉 Model Performance

- 💼 Business Insights

Use the **left sidebar** to navigate between pages.
""")

with right:
    st.markdown("""
<div class="glass">

### 📌 Project

**Dataset**

Telco Customer Churn

**Algorithm**

Random Forest

**Version**

2.0

**Developer**

Harsh

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------
# Dashboard Overview
# ---------------------------

st.subheader("📊 Dashboard Overview")

chart1, chart2 = st.columns(2)

with chart1:
    st.info("""
### 🎯 Objective

Predict customers likely to leave the company.

Enable retention strategies before churn happens.
""")

with chart2:
    st.success("""
### 💡 Business Benefits

✔ Increase Customer Retention

✔ Reduce Revenue Loss

✔ Improve Customer Satisfaction

✔ Better Marketing Decisions
""")

st.markdown("---")

# ---------------------------
# Workflow
# ---------------------------

st.subheader("⚙ Workflow")

st.markdown("""

1️⃣ Enter Customer Details

⬇

2️⃣ Machine Learning Prediction

⬇

3️⃣ Churn Probability

⬇

4️⃣ Business Recommendation

⬇

5️⃣ Retention Strategy

""")

st.markdown("---")

# ---------------------------
# Footer
# ---------------------------

st.markdown("""
<div class="footer">

© 2026 Customer Churn Prediction Platform

Built with ❤️ using Streamlit & Scikit-Learn

</div>
""", unsafe_allow_html=True)
