from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# نحمّل النموذج المحفوظ من مجلد models
PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / "models" / "texas_electricity_pipeline.joblib"

st.set_page_config(
    page_title="Texas Electricity Consumption",
    page_icon="⚡",
    layout="centered",
)

st.title("Texas Monthly Electricity Consumption")
st.write(
    "Estimate monthly electricity consumption using the observed "
    "average temperature and calendar information for that month."
)

st.info(
    "This app estimates consumption after the month's average temperature "
    "is known. It is not a forecast made before the month begins."
)

if not MODEL_PATH.exists():
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

model = joblib.load(MODEL_PATH)

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input(
            "Year",
            min_value=2001,
            max_value=2100,
            value=2026,
            step=1,
        )

    with col2:
        month = st.selectbox(
            "Month",
            options=list(range(1, 13)),
            format_func=lambda m: pd.Timestamp(2000, m, 1).strftime("%B"),
            index=5,
        )

    avg_temp_f = st.number_input(
        "Observed average temperature (°F)",
        min_value=-30.0,
        max_value=130.0,
        value=70.0,
        step=0.1,
    )

    submitted = st.form_submit_button("Estimate consumption")

if submitted:
    input_data = pd.DataFrame(
        [{
            "avg_temp_f": avg_temp_f,
            "year": year,
            "month": month,
        }]
    )

    prediction = float(model.predict(input_data)[0])

    st.subheader("Estimated monthly consumption")
    st.metric(
        label="Consumption (million kWh)",
        value=f"{prediction:,.0f}",
    )
