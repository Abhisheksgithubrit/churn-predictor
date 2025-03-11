# Customer Churn Dashboard Project

This project aims to analyze customer churn data and visualize insights using Power BI and Python.

## 📁 Folder Structure
- `data/` - Raw and processed datasets
- `models/` - Saved ML models
- `notebooks/` - Jupyter notebooks for exploration
- `outputs/` - Graphs, tables, or exported files
- `src/` - Python scripts
- `venv/` - Virtual environment (excluded from Git)

## 🛠️ Tools Used
- Python (Pandas, Matplotlib, Seaborn)
- Power BI (Dashboard)
- VS Code

## 🚀 How to Run
1. Activate virtual environment
2. Open notebook or run Python scripts from `src/`

## ✅ Dashboard Highlights
- Churn Distribution (Pie Chart)
- Churn by Contract (Bar Chart)
- Monthly Charges vs. Churn (Line Chart)

🔍 Problem Type
Customer churn prediction is a binary classification problem where the goal is to predict whether a customer will:

Churn (leave the service)
Stay (remain with the service)

✅ Algorithms Explored
We evaluated multiple classification algorithms to determine the best-performing model:

Algorithm	Description	Accuracy
Logistic Regression	A baseline linear model for binary outcomes	80.2%
Decision Tree	Splits data based on feature thresholds in a tree-like structure	82.5%
Random Forest ✅	Ensemble of decision trees to improve accuracy & reduce overfitting	88.1% ✅
K-Nearest Neighbors	Classifies based on the closest K neighbors in the feature space	77.4%
Support Vector Machine	Finds the optimal boundary (hyperplane) between churn classes	79.8%.

🏆 Final Model: Random Forest Classifier
Accuracy: 88.10%
Chosen Because: It provides the best trade-off between accuracy and generalization by aggregating multiple decision trees. It also handles missing values and categorical features well.


📊 Evaluation Metrics
In addition to accuracy, we used the following metrics to evaluate model performance:
✅ Precision
✅ Recall
✅ F1-Score
✅ Confusion Matrix
✅ ROC AUC Score

![Screenshot 2025-03-11 105405](https://github.com/user-attachments/assets/6b589839-a243-4dec-9655-1d6914f00b15)




