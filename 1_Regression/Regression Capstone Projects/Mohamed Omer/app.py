import streamlit as st
import joblib
import pandas as pd
import os
import glob
import json

# استيراد كلاس هندسة الخصائص من ملف utils.py
try:
    from utils import AdvancedFeatureEngineer
except ImportError:
    st.warning("⚠️ لم يتم العثور على ملف utils.py، تأكد من وجوده في نفس المجلد.")

# ===========================
# 1. Auto-detect latest model version
# ===========================
model_folders = glob.glob("models/v1_*")
if not model_folders:
    st.error("❌ No model folders found in 'models/'. Please train and save a model first.")
    st.stop()

# جلب أحدث مجلد تم إنشاؤه بناءً على وقت التعديل
MODEL_DIR = max(model_folders, key=os.path.getmtime)
model_path = os.path.join(MODEL_DIR, "best_model.pkl")
preprocessor_path = os.path.join(MODEL_DIR, "preprocessor.pkl")
card_path = os.path.join(MODEL_DIR, "model_card.json")

# فحص الأمان للتأكد من وجود الملفات المطلوبة
if not os.path.exists(model_path):
    st.error(f"❌ Model file not found at {model_path}")
    st.stop()
if not os.path.exists(preprocessor_path):
    st.error(f"❌ Preprocessor file not found at {preprocessor_path}")
    st.stop()

# ✅ تحميل النموذج والـ Pipeline الموحد
@st.cache_resource
def load_model():
    model = joblib.load(model_path)
    preprocessor = joblib.load(preprocessor_path)

    # تحميل اسم النموذج ديناميكياً من بطاقة النموذج إن وجدت
    model_name = "Car Price Regressor"
    if os.path.exists(card_path):
        try:
            with open(card_path, "r") as f:
                card_data = json.load(f)
                model_name = card_data.get("model_name", model_name)
        except Exception:
            pass

    return model, preprocessor, model_name

model, preprocessor, best_model_name = load_model()

# ===========================
# 2. Streamlit UI
# ===========================
st.set_page_config(page_title="🚗 Used Car Price Predictor", layout="wide")
st.title("🚗 Used Car Price Predictor")
st.write("Enter the vehicle specifications below to estimate its market price.")

st.sidebar.header("📋 Vehicle Specifications")
col1, col2 = st.columns(2)

with col1:
    make = st.selectbox("Make / Manufacturer", ["Toyota", "Honda", "Ford", "BMW", "Audi"])
    car_model = st.selectbox("Model Name", ["Model A", "Model B", "Model C", "Model D", "Model E"])
    year = st.number_input("Manufacturing Year", min_value=2000, max_value=2026, value=2015, step=1)
    engine_size = st.number_input("Engine Size (Liters)", min_value=1.0, max_value=5.0, value=2.5, step=0.1)

with col2:
    mileage = st.number_input("Mileage (km or miles)", min_value=0, max_value=250000, value=70000, step=1000)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric"])
    transmission = st.selectbox("Transmission Type", ["Automatic", "Manual"])

# ===========================
# 3. Prepare input DataFrame
# ===========================
feature_names = [
    'Make', 'Model', 'Year', 'Engine Size', 'Mileage', 'Fuel Type', 'Transmission'
]

input_df = pd.DataFrame([[
    make, car_model, year, engine_size, mileage, fuel_type, transmission
]], columns=feature_names)

# 🛠️ إصلاح هام: التأكد من أن الأعمدة الرقمية تُعامل كأرقام وليست نصوصاً لتجنب الأخطاء الحسابية
input_df['Year'] = pd.to_numeric(input_df['Year'])
input_df['Engine Size'] = pd.to_numeric(input_df['Engine Size'])
input_df['Mileage'] = pd.to_numeric(input_df['Mileage'])

# ===========================
# 4. Preprocess & Predict
# ===========================
if st.button("🚗 Predict Car Price"):
    try:
        # معالجة المدخلات عبر الـ Pipeline الموحد
        scaled_input = preprocessor.transform(input_df)

        # التنبؤ بالسعر النهائي
        predicted_price = model.predict(scaled_input)[0]

        st.success(f"### Predicted Car Price: ${predicted_price:,.2f}")
        st.write("#### Input Features")
        st.write(input_df)
    except Exception as e:
        st.error(f"❌ Error making prediction: {str(e)}")

# ===========================
# 5. Sidebar Info
# ===========================
st.sidebar.markdown("---")
st.sidebar.subheader("ℹ️ Model Information")
st.sidebar.write(f"**Loaded from:** `{MODEL_DIR}`")
st.sidebar.write(f"**Model:** {best_model_name}")
st.sidebar.write("**Dataset:** Used Cars Dataset") 
