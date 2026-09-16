# 💳 Credit Scoring Model

A machine learning application that predicts an individual's credit risk using historical financial and personal information.

## 🚀 Live Demo

👉 https://credit-scoring-model-9rqtxwunagbgaa9um9sqht.streamlit.app/

## 📌 Project Overview

This project uses supervised machine learning classification algorithms to predict whether an applicant is likely to default on a loan.

The project includes:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature analysis
- Logistic Regression
- Decision Tree
- Random Forest
- Hyperparameter tuning
- Model evaluation
- Streamlit web application
- Model deployment

## 📊 Dataset

The dataset contains **32,581 records** and **12 features** related to an individual's financial and credit history.

Important features include:

- Person age
- Person income
- Home ownership
- Employment length
- Loan intent
- Loan grade
- Loan amount
- Interest rate
- Loan status
- Loan percent of income
- Previous default history
- Credit history length

## 🤖 Machine Learning Models

The following classification algorithms were evaluated:

### Logistic Regression

ROC-AUC:

**0.8702**

### Decision Tree

ROC-AUC:

**0.9111**

### Tuned Random Forest

The final model was selected after hyperparameter tuning.

| Metric | Score |
|---|---:|
| Accuracy | 93.57% |
| Precision | 97.35% |
| Recall | 72.57% |
| F1-Score | 83.15% |
| ROC-AUC | 93.49% |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook
- Git & GitHub

## 📂 Project Structure

```text
Credit-Scoring-Model/
│
├── data/
│   └── credit_risk_dataset.csv
│
├── models/
│   └── credit_risk_model_compressed.pkl
│
├── notebooks/
│   └── credit_scoring.ipynb
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md