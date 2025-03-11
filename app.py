import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Page config
st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Load data safely
file_path = os.path.join(os.path.dirname(__file__), 'data', 'processed_data.csv')
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    st.error("🚫 The data file was not found. Make sure 'processed_data.csv' exists in the 'data/' folder.")
    st.stop()

# Sidebar - Filters
st.sidebar.title("🔍 Filter Options")

if 'gender' in data.columns:
    gender_filter = st.sidebar.multiselect("Select Gender", options=data['gender'].unique(), default=data['gender'].unique())
    data = data[data['gender'].isin(gender_filter)]

if 'SeniorCitizen' in data.columns:
    senior_filter = st.sidebar.multiselect("Senior Citizen", options=data['SeniorCitizen'].unique(), default=data['SeniorCitizen'].unique())
    data = data[data['SeniorCitizen'].isin(senior_filter)]

if 'Contract' in data.columns:
    contract_filter = st.sidebar.multiselect("Contract Type", options=data['Contract'].unique(), default=data['Contract'].unique())
    data = data[data['Contract'].isin(contract_filter)]

# Sidebar - Show Columns
st.sidebar.subheader("📋 Available Columns")
st.sidebar.write(data.columns.tolist())

# Title
st.title("📊 Customer Churn Dashboard")

# Key Metrics
st.markdown("### 🔢 Key Metrics")
total_customers = data.shape[0]
churn_rate = data['Churn'].value_counts(normalize=True).get('Yes', 0) * 100

col1, col2 = st.columns(2)
col1.metric("Total Customers", f"{total_customers}")
col2.metric("Churn Rate", f"{churn_rate:.2f}%")

# Show Preview
st.markdown("### 🧾 Sample Data")
st.dataframe(data.head())

# Plot: Churn Distribution
st.markdown("### 📉 Churn Distribution")
fig, ax1 = plt.subplots()
sns.countplot(data=data, x='Churn', ax=ax1)
st.pyplot(fig)

# Plot: Churn by Internet Service
if 'InternetService' in data.columns:
    st.markdown("### 📡 Churn by Internet Service")
    fig2, ax2 = plt.subplots()
    sns.countplot(data=data, x='InternetService', hue='Churn', ax=ax2)
    st.pyplot(fig2)
else:
    st.warning("⚠️ Column 'InternetService' not found in data.")

# Plot: Churn by Contract
if 'Contract' in data.columns:
    st.markdown("### 📃 Churn by Contract Type")
    fig3, ax3 = plt.subplots()
    sns.countplot(data=data, x='Contract', hue='Churn', ax=ax3)
    st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("✅ Dashboard by **Abhishek Alavandi** | Powered by Streamlit & Seaborn")
