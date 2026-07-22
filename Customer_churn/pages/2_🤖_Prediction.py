import os
import sys
import joblib
import pandas as pd

# ---------------------------------------------------------
# Absolute Path Setup for Cloud Deployment (Streamlit Cloud)
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Agar parent directory me bhi search karna pade toh path add kar do
PARENT_DIR = os.path.dirname(BASE_DIR)
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)

MODEL_PATH = os.path.join(BASE_DIR, "churn_model.pkl")
PREPROCESSOR_PATH = os.path.join(BASE_DIR, "preprocessor.pkl")
DATA_PATH = os.path.join(BASE_DIR, "telco_clean.csv")

# Load Model safely
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None

# Load Preprocessor safely
try:
    preprocessor = joblib.load(PREPROCESSOR_PATH)
except Exception as e:
    preprocessor = None

# Load Dataset safely
def load_data():
    try:
        if os.path.exists(DATA_PATH):
            return pd.read_csv(DATA_PATH)
        return None
    except Exception as e:
        return None

# Prediction Function helper
def predict_churn(input_data):
    if model is None:
        raise ValueError("Model is not loaded properly. Check file paths.")
    
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data) if hasattr(model, "predict_proba") else None
    
    return prediction, probability
