"""واجهة رسومية (Streamlit): توقع المبيعات + تعديل البيانات + إعادة التدريب.
التشغيل:  streamlit run ui.py
"""
import os

import pandas as pd
import streamlit as st

import sales_core as core

st.set_page_config(page_title="Sales Predictor", page_icon="📈", layout="wide")
st.title("📈 نظام التنبؤ بالمبيعات")

# ---------- تأكد من وجود البيانات ----------
if not os.path.exists(core.DATA_PATH):
    st.error("ملف sales_data.csv غير موجود. شغّل generate_data.py اولاً.")
    st.stop()

tab_pred, tab_data, tab_train = st.tabs(["🔮 التوقع", "🗂️ تعديل البيانات", "🧠 التدريب"])

# =====================================================
# تبويب 1: التوقع
# =====================================================
with tab_pred:
    loaded = core.load_latest()
    if loaded is None:
        st.warning("ما في موديل محفوظ. روح لتبويب التدريب وابدأ التدريب.")
    else:
        model_dir, model, scaler = loaded
        st.caption(f"الموديل المستخدم: `{model_dir}`")
        c1, c2, c3 = st.columns(3)
        advertising = c1.number_input("ميزانية الإعلان", 100.0, 5000.0, 2500.0, 50.0)
        price = c2.number_input("السعر", 5.0, 100.0, 30.0, 1.0)
        discount = c3.number_input("الخصم %", 0.0, 40.0, 15.0, 1.0)
        customers = c1.number_input("عدد العملاء", 20, 500, 200, 10)
        day = c2.selectbox("اليوم (1-7)", list(range(1, 8)), index=4)
        stock = c3.number_input("المخزون", 10, 1000, 600, 10)

        if st.button("احسب التوقع", type="primary"):
            result = core.predict(model, scaler, {
                "advertising": advertising, "price": price, "discount": discount,
                "customers": customers, "day_of_week": day, "stock": stock,
            })
            st.metric("المبيعات المتوقعة", f"{result:,.2f}")

# =====================================================
# تبويب 2: تعديل البيانات
# =====================================================
with tab_data:
    df = core.load_data()
    st.write(f"عدد الصفوف الحالي: **{len(df):,}**")

    mode = st.radio("طريقة العرض", ["أول N صف (للتعديل)", "كل البيانات (للقراءة)"], horizontal=True)

    if mode.startswith("أول"):
        n = st.slider("عدد الصفوف المعروضة للتعديل", 10, min(1000, len(df)), min(100, len(df)))
        st.caption("عدّل الخلايا مباشرة، أضف صفاً بالضغط على آخر الجدول، أو احذف صفوفاً بتحديدها ثم زر الحذف.")
        edited = st.data_editor(
            df.head(n), num_rows="dynamic", key="editor",
        )
        if st.button("💾 حفظ التعديلات في الملف", type="primary"):
            new_df = pd.concat([edited, df.iloc[n:]], ignore_index=True)
            core.save_data(new_df)
            st.success(f"تم الحفظ. العدد الآن {len(new_df):,} صف. اذهب للتدريب لإعادة بناء الموديل.")
    else:
        st.dataframe(df, height=400)

    st.divider()
    st.subheader("➕ إضافة صف جديد")
    with st.form("add_row"):
        cols = st.columns(7)
        vals = [cols[i].number_input(name, value=0.0) for i, name in enumerate(core.COLUMNS)]
        if st.form_submit_button("إضافة"):
            core.save_data(pd.concat([df, pd.DataFrame([dict(zip(core.COLUMNS, vals))])], ignore_index=True))
            st.success("تمت الإضافة. حدّث الصفحة لرؤية التغيير.")

    st.divider()
    st.subheader("📤 رفع ملف CSV جديد")
    up = st.file_uploader("ارفع ملف بنفس أسماء الأعمدة", type="csv")
    if up is not None:
        new = pd.read_csv(up)
        missing = [c for c in core.COLUMNS if c not in new.columns]
        if missing:
            st.error(f"أعمدة ناقصة: {missing}")
        else:
            st.dataframe(new.head())
            c1, c2 = st.columns(2)
            if c1.button("استبدال البيانات الحالية"):
                core.save_data(new)
                st.success("تم الاستبدال.")
            if c2.button("إلحاق بالبيانات الحالية"):
                core.save_data(pd.concat([df, new[core.COLUMNS]], ignore_index=True))
                st.success("تم الإلحاق.")

# =====================================================
# تبويب 3: التدريب
# =====================================================
with tab_train:
    st.write("درّب الموديل من جديد على الملف الحالي. كل تدريب يُحفظ كنسخة جديدة في `models/`.")
    if st.button("🚀 ابدأ التدريب", type="primary"):
        with st.spinner("جاري التدريب..."):
            model_dir, m = core.train(core.load_data())
        st.success(f"تم الحفظ في {model_dir}")
        a, b, c, d = st.columns(4)
        a.metric("الصفوف", f"{m['rows']:,}")
        b.metric("R²", f"{m['R2']:.4f}")
        c.metric("MAE", f"{m['MAE']:.2f}")
        d.metric("MSE", f"{m['MSE']:.2f}")
