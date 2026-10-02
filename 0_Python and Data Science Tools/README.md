
# 🐍 Module 0: Python Foundations

**Your First Step on the Road to ML Engineering Mastery**

> 📌 **Part of the [SAIR Jr. ML Engineering Track](../README.md)** — bottom-up, depth-first. We build the foundation that lasts years, not the framework of the month.

**📍 Location:** `0_Python and Data Science Tools/`  
**🎯 Prerequisite:** None — Start here!  
**➡️ Next Module:** [Module 1: Regression Mastery](../1_Regression/README.md)

**Welcome to SAIR!** This is where your ML engineering journey begins. Whether you're completely new to programming or looking to strengthen your fundamentals, this module will give you the Python skills needed to start building real machine learning systems — from the ground up.

---

## 🎯 Is This Module For You?

### ✅ **Complete this module if:**
- You're new to Python programming
- You want to refresh your Python skills for ML
- You've never worked with NumPy, Pandas, or Matplotlib
- You want solid foundations before diving into ML algorithms

### 🚀 **Skip to [Module 1: Regression](../1_Regression/README.md) if:**
- You're already comfortable with Python basics
- You have experience with NumPy arrays and Pandas DataFrames
- You can create basic plots with Matplotlib
- You're eager to start building your first ML model

---

## 🛠️ Tools You'll Master

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)

</div>

These are the **essential tools** used by every ML engineer worldwide. Master them here, use them everywhere.

---

## 📚 What You'll Learn

| Notebook | Focus | Time Estimate | After This You Can... |
|----------|-------|---------------|-----------------------|
| **`SAIR_Lecture_0.ipynb`** | Python Basics & OOP | 3–4 hours | Write functions, classes, list comprehensions; understand Python for ML |
| **`numpy.ipynb`** | Numerical Computing | 4–5 hours | Create/reshape arrays, use broadcasting, perform matrix math for ML |
| **`pandas.ipynb`** | Data Analysis | 4–5 hours | Load CSVs, clean data, group/filter/merge DataFrames |
| **`matplot.ipynb`** | Data Visualization | 3–4 hours | Plot loss curves, histograms, scatter plots, heatmaps |

---

## 🗺️ Your Learning Journey

### **Phase 1: Get Started** 🎯
**Start with:** `SAIR_Lecture_0.ipynb`
- Python syntax, functions, and OOP basics
- Everything you need to begin Module 1

### **Phase 2: Build & Grow** 🚀
**Use as needed during Modules 1-3:**

| You'll need... | Jump to... |
|----------------|------------|
| Array operations, matrix math | `numpy.ipynb` — Sections 3–5 |
| Loading/cleaning a CSV dataset | `pandas.ipynb` — Section 2 |
| Plotting loss or accuracy curves | `matplot.ipynb` — Section 3 |
| Group-by aggregations | `pandas.ipynb` — Section 4 |
| Broadcasting confusion | `numpy.ipynb` — Section 4 |

### **Phase 3: Master the Tools** 📚
**Complete for deep understanding:**
- Return to master NumPy for performance optimization
- Deepen Pandas skills for complex data analysis
- Perfect Matplotlib for publication-quality plots

---

## 💡 Our Learning Philosophy

> **"Learn enough to build, then build to learn more."**

At SAIR, we believe in **progressive mastery**. You don't need to be an expert in everything before you start creating. These notebooks are your **foundation and reference library** — tools you'll return to again and again as you grow.

**The road to ML engineering mastery is long, but every expert started exactly where you are now.**

---

## 🚀 Quick Start Guide

### **For Beginners:**
```bash
# 1. Start with Python basics
uv run jupyter notebook SAIR_Lecture_0.ipynb

# 2. Begin Module 1: Regression when comfortable
# 3. Return to other notebooks as needed
```

### **For Those with Experience:**
```bash
# Skim SAIR_Lecture_0 to refresh basics
# Jump to Module 1 when ready
# Use other notebooks as reference during projects
```

> 💡 **First time here?** Run `uv sync` from the SAIR root first to install dependencies.

---

## 🤝 Get Help & Connect

Stuck? Have questions? Want to share your progress?

[![Telegram](https://img.shields.io/badge/Telegram-Join_SAIR_Community-blue?logo=telegram)](https://t.me/+jPPlO6ZFDbtlYzU0)

Our community of learners and mentors is here to support you every step of the way. Join live lectures and get real-time help!

---

## 🎯 Ready for Your Next Step?

### **Just starting?**
→ Begin with [`SAIR_Lecture_0.ipynb`](SAIR_Lecture_0.ipynb)

### **Ready to build?**
→ Jump to [Module 1: Regression](../1_Regression/README.md)

### **Want to deepen your skills?**
→ Explore the mastery notebooks below

---

## 📚 Mastery Notebooks

| Notebook | Description | Best For | Official Docs |
|----------|-------------|----------|---------------|
| [`numpy.ipynb`](numpy.ipynb) | High-performance numerical computing | ML algorithms & math | [numpy.org](https://numpy.org/doc/stable/) |
| [`pandas.ipynb`](pandas.ipynb) | Real-world data analysis & cleaning | Data preprocessing | [pandas.pydata.org](https://pandas.pydata.org/docs/) |
| [`matplot.ipynb`](matplot.ipynb) | Professional data visualization | Results communication | [matplotlib.org](https://matplotlib.org/stable/index.html) |

---

## 🔧 Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| `ModuleNotFoundError: numpy` | Dependencies not installed | Run `uv sync` from the SAIR root |
| Jupyter won't open | Not installed or wrong env | `uv run jupyter notebook` |
| `ValueError: shape mismatch` | Wrong array dimensions | Check shapes with `arr.shape` before operations |
| `KeyError` in pandas | Column name typo or wrong case | Use `df.columns` to list all column names |
| Blank matplotlib plot | Missing `plt.show()` or output in script | Add `plt.show()` or use `%matplotlib inline` |

---

> **"السير" — "Walking on a road"**  
> *Every master was once a beginner. Your journey to ML engineering excellence starts here.*

**Welcome to the SAIR family! 🌟**

---

**🔜 Next Step:** [Module 1: Regression Mastery](../1_Regression/README.md)

---

## 🗂️ Module Structure

```
0_Python and Data Science Tools/
│
├── 📚 README.md                    # This guide
├── 🎯 SAIR_Lecture_0.ipynb         # Start here — Python basics
├── 🚀 numpy.ipynb                  # Numerical computing mastery
├── 📊 pandas.ipynb                 # Data analysis mastery
├── 📈 matplot.ipynb                # Visualization mastery
└── 🖼️ assets/                      # Figures and images used in notebooks
    ├── research_figure.jpg
    ├── research_figure.pdf
    ├── research_figure.png
    ├── research_figure.svg
    └── SAIR.jpg
```
