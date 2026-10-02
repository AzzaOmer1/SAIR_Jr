"""الخطوة 3: استقبال المدخلات من المستخدم وإخراج توقع المبيعات."""
import glob
import os
import joblib
import pandas as pd

# تحميل آخر نسخة من المودل
latest = sorted(glob.glob(os.path.join("models", "v1_*")))[-1]
model = joblib.load(os.path.join(latest, "best_model.pkl"))
scaler = joblib.load(os.path.join(latest, "preprocessor.pkl"))
FEATURES = joblib.load(os.path.join(latest, "features.pkl"))
print("المودل المحمّل:", latest)

PROMPTS = {
    "advertising": "ميزانية الإعلان (100 - 5000)",
    "price": "السعر (5 - 100)",
    "discount": "الخصم % (0 - 40)",
    "customers": "عدد العملاء (20 - 500)",
    "day_of_week": "اليوم (1 - 7)",
    "stock": "المخزون (10 - 1000)",
}

def predict_sales(values: dict) -> float:
    """values: قاموس فيه الـ 6 مدخلات. يرجّع المبيعات المتوقعة."""
    df = pd.DataFrame([values])[FEATURES]
    return float(model.predict(scaler.transform(df))[0])

if __name__ == "__main__":
    data = {}
    for f in FEATURES:
        data[f] = float(input(f"{PROMPTS[f]}: "))
    print(f"\n📈 المبيعات المتوقعة: {predict_sales(data):,.2f}")
