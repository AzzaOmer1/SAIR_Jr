"""الخطوة 2: قراءة البيانات من الملف، تدريب المودل، تقييمه، وحفظه."""
import os
import joblib
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

DATA_PATH = "sales_data.csv"
FEATURES = ["advertising", "price", "discount", "customers", "day_of_week", "stock"]
TARGET = "sales"

# 1) تحميل البيانات من الملف المنفصل
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError("شغّل generate_data.py اول عشان يتكون ملف البيانات")
df = pd.read_csv(DATA_PATH)
print("Data shape:", df.shape)
print("Missing values:", int(df.isnull().sum().sum()))

X, y = df[FEATURES], df[TARGET]

# 2) تقسيم
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3) Scaling (fit على التدريب فقط)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# 4) تدريب
model = LinearRegression()
model.fit(X_train_s, y_train)

# 5) تقييم
pred = model.predict(X_test_s)
print(f"MSE: {mean_squared_error(y_test, pred):.4f}")
print(f"MAE: {mean_absolute_error(y_test, pred):.4f}")
print(f"R² : {r2_score(y_test, pred):.4f}")

# 6) حفظ المودل + الـ preprocessor في فولدر بنسخة (version)
version = datetime.now().strftime("v1_%Y%m%d_%H%M%S")
model_dir = os.path.join("models", version)
os.makedirs(model_dir, exist_ok=True)
joblib.dump(model, os.path.join(model_dir, "best_model.pkl"))
joblib.dump(scaler, os.path.join(model_dir, "preprocessor.pkl"))
joblib.dump(FEATURES, os.path.join(model_dir, "features.pkl"))
print("✅ تم الحفظ في:", model_dir)
