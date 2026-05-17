import streamlit as st
import joblib
import numpy as np

model = joblib.load(r'C:\Users\hp\Desktop\churn-prediction\models\churn_model.pkl')
scaler = joblib.load(r'C:\Users\hp\Desktop\churn-prediction\models\scaler.pkl')

st.title("Customer Churn Prediction App")
st.write("Fill in customer data and predict - Will they churn or not?")

gender = st.selectbox("Gender", [0, 1])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", [0, 1])
dependents = st.selectbox("Dependents", [0, 1])
tenure = st.slider("Tenure (Months)", 0, 72, 12)
phone = st.selectbox("Phone Service", [0, 1])
multiple = st.selectbox("Multiple Lines", [0, 1, 2])
internet = st.selectbox("Internet Service", [0, 1, 2])
security = st.selectbox("Online Security", [0, 1, 2])
backup = st.selectbox("Online Backup", [0, 1, 2])
protection = st.selectbox("Device Protection", [0, 1, 2])
support = st.selectbox("Tech Support", [0, 1, 2])
tv = st.selectbox("Streaming TV", [0, 1, 2])
movies = st.selectbox("Streaming Movies", [0, 1, 2])
contract = st.selectbox("Contract", [0, 1, 2])
billing = st.selectbox("Paperless Billing", [0, 1])
payment = st.selectbox("Payment Method", [0, 1, 2, 3])
monthly = st.number_input("Monthly Charges", 0.0, 120.0, 65.0)
total = st.number_input("Total Charges", 0.0, 9000.0, 1000.0)

if st.button("Predict"):
    data = np.array([[gender, senior, partner, dependents, tenure,
                      phone, multiple, internet, security, backup,
                      protection, support, tv, movies, contract,
                      billing, payment, monthly, total]])
    data = scaler.transform(data)
    result = model.predict(data)
    if result[0] == 1:
        st.error("⚠️ Customer Will Churn")
    else:
        st.success("✅ Customer Will Stay!")