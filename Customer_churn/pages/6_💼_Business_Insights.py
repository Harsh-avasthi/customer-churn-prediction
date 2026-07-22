import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ---------------------------------------
# Page Config
# ---------------------------------------

st.set_page_config(
    page_title="Business Insights",
    page_icon="💼",
    layout="wide"
)

# ---------------------------------------
# Absolute Path Setup
# ---------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

CSS_PATH = os.path.join(ROOT_DIR, "style.css")
DATA_PATH = os.path.join(ROOT_DIR, "telco_clean.csv")

# ---------------------------------------
# Load CSS Safely
# ---------------------------------------
try:
    if os.path.exists(CSS_PATH):
        with open(CSS_PATH) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# ---------------------------------------
# Load Dataset Safely
# ---------------------------------------

@st.cache_data
def load_data():
    if os.path.exists(DATA_PATH):
        data = pd.read_csv(DATA_PATH)
        # Convert 'Churn' column to numeric (1 for Yes, 0 for No) for calculations like sum()
        if "Churn" in data.columns:
            data["Churn"] = data["Churn"].apply(lambda x: 1 if str(x).strip() == 'Yes' else 0)
        return data
    return None

df = load_data()

if df is not None:

    # ---------------------------------------
    # Header
    # ---------------------------------------

    st.title("💼 Business Insights Dashboard")

    st.caption("AI Driven Customer Retention Insights")

    st.markdown("---")

    # ---------------------------------------
    # KPI Cards
    # ---------------------------------------

    total = len(df)
    churn = int(df["Churn"].sum())
    stay = total - churn
    rate = (churn / total) * 100

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("👥 Customers", total)

    with c2:
        st.metric("🚨 Churn Customers", churn)

    with c3:
        st.metric("✅ Retained", stay)

    with c4:
        st.metric("📊 Churn Rate", f"{rate:.2f}%")

    st.markdown("---")

    # ---------------------------------------
    # Estimated Revenue Loss
    # ---------------------------------------

    avg_bill = df["MonthlyCharges"].mean()

    estimated_loss = churn * avg_bill

    st.error(
        f"💰 Estimated Monthly Revenue at Risk : ₹ {estimated_loss:,.2f}"
    )

    st.markdown("---")

    # ---------------------------------------
    # Churn By Contract
    # ---------------------------------------

    st.subheader("📊 Churn by Contract")

    contract = (
        df.groupby("Contract")["Churn"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        contract,
        x="Contract",
        y="Churn",
        color="Contract",
        text="Churn",
        title="Contract Wise Churn"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------------------------------------
    # Internet Service
    # ---------------------------------------

    st.subheader("🌐 Internet Service Analysis")

    internet = (
        df.groupby("InternetService")["Churn"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        internet,
        values="Churn",
        names="InternetService",
        hole=.45,
        title="Internet Service Churn"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------------------------------------
    # AI Recommendation
    # ---------------------------------------

    st.markdown("---")

    st.subheader("🤖 AI Business Suggestions")

    if rate < 20:

        st.success("""
    ### 🟢 Healthy Customer Base

    ✔ Continue loyalty programs

    ✔ Upsell premium plans

    ✔ Focus on customer engagement
    """)

    elif rate < 40:

        st.warning("""
    ### 🟡 Moderate Risk

    ✔ Launch targeted campaigns

    ✔ Offer annual contracts

    ✔ Improve customer support

    ✔ Provide personalized discounts
    """)

    else:

        st.error("""
    ### 🔴 High Risk

    ✔ Immediate retention campaign

    ✔ Contact high-value customers

    ✔ Improve service quality

    ✔ Offer special discounts

    ✔ Assign retention managers
    """)

    st.markdown("---")

    # ---------------------------------------
    # Executive Summary
    # ---------------------------------------

    st.subheader("📄 Executive Summary")

    st.info(f"""
    Total Customers : {total}

    Customers at Risk : {churn}

    Retention Rate : {(stay/total)*100:.2f}%

    Estimated Revenue at Risk :

    ₹ {estimated_loss:,.2f} / Month

    Recommendation :

    Focus on Month-to-Month contract customers and provide loyalty offers.
    """)

else:
    st.error("⚠️ `telco_clean.csv` file not found in the root directory. Please check your GitHub files.")
