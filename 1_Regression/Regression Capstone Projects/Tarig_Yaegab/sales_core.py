"""منطق مشترك: تحميل البيانات، التدريب، الحفظ، تحميل آخر موديل، التوقع."""
import glob
import os
from datetime import datetime

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA_PATH = "sales_data.csv"
FEATURES = ["advertising", "price", "discount", "customers", "day_of_week", "stock"]
TARGET = "sales"
COLUMNS = FEATURES + [TARGET]


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def save_data(df: pd.DataFrame, path: str = DATA_PATH) -> None:
    df[COLUMNS].to_csv(path, index=False)


def train(df: pd.DataFrame):
    """يدرّب الموديل ويحفظه في models/v1_<وقت>/ ويرجّع (المسار، المقاييس)."""
    df = df[COLUMNS].dropna()
    X, y = df[FEATURES], df[TARGET]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    model = LinearRegression()
    model.fit(scaler.fit_transform(X_tr), y_tr)

    pred = model.predict(scaler.transform(X_te))
    metrics = {
        "rows": len(df),
        "MSE": mean_squared_error(y_te, pred),
        "MAE": mean_absolute_error(y_te, pred),
        "R2": r2_score(y_te, pred),
    }

    version = datetime.now().strftime("v1_%Y%m%d_%H%M%S")
    model_dir = os.path.join("models", version)
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, os.path.join(model_dir, "best_model.pkl"))
    joblib.dump(scaler, os.path.join(model_dir, "preprocessor.pkl"))
    joblib.dump(FEATURES, os.path.join(model_dir, "features.pkl"))
    return model_dir, metrics


def latest_model_dir():
    dirs = sorted(glob.glob(os.path.join("models", "v1_*")))
    return dirs[-1] if dirs else None


def load_latest():
    d = latest_model_dir()
    if d is None:
        return None
    return (
        d,
        joblib.load(os.path.join(d, "best_model.pkl")),
        joblib.load(os.path.join(d, "preprocessor.pkl")),
    )


def predict(model, scaler, values: dict) -> float:
    row = pd.DataFrame([values])[FEATURES]
    return float(model.predict(scaler.transform(row))[0])
