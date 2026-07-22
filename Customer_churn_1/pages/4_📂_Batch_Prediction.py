import streamlit as st
import pandas as pd
import joblib

# -----------------------
# Page Config
# -----------------------

st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide"
)

# -----------------------
# Load CSS
# -----------------------

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------
# Load Model
# -----------------------

model = joblib.load("churn_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

# -----------------------
# Header
# -----------------------

st.title("📂 Batch Customer Churn Prediction")

st.write("Upload a CSV file to predict churn for multiple customers.")

st.markdown("---")

# -----------------------
# Upload File
# -----------------------

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Uploaded Dataset")

    st.dataframe(df.head(), use_container_width=True)

    if st.button("🚀 Predict All Customers", use_container_width=True):

        with st.spinner("Processing..."):

            X = preprocessor.transform(df)

            prediction = model.predict(X)

            probability = model.predict_proba(X)[:, 1]

            df["Prediction"] = prediction

            df["Probability"] = (probability * 100).round(2)

            df["Risk"] = pd.cut(
                probability,
                bins=[0, 0.3, 0.7, 1],
                labels=["Low", "Medium", "High"]
            )

        st.success("Prediction Completed Successfully!")

        # -----------------------
        # KPI Cards
        # -----------------------

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Total Customers",
                len(df)
            )

        with c2:
            st.metric(
                "Likely to Churn",
                int((df["Prediction"] == 1).sum())
            )

        with c3:
            st.metric(
                "Likely to Stay",
                int((df["Prediction"] == 0).sum())
            )

        st.markdown("---")

        st.subheader("📊 Prediction Results")

        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Results",
            data=csv,
            file_name="batch_predictions.csv",
            mime="text/csv"
        )