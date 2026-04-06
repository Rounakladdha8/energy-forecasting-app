# Building Energy Forecasting & Cost Analysis

This project develops a machine learning-based application to predict building heating energy consumption and estimate associated costs. It enables interactive scenario analysis by allowing users to adjust building design parameters and evaluate their impact on energy efficiency and cost.

---

## 📊 Problem Statement

Energy efficiency is a critical factor in building design. Poor design choices can lead to higher heating and cooling costs. This project aims to:

- Predict heating energy requirements of buildings
- Estimate energy cost based on predicted consumption
- Analyze how design parameters affect energy efficiency
- Support decision-making through scenario comparison

---

## 📁 Dataset Information

The dataset used is the **Energy Efficiency Dataset** from the UCI Machine Learning Repository.

### 🔹 Dataset Characteristics

- Total Instances: 768
- Features: 8 input variables
- Targets:
  - Heating Load (Y1)
  - Cooling Load (Y2)

### 🔹 Input Features

| Feature | Description |
|--------|------------|
| Relative Compactness | Shape efficiency of the building |
| Surface Area | Total external surface area |
| Wall Area | Area of building walls |
| Roof Area | Area of roof |
| Overall Height | Building height |
| Orientation | Building orientation (categorical encoded as integers) |
| Glazing Area | Window area proportion |
| Glazing Area Distribution | Distribution of glazing across surfaces |

### 🔹 Target Variable

- Heating Load → Used for prediction in this project
- Cooling Load → Available but not used in this model

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Loaded dataset using Pandas
- Renamed columns for clarity
- Verified no missing values

### 2. Model Development
- Used **Linear Regression (Scikit-learn)**
- Split dataset into training and testing sets
- Evaluated model using Mean Absolute Error (MAE)

### 3. Feature Insights
- Observed strong relationships between:
  - Overall Height and Heating Load
  - Relative Compactness and Energy Efficiency
  - Surface Area and Heat Loss

---

## 💡 Business Logic Layer

To make predictions actionable:



- Implemented **scenario comparison**:
- Baseline vs User-defined configuration
- Calculated % cost change

---

## 🖥️ Application (Streamlit)

An interactive web application was built using Streamlit.

### 🔹 Features

- User input via sliders for building parameters
- Real-time prediction of heating load
- Cost estimation
- Scenario comparison (baseline vs modified input)
- Business-friendly explanation of results

---

## 📈 Example Use Case

Users can modify parameters such as:
- Glazing Area
- Building Height
- Surface Area

And instantly observe:
- Impact on heating load
- Change in estimated cost
- Efficiency trade-offs

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

- Converted energy predictions into **estimated cost**
- Cost formula:
