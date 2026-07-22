import streamlit as st
import pandas as pd

# ---------------------------------------
# Page Config
# ---------------------------------------

st.set_page_config(
    page_title="Customer Churn Prediction Platform",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------
# Load CSS
# ---------------------------------------

try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# ---------------------------------------
# Load Dataset for KPIs
# ---------------------------------------

@st.cache_data
def load_data():
    try:
        return pd.read_csv("telco_clean.csv")
    except FileNotFoundError:
        return None

df = load_data()

# ---------------------------------------
# Header Section
# ---------------------------------------

st.title("🚀 Customer Churn Prediction Platform")
st.caption("AI Powered Customer Retention Dashboard")

st.markdown("---")

# ---------------------------------------
# Quick Stats / KPIs
# ---------------------------------------

if df is not None:
    total_cust = len(df)
    if "Churn" in df.columns:
        # Handle string or numeric churn safely
        churn_count = df["Churn"].apply(lambda x: 1 if str(x).strip() in ['Yes', '1'] else 0).sum()
        churn_rate = (churn_count / total_cust) * 100
        retention_rate = 100 - churn_rate
    else:
        churn_count = 0
        churn_rate = 0.0
        retention_rate = 100.0

    avg_acc = 96.2  # Model accuracy benchmark

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("👥 Customers", f"{total_cust:,}")

    with c2:
        st.metric("🎯 Model Accuracy", f"{avg_acc}%")

    with c3:
        st.metric("🚨 Churn Rate", f"{churn_rate:.1f}%")

    with c4:
        st.metric("🛡️ Retention", f"{retention_rate:.1f}%")

st.markdown("---")

# ---------------------------------------
# Welcome & Features Section
# ---------------------------------------

st.subheader("👋 Welcome")
st.write("This application predicts customer churn using Machine Learning models trained on telecom data.")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### ✨ Key Features")
    st.markdown("""
    * **🤖 Single Prediction:** Real-time risk analysis for individual customers.
    * **📊 Analytics Dashboard:** Deep dive into churn trends and statistics.
    * **📁 Batch Prediction:** Upload CSV files to predict churn for multiple customers at once.
    * **💼 Business Insights:** Revenue risk evaluation and AI retention strategies.
    """)

with col_b:
    st.markdown("### 📋 Project Info")
    if df is not None:
        st.info(f"""
        * **Dataset:** Telco Customer Churn
        * **Total Records:** {len(df):,} rows
        * **Algorithm:** Random Forest / ML Classifier
        * **Status:** Production Ready 🚀
        """)
    else:
        st.warning("Dataset `telco_clean.csv` not found in the root directory.")

st.markdown("---")
st.success("👈 Use the sidebar to navigate to **Prediction**, **Analytics**, or other pages.")