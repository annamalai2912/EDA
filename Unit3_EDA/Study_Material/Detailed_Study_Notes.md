# Unit 3: Exploratory Data Analysis (EDA) - Detailed Study Guide

## 1. Introduction to Data Exploration Process

**Exploratory Data Analysis (EDA)** is the crucial first step in any data science project. It involves summarizing the main characteristics of a dataset, often using visual methods. The goal is to:
*   Understand the data structure.
*   Check assumptions.
*   Detect anomalies (outliers).
*   Find patterns and relationships.

**The Process:**
1.  **Data Discovery**: Identifying where the data resides (databases, APIs, CSVs) and gaining access.
2.  **Characterization**: Understanding the dimensions (rows/cols), data types (int, float, object), and basic statistics.
3.  **Data Preparation**: Cleaning the data (handling missing values, duplicates, inconsistencies).
4.  **Analysis Questions**: Formulating hypotheses (e.g., "Is there a relationship between Age and Salary?").
5.  **Graphical Techniques**: Using charts to visualize distributions and correlations.

---

## 2. Issues Related with Data Access

Before analysis begins, getting the data can be challenging:
*   **Security & Privacy**: Dealing with sensitive data (PII like names, SSNs) requires anonymization and strict access controls.
*   **Format Incompatibility**: Data might be in unstructured formats (PDFs, logs) or proprietary formats requiring specialized parsers.
*   **Volume**: Datasets might be too large for local memory (Big Data), requiring sampling or distributed computing (Spark).
*   **Latency**: Real-time data access might have delays, affecting time-sensitive analysis.

---

## 3. Characterization of Data & Consistency

**Characterization** involves summarizing the data:
*   **Central Tendency**: Mean (average), Median (middle value), Mode (most frequent).
*   **Dispersion**: Variance, Standard Deviation, Range, IQR (Interquartile Range).
*   **Shape**: Skewness (asymmetry) and Kurtosis (tailedness).

**Consistency & Pollution:**
*   **Inconsistency**: Data that violates logical rules.
    *   *Example*: A user's "Age" is 25, but "Year of Birth" is 1900.
    *   *Example*: Date formats mixed as `MM/DD/YYYY` and `DD/MM/YYYY`.
*   **Pollution**: The presence of erroneous or irrelevant data.
    *   *Example*: Test data (`test_user_1`) left in a production database.
    *   *Example*: System error codes (`-999`) stored in a numeric age column.

---

## 4. Duplicate or Redundant Variables

*   **Duplicates**: Identical rows that inflate the dataset size and bias results (e.g., counting a customer twice).
    *   *Handling*: `df.drop_duplicates()`
*   **Redundant Variables**: Two variables that carry the same information (High Correlation / Multicollinearity).
    *   *Example*: "Age in Years" and "Date of Birth". You only need one.
    *   *Impact*: Causes instability in regression models (multicollinearity).

---

## 5. Outliers and Leverage Data

*   **Outliers**: Observations that deviate significantly from the rest of the data.
    *   *Cause*: Measurement errors, data entry errors, or genuine extreme events.
    *   *Detection*: Box Plots, Z-Score (> 3), IQR method.
*   **Leverage Points**: In regression, these are points with extreme predictors (x-values) that have a high potential to influence the slope of the regression line.

**Noisy Data**:
*   Random error or variance in a measured variable.
*   *Solution*: Smoothing techniques (Moving Average, Binning).

---

## 6. Missing Values & Imputation Techniques

**Missing Patterns:**
1.  **MCAR (Missing Completely at Random)**: The missingness typically happens randomly (e.g., a sensor temporarily failed).
    *   *Action*: Safe to drop rows if sample size permits.
2.  **MAR (Missing at Random)**: The probability of missingness depends on other observed variables (e.g., women are more likely to skip the "Weight" question).
    *   *Action*: Imputation is preferred over dropping.
3.  **MNAR (Missing Not at Random)**: The missingness depends on the value itself (e.g., high-income earners hide their income).
    *   *Action*: Modeled explicitly; simple imputation often biases results.

**Imputation Techniques:**
1.  **Mean/Median**: Fill with the average or middle value (Simple, but reduces variance).
2.  **Mode**: Fill with the most frequent value (Good for categorical data).
3.  **KNN Imputation**: Find the 'k' most similar rows and use their average.
4.  **Forward/Backward Fill**: Propagate the last valid observation (Time Series).
5.  **Multiple Imputation (MICE)**: Iteratively models each feature with missing values as a function of other features.

**Handling Non-Numerical (Categorical) Missing Data:**
*   **Mode Imputation**: Simple and fast.
*   **"Unknown" Category**: Treat missing as a separate category. This preserves the information that the value was missing.

---

## 7. Graphical Techniques & Autocorrelation

**Common Plots:**
*   **Histogram**: Distribution of a single variable.
*   **Box Plot**: Five-number summary (Min, Q1, Median, Q3, Max) + Outliers.
*   **Scatter Plot**: Relationship between two variables.

**Autocorrelation Plot (Correlogram):**
Used in Time Series to see if past values influence future values.
*   **Random Data**: Spikes are small and stay within the confidence interval bounds (usually blue shaded region).
*   **Moderate Correlation**: Spikes decay slowly.
*   **Strong Autoregressive**: High correlation at Lag 1 ($r_{t, t-1}$) that tapers off.
*   **Sinusoidal**: Calculating correlation reveals a wave pattern, indicating seasonality.
