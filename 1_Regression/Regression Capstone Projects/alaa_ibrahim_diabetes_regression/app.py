import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("best_model.pkl")

# App title
st.title("Diabetes Progression Prediction")

st.write(
    "Enter the patient features to generate a prediction."
)

# Input fields
age = st.number_input("Age", value=0.0)
sex = st.number_input("Sex", value=0.0)
bmi = st.number_input("BMI", value=0.0)
bp = st.number_input("Blood Pressure", value=0.0)

s1 = st.number_input("S1", value=0.0)
s2 = st.number_input("S2", value=0.0)
s3 = st.number_input("S3", value=0.0)
s4 = st.number_input("S4", value=0.0)
s5 = st.number_input("S5", value=0.0)
s6 = st.number_input("S6", value=0.0)

# Prediction
if st.button("Predict"):
    input_data = pd.DataFrame([
        {
            "age": age,
            "sex": sex,
            "bmi": bmi,
            "bp": bp,
            "s1": s1,
            "s2": s2,
            "s3": s3,
            "s4": s4,
            "s5": s5,
            "s6": s6
        }
    ])

    prediction = model.predict(input_data)

    st.success(
        f"Predicted target: {prediction[0]:.2f}"
    )