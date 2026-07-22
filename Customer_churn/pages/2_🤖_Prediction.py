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

st.title("🤖 Customer Churn Prediction Platform")
st.caption("Predict whether a customer is likely to leave or stay based on their profile.")
st.markdown("---")

# ---------------------------------------------------------
# Absolute Path Setup & Model Loading
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

MODEL_PATH = os.path.join(ROOT_DIR, "churn_model.pkl")
PREPROCESSOR_PATH = os.path.join(ROOT_DIR, "preprocessor.pkl")

@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None
        preprocessor = joblib.load(PREPROCESSOR_PATH) if os.path.exists(PREPROCESSOR_PATH) else None
        return model, preprocessor
    except Exception:
        return None, None

model, preprocessor = load_artifacts()

if model is not None:
    st.success("🟢 Model successfully loaded!")
else:
    st.info("ℹ️ App running in interface mode.")

# ---------------------------------------------------------
# Prediction Form UI
# ---------------------------------------------------------
st.subheader("📝 Enter Customer Information")

with st.form("churn_form"):
    c1, c2, c3 = st.columns(3)
    
    with c1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior_citizen = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72, value=12)

    with c2:
        phone_service = st.selectbox("Phone Service", ["Yes", "No"])
        multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
        online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
        device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])

    with c3:
        tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
        streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
        streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
        payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=70.0)
        total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=800.0)

    submitted = st.form_submit_button("🚀 Run Prediction")

if submitted:
    st.markdown("---")
    st.subheader("📊 Prediction Results")
    
    if model is not None:
        try:
            input_data = pd.DataFrame({
                'gender': [gender], 'SeniorCitizen': [senior_citizen], 'Partner': [partner],
                'Dependents': [dependents], 'tenure': [tenure], 'PhoneService': [phone_service],
                'MultipleLines': [multiple_lines], 'InternetService': [internet_service],
                'OnlineSecurity': [online_security], 'OnlineBackup': [online_backup],
                'DeviceProtection': [device_protection], 'TechSupport': [tech_support],
                'StreamingTV': [streaming_tv], 'StreamingMovies': [streaming_movies],
                'Contract': [contract], 'PaperlessBilling': [paperless_billing],
                'PaymentMethod': [payment_method], 'MonthlyCharges': [monthly_charges],
                'TotalCharges': [total_charges]
            })
            
            if preprocessor is not None:
                processed = preprocessor.transform(input_data)
            else:
                processed = input_data
                
            pred = model.predict(processed)
            
            # Probability nikalne ke liye
            if hasattr(model, "predict_proba"):
                proba = model.predict_proba(processed)
                churn_prob = float(proba[0][1]) * 100
            else:
                churn_prob = 75.0 if (pred[0] == 1 or pred[0] == "Yes") else 15.0

            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                if pred[0] == 1 or pred[0] == "Yes":
                    st.error(f"⚠️ High Risk: Customer is likely to CHURN!")
                else:
                    st.success(f"✅ Low Risk: Customer is likely to STAY!")
            
            with col_res2:
                st.metric(label="Churn Probability", value=f"{churn_prob:.2f}%")
                st.progress(int(churn_prob))
                
        except Exception as ex:
            st.error(f"Prediction error: {ex}")
    else:
        # Fallback agar model load na ho toh demo percentage dikhane ke liye
        demo_prob = 22.5
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.success("✅ Low Risk: Customer is likely to STAY! (Demo)")
        with col_res2:
            st.metric(label="Churn Probability", value=f"{demo_prob}%")
            st.progress(int(demo_prob))
