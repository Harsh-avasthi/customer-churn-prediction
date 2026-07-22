import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# Load CSS
# -------------------------

try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# -------------------------
# Load Dataset
# -------------------------

@st.cache_data
def load_data():
    data = pd.read_csv("telco_clean.csv")
    # Convert 'Churn' column to numeric (1 for Yes, 0 for No) to avoid mean/calculation errors
    if "Churn" in data.columns:
        data["Churn_Numeric"] = data["Churn"].apply(lambda x: 1 if str(x).strip() == 'Yes' else 0)
    return data

df = load_data()

# -------------------------
# Header
# -------------------------

st.title("📊 Customer Analytics Dashboard")
st.caption("Explore Customer Churn Patterns")

st.markdown("---")

# -------------------------
# KPI Cards
# -------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Customers", len(df))

with c2:
    st.metric("Average Monthly Charges",
              f"₹ {df['MonthlyCharges'].mean():.2f}")

with c3:
    st.metric("Average Tenure",
              f"{df['tenure'].mean():.1f} Months")

with c4:
    # Use Churn_Numeric for mathematical calculations like mean()
    if "Churn_Numeric" in df.columns:
        churn_rate = df["Churn_Numeric"].mean() * 100
    else:
        churn_rate = 0.0
    st.metric("Churn Rate",
              f"{churn_rate:.2f}%")

st.markdown("---")

# -------------------------
# Row 1
# -------------------------

col1, col2 = st.columns(2)

with col1:
    fig = px.pie(
        df,
        names="Churn",
        title="Customer Churn Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.bar(
        df,
        x="Contract",
        color="Churn",
        title="Contract vs Churn"
    )
    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Row 2
# -------------------------

col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(
        df,
        x="MonthlyCharges",
        color="Churn",
        title="Monthly Charges Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.box(
        df,
        x="Churn",
        y="tenure",
        color="Churn",
        title="Tenure Analysis"
    )
    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Row 3
# -------------------------

fig = px.histogram(
    df,
    x="InternetService",
    color="Churn",
    title="Internet Service Analysis"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Dataset Preview
# -------------------------

st.markdown("---")

st.subheader("📋 Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)

# -------------------------
# Download
# -------------------------

csv = df.to_csv(index=False)

st.download_button(
    "📥 Download Dataset",
    csv,
    "telco_clean.csv",
    "text/csv"
)