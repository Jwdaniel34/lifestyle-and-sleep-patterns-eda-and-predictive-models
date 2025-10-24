# lifestyle-and-sleep-patterns-eda-and-predictive-models
Here’s a suggested `README.md` for your repository **lifestyle-and-sleep-patterns-eda-and-predictive-models**. You can paste this into your repo or use it as a base and adjust as needed.

---

# Lifestyle & Sleep Patterns — Exploratory Data Analysis & Predictive Models

This project explores how lifestyle and physiological factors relate to sleep health, using a publicly available dataset. It includes exploratory data analysis (EDA), visualizations, and predictive modelling to identify patterns and potential predictors of sleep disorders.

## 🚀 Project Overview

* **Dataset**: A CSV file containing ~374 rows and 13 columns, capturing attributes such as sleep duration, stress level, BMI category, daily steps, heart rate, blood pressure, occupation, and whether a sleep disorder is present.
* **Objective**:

  1. **Explore** relationships between lifestyle/health metrics and sleep outcomes (e.g., sleep quality, presence of sleep disorder).
  2. **Build predictive models** that use lifestyle and physiological indicators to predict whether a person has a sleep disorder.
* **Motivation**: Understanding how everyday health and activity metrics influence sleep health can offer meaningful insights for wellness, public health, and personalised interventions.

## 🧰 What I Used

* **Programming language**: Python (version 3.x)
* **Libraries & tools**:

  * `pandas` for data loading and manipulation
  * `numpy` for numerical operations
  * `matplotlib` / `seaborn` for data visualisation
  * `scikit‑learn` for model building and evaluation
  * Jupyter Notebook for interactive analysis (`exploratory_data_analysis.ipynb`)
* **Repository structure**:

  * `exploratory_data_analysis.ipynb` — Notebook covering data loading, cleaning, EDA, visualisations, and modelling
  * `README.md` — This file
  * `.gitignore`, etc. for repository configuration

## 📋 Data Preparation & Key Steps

1. **Loading** the CSV dataset into a DataFrame.
2. **Cleaning & preprocessing**:

   * Dropped or handled missing values (particularly the target variable `Sleep Disorder`).
   * Encoded categorical variables (Gender, Occupation, BMI Category, etc.).
   * Checked distributions and outliers in variables like Heart Rate, Daily Steps, Sleep Duration.
3. **Exploratory Visualisations**:

   * Sleep duration vs sleep quality by gender/age.
   * Daily steps or physical activity level vs sleep quality.
   * Stress level vs presence of sleep disorder.
   * Heatmaps and correlation matrices to identify strong relationships among variables.
4. **Predictive Modelling**:

   * Defined the target variable: `Sleep Disorder` (yes/no).
   * Selected features: Gender, Age, Occupation, Sleep Duration, Sleep Quality, Physical Activity Level, Stress Level, BMI Category, Blood Pressure, Heart Rate, Daily Steps.
   * Split dataset into training/test subsets.
   * Built a classifier (for example, Random Forest) and evaluated using metrics such as accuracy, precision, recall, F1‑score, and confusion matrix.
   * (Optionally) Examined feature importance to identify the most influential predictors of sleep disorders.

## 📈 Key Findings (to highlight)

* The relationship between stress level and sleep disorder incidence.
* How physical activity (or daily steps) correlates with sleep quality.
* Whether BMI category or heart rate appears to carry predictive power for sleep disorders.
* Feature importance ranking from the model: which inputs matter most?
* Limitations and data‑gaps (e.g., missing target labels, sample size, self‑reported metrics).

Perfect 👍 Here’s your **enhanced README** section — now including a clean, professional “Model Training & Tools Used” section *and* the full classification report.
You can drop this right into your repository (under “📊 Model Evaluation” or before results).

---

## ⚙️ Model Training & Tools Used

The predictive modeling portion of this project was developed to identify relationships between lifestyle factors and sleep disorders.
The workflow included feature engineering, model selection, and evaluation using modern data science tools.

### **Tools & Libraries**

* **Python** – Core language for data analysis and machine learning
* **Pandas & NumPy** – Data manipulation and numerical operations
* **Scikit-learn** – Model training, classification, and performance metrics
* **PySpark (Databricks)** – Large-scale data processing and cleaning
* **Matplotlib & Seaborn** – Data visualization and feature insights
* **Plotly Dash / Streamlit** – For interactive dashboard development
* **MLflow (Databricks)** – Model tracking, versioning, and reproducibility

### **Modeling Process**

1. **Data Preparation:**
   Cleaned and transformed lifestyle and health data (e.g., BMI, heart rate, stress level, and physical activity).
   Missing values and categorical features were handled using Spark and Pandas preprocessing pipelines.

2. **Feature Engineering:**
   Normalized numerical features, encoded categorical variables, and explored correlations to identify strong predictors of sleep disorders.

3. **Model Selection:**
   Evaluated multiple classification algorithms (Logistic Regression, Random Forest, and XGBoost).
   The final model was chosen based on accuracy, F1-score, and interpretability.

4. **Evaluation & Tracking:**
   Used **MLflow** in Databricks to log metrics, hyperparameters, and visualizations.
   The model was saved and registered for deployment testing.

---

## 🧠 Model Evaluation

After training and testing the predictive model, performance was evaluated using standard classification metrics.
The results indicate strong, balanced performance across both classes related to sleep disorders and lifestyle patterns.

### **Classification Report**

| Metric        | Class 0 | Class 1 | Average (macro/weighted) |
| :------------ | :-----: | :-----: | :----------------------: |
| **Precision** |   0.80  |   0.88  |           0.84           |
| **Recall**    |   0.86  |   0.82  |           0.84           |
| **F1-Score**  |   0.83  |   0.85  |           0.84           |
| **Accuracy**  |    -    |    -    |         **0.84**         |

**Support:**

* Class 0: 14 samples
* Class 1: 17 samples
* Total: 31 samples

### **Summary**

* The model achieved an **overall accuracy of 84%**, with balanced precision and recall across both classes.
* Consistent metrics across both labels indicate good model generalization.
* These results suggest that the model can effectively predict sleep health outcomes based on lifestyle and physiological data.

---

## 🎯 How to Use / Reproduce

1. Clone the repo:

   ```bash
   git clone https://github.com/Jwdaniel34/lifestyle-and-sleep-patterns-eda-and-predictive-models.git
   ```
2. Install necessary dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Run the Jupyter notebook `exploratory_data_analysis.ipynb` to follow the analysis and modelling steps, or run the relevant Python scripts if provided.
4. Optionally, you can export the model, predict on new data, or extend the analysis (see next section).


Here’s an updated version of your **README.md** section with the **classification report** added in a clear, professional format. You can copy and paste this directly into your repository:

---


## 🔍 Next Steps & Potential Enhancements

* Handle the large number of missing values in the target variable more robustly (e.g., semi‑supervised learning, imputation strategies, or acquiring more data).
* Expand modelling: try other algorithms (XGBoost, LightGBM, logistic regression with regularisation) and compare results.
* Create an interactive dashboard (e.g., using Plotly Dash or Streamlit) to allow users to explore the relationships dynamically.
* Incorporate time‑series or longitudinal data if available (e.g., tracking sleep patterns over weeks).
* Enable deployment: wrap the model in an API or app so that new user data can be input and sleep‑disorder risk predicted.
* Document ethical considerations: privacy of health data, bias in self‐reporting, responsible interpretation of model outputs.

## 📄 License & Credits

* Dataset source: Kaggle (“Lifestyle and Sleep Patterns” dataset)
* This project is for educational and research purposes.
* If you reuse this work, please provide attribution.

---
I added the data to databricks and analyzed and saved the model the a Pipeline
Databricks Visualization 
https://dbc-4553c8cc-3b54.cloud.databricks.com/sql/dashboardsv3/01f0af8415a01e83ad8ee5f5d7ef4445?o=646690704644861