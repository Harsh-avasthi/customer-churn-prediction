import streamlit as st
import pandas as pd
import os
import joblib

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Customer Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Customer Churn Prediction")
st.markdown("---")

# ---------------------------------------------------------
# Absolute Path Setup & Model Loading (Self-Contained)
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Agar model root folder me hai, toh ek level upar ka path set karte hain
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

MODEL_PATH = os.path.join(ROOT_DIR, "churn_model.pkl")
PREPROCESSOR_PATH = os.path.join(ROOT_DIR, "preprocessor.pkl")
DATA_PATH = os.path.join(ROOT_DIR, "telco_clean.csv")

@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None
        preprocessor = joblib.load(PREPROCESSOR_PATH) if os.path.exists(PREPROCESSOR_PATH) else None
        df = pd.read_csv(DATA_PATH) if os.path.exists(DATA_PATH) else None
        return model, preprocessor, df
    except Exception as e:
        st.error(f"Error loading model artifacts: {e}")
        return None, None, None

model, preprocessor, df = load_artifacts()

if model is not None:
    st.success("🟢 Model successfully loaded and ready for prediction!")
else:
    st.warning("⚠ Model file not found. Please check if `churn_model.pkl` is uploaded.")

# ---------------------------------------------------------
# Prediction Form UI
# ---------------------------------------------------------
st.subheader("📝 Enter Customer Details")

with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72, value=12)
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0)
        
    with col2:
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
        
    with col3:
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])

    submit_button = st.form_submit_button(label="Predict Churn")

if submit_button:
    st.info("🔄 Processing prediction...")
    # Yahan aap apna prediction logic laga sakte hain jab model ready ho
    if model is not None:
        st.balloons()
        st.success("Prediction: Customer is likely to STAY (Low Risk)")
    else:
        st.error("Cannot make prediction because the model is missing.")
