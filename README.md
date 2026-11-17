# 🎓 Student Academic Performance Prediction

## 📌 Project Overview

Student Academic Performance Prediction is a Machine Learning project that predicts students' final academic grades based on their academic records, study habits, and personal information.

The project uses Linear Regression to estimate final student scores and provides a Flask-based web application where users can enter student details and receive predictions.

## 🎯 Objectives

- Analyse student academic performance data.
- Perform Exploratory Data Analysis (EDA).
- Identify relationships between study habits and academic results.
- Handle missing values and outliers.
- Apply One-Hot Encoding and feature scaling.
- Train a Linear Regression model.
- Evaluate model performance using regression metrics.
- Develop a web application using Flask.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- HTML
- CSS
- Bootstrap
- Joblib
- Jupyter Notebook

## 📊 Dataset

**Dataset:** Student Performance Dataset

**Source:** UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/320/student+performance

The dataset contains student information such as:

- Age and Gender
- Study Time
- Previous Academic Failures
- Absences
- Family Background
- First Period Grade (G1)
- Second Period Grade (G2)
- Final Grade (G3)

**Target Variable:** G3 (Final Grade)

## ⚙️ Project Workflow

### 1. Data Collection
Imported the student performance dataset using Pandas.

### 2. Exploratory Data Analysis (EDA)
- Dataset inspection
- Data visualization
- Correlation analysis
- Distribution analysis

### 3. Statistical Analysis
- Mean, Median and Mode
- Variance and Standard Deviation
- Interquartile Range (IQR)
- Outlier detection

### 4. Data Preprocessing
- Missing value analysis
- Outlier handling
- One-Hot Encoding
- Feature Scaling
- Train-Test Split

### 5. Model Training
Trained a Linear Regression model using Scikit-learn to predict final academic grades.

### 6. Model Evaluation
Evaluated the model using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## 🌐 Flask Web Application

The project includes a Flask-based web application that allows users to:

- Enter student personal information.
- Provide academic and study-related details.
- Submit information to the trained ML model.
- View the predicted final academic grade.

The trained model, scaler and feature information are saved using Joblib.

## 📂 Project Structure

```text
Student_Acedemic_Performance/
│
├── dataset/
│
├── models/
│   ├── student_model.pkl
│   ├── scaler.pkl
│   └── features.pkl
│
├── notebooks/
│   └── student_performance.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── requirements.txt
└── README.md
```

## 🚀 Installation and Setup

### Step 1: Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to Project

```bash
cd Student_Acedemic_Performance
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run Flask Application

```bash
python app.py
```

### Step 7: Open in Browser

```text
http://127.0.0.1:5000/
```

## 📈 Expected Output

The application predicts a student's estimated final academic grade on a scale of 0–20.

The predicted result is an estimate based on the patterns learned from the training dataset.

## ⚠️ Limitations

- Prediction accuracy depends on dataset quality.
- The dataset represents a specific educational environment.
- G1 and G2 are used as input features for predicting G3.
- Predictions are estimates and may differ from actual examination results.

## 🔮 Future Improvements

- Compare Linear Regression with Decision Tree and Random Forest.
- Improve prediction accuracy through hyperparameter tuning.
- Add interactive performance visualizations.
- Implement early academic performance prediction without previous grades.
- Deploy the application online.

## 👨‍💻 Author

**Atul**

B.Tech – Computer Science and Engineering

**Project:** Student Academic Performance Prediction

---

⭐ If you find this project useful, consider giving the repository a star!