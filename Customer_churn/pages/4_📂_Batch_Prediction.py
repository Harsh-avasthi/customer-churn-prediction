import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------
# Page Config
# -----------------------

st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide"
)

# -----------------------
# Absolute Path Setup
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

CSS_PATH = os.path.join(ROOT_DIR, "style.css")
MODEL_PATH = os.path.join(ROOT_DIR, "churn_model.pkl")
PREPROCESSOR_PATH = os.path.join(ROOT_DIR, "preprocessor.pkl")

# -----------------------
# Load CSS Safely
# -----------------------
try:
    if os.path.exists(CSS_PATH):
        with open(CSS_PATH) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# -----------------------
# Load Model Safely
# -----------------------
@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None
        preprocessor = joblib.load(PREPROCESSOR_PATH) if os.path.exists(PREPROCESSOR_PATH) else None
        return model, preprocessor
    except Exception:
        return None, None

model, preprocessor = load_artifacts()

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
        if model is not None and preprocessor is not None:
            with st.spinner("Processing..."):
                try:
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
                except Exception as e:
                    st.error(f"Error during transformation or prediction: {e}")
        else:
            st.error("⚠️ Model or Preprocessor file not found in root directory. Please check your GitHub files.")
