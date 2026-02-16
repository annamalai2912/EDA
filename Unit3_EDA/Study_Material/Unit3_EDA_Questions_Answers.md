# Unit 3 - Exploratory Data Analysis (EDA) Q&A

This document covers the theoretical aspects of EDA, Data Exploration, Data Quality, and Missing Values handling as per the syllabus.

## 1. Introduction to Data Analysis & EDA

**Q1: What is Exploratory Data Analysis (EDA)?**
**A1:** Exploratory Data Analysis (EDA) is an approach to analyzing datasets to summarize their main characteristics, often with visual methods. It is used to discover patterns, spot anomalies, test hypotheses, and check assumptions with the help of summary statistics and graphical representations. It is a critical step before formal modeling.

**Q2: What are some common graphical techniques used in EDA?**
**A2:** Common graphical techniques include:
*   **Histograms:** To visualize the distribution of a single numerical variable.
*   **Box Plots (Box-and-Whisker Plots):** To detect outliers and see the spread of data.
*   **Scatter Plots:** To observe relationships between two numerical variables.
*   **Bar Charts:** To visualize categorical data frequencies.
*   **Heatmaps:** To visualize correlation matrices or 2D data intensity.
*   **Autocorrelation Plots:** To check for randomness or time-series dependency.

**Q3: What are the key objectives (Analysis Questions) of EDA?**
**A3:** EDA seeks to answer questions such as:
*   What is the typical value of the data (central tendency)?
*   How much does the data vary (dispersion)?
*   Are there any outliers or anomalies?
*   How are variables related to each other (correlation)?
*   Is the data consistent over time (time series analysis)?
*   Are there missing values or data quality issues?

---

## 2. Autocorrelation & Time Series patterns

**Q4: What is an Autocorrelation Plot?**
**A4:** An autocorrelation plot (or correlogram) shows the correlation of a time series with itself at different time lags. It helps identify patterns like seasonality or trends. On the x-axis are the lags (h), and on the y-axis is the autocorrelation coefficient.

**Q5: Describe different types of correlation observed in Autocorrelation Plots.**
**A5:**
*   **Random Data:** The autocorrelation coefficients are near zero for all non-zero lags.
*   **Moderate Correlation:** Coefficients decay slowly but are significantly different from zero for several lags.
*   **Strong Autoregressive Correlation:** High correlation at lag 1 that persists, often indicating that the current value strongly depends on immediate past values.
*   **Sinusoidal Correlation:** The plot exhibits a wave-like pattern (alternating positive and negative correlations), indicating seasonality or cyclical behavior.

---

## 3. Data Exploration Process

**Q6: What are the steps in the Data Exploration Process?**
**A6:** The process generally involves:
1.  **Data Access/Discovery:** Locating and retrieving the data.
2.  **Characterization:** Understanding the structure (rows, columns, data types).
3.  **Preparation (Cleaning):** Handling missing values, duplicates, and inconsistencies.
4.  **Analysis/Visualization:** Applying statistical and graphical techniques.
5.  **Documentation:** Recording findings.

**Q7: unique challenges in Data Access?**
**A7:**
*   **Security/Privacy:** Permissions, PII (Personally Identifiable Information).
*   **Format:** Handling various file formats (CSV, JSON, SQL, unstructured text).
*   **Volume:** Dealing with datasets larger than memory.
*   **Location:** Accessing data from distributed systems or APIs.

**Q8: What is meant by Data Consistency and Pollution?**
**A8:**
*   **Consistency:** Data should follow specific rules (e.g., date formats, valid ranges). Inconsistent data might have "Jan 1, 2020" and "2020-01-01" in the same column.
*   **Pollution:** Presence of erroneous or irrelevant data (e.g., test entries, system logs mixed with user data).

---

## 4. Data Quality & Cleaning

**Q9: What are Outliers and Leverage Points?**
**A9:**
*   **Outliers:** Data points that differ significantly from other observations. They can be due to variability or errors.
*   **Leverage Points:** In regression, these are observations with extreme predictor values (x-values) that can unduly influence the model's fit.

**Q10: What is Noisy Data?**
**A10:** Noisy data refers to meaningless information or random variance in a variable that obscures the true underlying pattern. It can be caused by faulty data collection instruments, data entry errors, or transmission problems.

**Q11: Why are Duplicate or Redundant Variables a problem?**
**A11:**
*   **Duplicates:** Inflate the dataset size and can bias statistical estimates (e.g., mean, count).
*   **Redundant Variables:** Two variables perfectly correlated (or identical) provide no new information and can cause multicollinearity issues in machine learning models.

---

## 5. Handling Missing Values

**Q12: Why is the Missing Pattern important?**
**A12:** Understanding *why* data is missing helps choose the right handling technique.
*   **MCAR (Missing Completely at Random):** No relationship between missingness and any values. Safe to drop.
*   **MAR (Missing at Random):** Missingness is related to observed data but not the missing value itself. Imputation is preferred.
*   **MNAR (Missing Not at Random):** Missingness depends on the unobserved value itself (e.g., high-income earners not reporting income). Requires specialized modeling.

**Q13: Common Imputation Techniques for Missing Values?**
**A13:**
*   **Mean/Median Imputation:** Replacing missing numerical values with the mean (for normal distribution) or median (for skewed data).
*   **Mode Imputation:** Replacing missing categorical values with the most frequent category.
*   **K-Nearest Neighbors (KNN):** Using similar data points to estimate missing values.
*   **Forward/Backward Fill:** Propagating the last known value forward (common in time series).

**Q14: How to handle Missing Values in Non-Numerical (Categorical) Data?**
**A14:**
*   **Mode Imputation:** Fill with the most common category.
*   **New Category:** Creating a distinct category like "Unknown" or "Missing". This preserves the information that the value was specifically missing.
*   **Prediction:** Building a classification model to predict the missing category based on other features.
