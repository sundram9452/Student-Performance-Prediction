# 🎓 Student Performance Prediction System

A machine learning capstone project that predicts a student's final grade (G3) from academic, demographic, and behavioural indicators — built for the **AIML Summer Internship 2026**, IIHMF, MNNIT Allahabad, Prayagraj
AIML Capstone Project Guidelines · Regression-based academic performance prediction, deployed as a live Streamlit app.

---

## 🚀 Live Demo

🔗 **Streamlit App:** [student-performance-prediction-gvjtjnnqo8rmhe4viudjl5.streamlit.app](https://student-performance-prediction-gvjtjnnqo8rmhe4viudjl5.streamlit.app/)

## 📂 Repository

🔗 [github.com/sundram9452/Student-Performance-Prediction](https://github.com/sundram9452/Student-Performance-Prediction)

---

## Team

| Role | Name |
|---|---|
| Team Leader | Sundram Pandey |
| Team Member | Swastik Shukla |
| Guide | Mr. Subhas Chaganti |

---

## Overview

Academic performance is shaped by a wide mix of factors — attendance, study habits, family background, and prior grades — making early, manual identification of at-risk students slow and inconsistent. This project builds a data-driven system that predicts a student's final grade (G3) from academic and behavioural indicators, enabling early intervention before performance drops.

The project follows the complete machine learning lifecycle: problem understanding, data collection, preprocessing, exploratory data analysis, feature engineering, model building, evaluation, and deployment.

---

## Features

- Predicts student final grade (G3) on a 0–20 scale
- Interactive Streamlit interface with real-time predictions
- Performance analysis and tailored recommendations
- Powered by a Linear Regression model

---

## Dataset

- **Source:** UCI Machine Learning Repository / Kaggle — [Student Performance Dataset](https://archive.ics.uci.edu/dataset/320/student+performance) (Cortez & Silva, 2008)
- **File:** `student-por.csv` (Portuguese language course)
- **Records:** 649 students
- **Attributes:** 33 (academic, demographic, and social)
- **Target variable:** `G3` — final grade, scale 0–20
- **Missing values / duplicates:** None

Features used for modelling: `age`, `studytime`, `failures`, `absences`, `G1`, `G2`, `higher`, `internet`.

## Methodology

1. **Problem Understanding** — define objectives and study the dataset
2. **Data Collection** — load and inspect the UCI/Kaggle dataset
3. **Data Preprocessing** — check for missing values/duplicates, encode categorical fields (`higher`, `internet`), select features
4. **Exploratory Data Analysis** — univariate, bivariate, and correlation analysis; heatmaps, boxplots, distribution plots
5. **Feature Engineering** — selected 8 features balancing predictive strength with a simple, usable input form
6. **Model Building** — trained and compared 3 regression models
7. **Model Evaluation** — MAE, MSE, RMSE, R² on an 80:20 train/test split (`random_state=42`)
8. **Deployment** — best model deployed via Streamlit

## Models & Results

Three regression models were trained on an identical 519/130 train/test split and compared:

| Model | MAE | MSE | RMSE | R² Score |
|---|---|---|---|---|
| **Linear Regression** ✅ | 0.746 | 1.333 | 1.155 | **0.863** |
| Random Forest Regressor | 0.751 | 1.549 | 1.245 | 0.841 |
| XGBoost Regressor | 0.806 | 1.797 | 1.341 | 0.816 |

**Linear Regression** achieved the best performance across every metric and was selected for deployment — prior grades (G1, G2) are near-linear predictors of the final grade, so the simpler model matched and slightly outperformed the ensemble methods while remaining faster, more interpretable, and easier to deploy.

---

## App Inputs

The deployed app accepts a student's:

- Age, Weekly Study Time, Past Failures, Absences
- First Period Grade (G1), Second Period Grade (G2)
- Higher Education aspiration, Internet Access at Home

...and returns a predicted final grade (G3) out of 20, a performance category (e.g. *Excellent Performance*), and tailored recommendations.

---

## Run Locally

```bash
git clone https://github.com/sundram9452/Student-Performance-Prediction.git
cd Student-Performance-Prediction
pip install -r requirements.txt
streamlit run app.py
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## Academic Integrity

This project was completed as part of the AIML Summer Internship 2026 capstone requirements. All code was written and understood by the team members; AI tools were used for learning support only, in line with the program's academic integrity guidelines.
