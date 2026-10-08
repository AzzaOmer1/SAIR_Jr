from pathlib import Path

import cloudpickle
import pandas as pd
import streamlit as st


MODEL_PATH = (
    Path(__file__).parent
    / "models"
    / "insurance_cost_pipeline.pkl"
)


st.set_page_config(
    page_title="Insurance Charges Prediction",
    page_icon="📊",
    layout="centered",
)


@st.cache_resource
def load_model():
    with MODEL_PATH.open("rb") as file:
        return cloudpickle.load(file)


st.title("Insurance Charges Prediction")
st.write("Enter the information below to estimate insurance charges.")

if not MODEL_PATH.exists():
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

model = load_model()

with st.form("prediction_form"):
    age = st.slider("Age", min_value=18, max_value=64, value=39)

    sex = st.selectbox(
        "Sex",
        options=["female", "male"],
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=30.7,
        step=0.1,
    )

    children = st.slider(
        "Number of children",
        min_value=0,
        max_value=5,
        value=1,
    )

    smoker = st.selectbox(
        "Smoker",
        options=["no", "yes"],
    )

    region = st.selectbox(
        "Region",
        options=["southwest", "southeast", "northwest", "northeast"],
    )

    submitted = st.form_submit_button("Predict charges")

if submitted:
    input_data = pd.DataFrame(
        [
            {
                "age": age,
                "sex": sex,
                "bmi": bmi,
                "children": children,
                "smoker": smoker,
                "region": region,
            }
        ]
    )

    prediction = float(model.predict(input_data)[0])
    st.metric("Predicted charges", f"{prediction:,.2f}")