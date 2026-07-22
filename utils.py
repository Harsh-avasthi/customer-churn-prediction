import joblib
import pandas as pd

# Load Model
model = joblib.load("churn_model.pkl")

# Load Preprocessor
preprocessor = joblib.load("preprocessor.pkl")


def predict_customer(input_df):
    # Ensure columns order matches the training data exactly
    expected_columns = [
        "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
        "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
        "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
        "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
        "MonthlyCharges", "TotalCharges"
    ]
    
    # Reindex or ensure columns match
    input_df = input_df[expected_columns]

    processed = preprocessor.transform(input_df)

    prediction = model.predict(processed)

    probability = model.predict_proba(processed)

    return prediction[0], probability[0][1]


def risk_level(prob):

    if prob < 0.30:
        return "🟢 Low Risk"

    elif prob < 0.70:
        return "🟡 Medium Risk"

    else:
        return "🔴 High Risk"


def recommendation(prob):

    if prob < 0.30:

        return """
Customer is loyal.

✔ Continue current plan

✔ Send thank-you email
"""

    elif prob < 0.70:

        return """
Customer may churn.

✔ Offer discount

✔ Contact customer

✔ Improve service
"""

    else:

        return """
High Churn Risk

✔ Call Immediately

✔ Upgrade Plan

✔ Loyalty Offer

✔ Premium Support
"""