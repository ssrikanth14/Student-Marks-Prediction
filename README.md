# 🎓 Student Marks Prediction using Machine Learning

## 📖 Project Overview

This project predicts a student's exam score based on various academic, family, lifestyle, and personal factors using Machine Learning.

The project follows a complete end-to-end Machine Learning workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, model evaluation, hyperparameter tuning, model saving, and deployment using Streamlit.

The primary objective is to build a professional Machine Learning project suitable for learning, portfolio building, and interviews.

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code
- Git & GitHub


## 📊 Dataset Information

- Dataset: StudentPerformanceFactors.csv
- Number of Rows: 6607
- Number of Columns: 20
- Target Variable: Exam_Score

The dataset contains information related to:

- Academic Performance
- Attendance
- Study Hours
- Family Background
- Teacher Quality
- Lifestyle Factors
- School Information

## ⚙️ Machine Learning Workflow

- Data Cleaning
- Missing Value Handling
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Ordinal Encoding
- One-Hot Encoding
- Train-Test Split
- Feature Scaling
- Model Training
- Model Comparison
- Hyperparameter Tuning
- Model Saving
- Streamlit Deployment

## 🤖 Models Trained

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

After comparing all models, **Linear Regression** achieved the best overall performance on the test dataset and was selected as the final deployed model.

## 📈 Final Model Performance (Linear Regression)

| Metric | Score |
|---------|--------|
| MAE | 0.446 |
| RMSE | 1.800 |
| R² Score | 0.771 |

## 📂 Project Structure

```text
Student-Marks-Prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── models/
│   ├── linear_regression_model.pkl
│   └── scaler.pkl
│
├── data/
│   └── StudentPerformanceFactors.csv
│
├── notebooks/
│   └── Student_Marks_Prediction.ipynb
│
└── images/
```

## 🚀 How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 🔮 Future Improvements

- Add additional regression models
- Improve the Streamlit UI
- Deploy the application to the cloud
- Add feature importance visualization
- Create an API for predictions