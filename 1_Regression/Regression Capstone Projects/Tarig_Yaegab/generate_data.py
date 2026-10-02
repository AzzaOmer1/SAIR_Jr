"""الخطوة 1: توليد ملف بيانات المبيعات (sales_data.csv) بشكل منفصل."""
import numpy as np
import pandas as pd

np.random.seed(42)
n_samples = 50_000          # غيّر الرقم لو عايز بيانات اكبر

advertising = np.random.uniform(100, 5000, n_samples)
price       = np.random.uniform(5, 100, n_samples)
discount    = np.random.uniform(0, 40, n_samples)
customers   = np.random.randint(20, 500, n_samples)
day_of_week = np.random.randint(1, 8, n_samples)
stock       = np.random.randint(10, 1000, n_samples)

noise = np.random.normal(0, 50, n_samples)

# العلاقة الحقيقية المخفية (المودل ما بيعرفها، لازم يتعلمها)
sales = (
    0.8 * advertising - 2.5 * price + 15 * discount
    + 8 * customers + 20 * day_of_week + 0.3 * stock + noise
)

df = pd.DataFrame({
    "advertising": advertising.round(2),
    "price": price.round(2),
    "discount": discount.round(2),
    "customers": customers,
    "day_of_week": day_of_week,
    "stock": stock,
    "sales": sales.round(2),
})
df.to_csv("sales_data.csv", index=False)
print(f"✅ تم حفظ sales_data.csv  | الشكل: {df.shape}")
