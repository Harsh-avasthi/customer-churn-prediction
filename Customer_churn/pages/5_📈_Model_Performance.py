import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

# -----------------------------------
# Load CSS
# -----------------------------------

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------------
# Header
# -----------------------------------

st.title("📈 Model Performance Dashboard")
st.caption("Machine Learning Model Evaluation")

st.markdown("---")

# -----------------------------------
# Metrics
# -----------------------------------

accuracy = 96.20
precision = 95.40
recall = 93.80
f1 = 94.60

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🎯 Accuracy", f"{accuracy}%")

with c2:
    st.metric("📌 Precision", f"{precision}%")

with c3:
    st.metric("📊 Recall", f"{recall}%")

with c4:
    st.metric("⭐ F1 Score", f"{f1}%")

st.markdown("---")

# -----------------------------------
# Accuracy Gauge
# -----------------------------------

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=accuracy,
    title={"text": "Model Accuracy"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "#2563EB"},
        "steps": [
            {"range": [0, 60], "color": "#EF4444"},
            {"range": [60, 80], "color": "#F59E0B"},
            {"range": [80, 100], "color": "#22C55E"}
        ]
    }
))

fig.update_layout(height=350)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# -----------------------------------
# Confusion Matrix
# -----------------------------------

st.subheader("🔲 Confusion Matrix")

cm = pd.DataFrame(
    [[920, 35],
     [42, 803]],
    columns=["Predicted Stay", "Predicted Churn"],
    index=["Actual Stay", "Actual Churn"]
)

st.dataframe(cm, use_container_width=True)

st.markdown("---")

# -----------------------------------
# Classification Report
# -----------------------------------

st.subheader("📋 Classification Report")

report = pd.DataFrame({
    "Metric": ["Precision", "Recall", "F1 Score", "Support"],
    "Stay": [0.96, 0.97, 0.96, 955],
    "Churn": [0.95, 0.94, 0.95, 845]
})

st.dataframe(report, use_container_width=True)

st.markdown("---")

# -----------------------------------
# Interpretation
# -----------------------------------

st.subheader("💡 Model Interpretation")

st.success("""
✅ High Accuracy indicates the model performs well.

✅ Precision shows predicted churn customers are mostly correct.

✅ Recall means the model identifies most customers who are likely to churn.

✅ F1 Score balances Precision and Recall.

This model is suitable for customer retention analysis.
""")