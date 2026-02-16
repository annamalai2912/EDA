# Unit 3: Data Analysis Tools & EDA Techniques - Master Guide

## 1. Introduction to Data Exploration Process
The data exploration process is a **systematic approach** to uncovering the structure, issues, and patterns hidden within a dataset.
*   **Sequence**: (1) Discover (2) Characterize (3) Prepare (4) Visualize (5) Model.
*   **Analysis Questions**: Formulating hypotheses is key.
    *   *Descriptive*: "What is the average rainfall?"
    *   *Comparitive*: "Is rainfall higher in July than June?"
    *   *Relationship*: "Does rainfall correlate with crop yield?"

---

## 2. Issues Related to Data Access & Discovery
Before you can analyze, you must obtain the data.
*   **Data Discovery**: Finding relevant datasets (public repositories, internal databases, APIs). Metadata (data about data) is crucial here.
*   **Access Issues**:
    1.  **Security & Privacy**: PII (Personally Identifiable Information) like SSN, Medical Records. Requires anonymization.
    2.  **Format Incompatibility**: CSV vs JSON vs Parquet vs Proprietary binary formats.
    3.  **Latency**: Real-time data streams vs Batch processing delays.
    4.  **Licensing**: Copyright restrictions on data usage (e.g., scraping Twitter).

---

## 3. Characterization of Data: Consistency & Pollution
*   **Data Characterization**: Understanding the "shape" of data (Rows, Columns, Types).
    *   *Real-Time*: Using `df.info()` and `df.describe()` in Pandas.
*   **Data Consistency**: Adhering to logical rules.
    *   *Example*: "Date of Birth" cannot be in the future. "Age" cannot be negative.
    *   *Check*: Regex validation for emails, phone numbers.
*   **Data Pollution**: Presence of erroneous, irrelevant, or garbage data.
    *   *Example*: Test entries (`test_user_123`) mixed with production data.
    *   *Example*: System error codes (`-999`, `NULL`) stored in numeric columns.

---

## 4. Redundancy: Duplicate Variables
Two variables that carry the same information are **redundant**.
*   **Perfect Multicollinearity**: Correlation $r = 1.0$.
    *   *Example*: "Temperature in Celsius" and "Temperature in Fahrenheit". Both convey identical info.
*   **Why remove?**:
    1.  Increases computational cost.
    2.  Causes instability in Regression models (Matrix inversion fails).
    3.  Overfits tree-based models (splitting on same info twice).

---

## 5. Outliers vs Leverage Data
These are distinct concepts in regression analysis.
*   **Outlier**: An observation with an unusual **Y-value** given its X-value. (Large Residual).
    *   *Impact*: Increases error variance, lowers $R^2$.
*   **Leverage Point**: An observation with an extreme **X-value** (far from the mean of X).
    *   *High Leverage*: If it follows the trend, it strengthens the model (Good Leverage).
    *   *Bad Leverage (Influential Point)*: If it has an extreme X **AND** an unusual Y, it pulls the regression line towards itself, biasing the slope. Measured by **Cook's Distance**.

---

## 6. Graphic Techniques & Autocorrelation
Visualizing dependence structure is critical.
*   **Autocorrelation Plot (ACF)**: Correlation of a time series with its own past values ($Y_t$ vs $Y_{t-k}$).
    *   **Random Data**: Spikes at lag 1, 2, ... are near zero (within confidence bands). No pattern.
    *   **Moderate Correlation**: Spikes decay slowly.
    *   **Strong Autoregressive (AR1)**: High correlation at Lag 1 ($r \approx 0.9$), then decays exponentially.
    *   **Sinusoidal**: Alternating positive/negative spikes in a wave pattern. Indicates **Seasonality**.

---

## 7. Handling Missing Values (Imputation)
Missing data is a major issue in real-world datasets.

### A. Missing Patterns (Mechanisms)
1.  **MCAR (Missing Completely at Random)**: The probability of missingness is purely random.
    *   *Example*: A survey page failed to load for 5% of users.
    *   *Solution*: Safe to drop rows (Listwise Deletion).
2.  **MAR (Missing at Random)**: Missingness depends on *observed* data.
    *   *Example*: Men are less likely to report "Depression Score". If we have "Gender", we can model this.
    *   *Solution*: Imputation is necessary (based on Gender).
3.  **MNAR (Missing Not at Random)**: Missingness depends on the *unobserved* value itself.
    *   *Example*: High-income earners refuse to disclose income.
    *   *Solution*: Requires specialized statistical modeling (Heckman correction).

### B. Imputation Techniques
*   **Mean/Median**: Fast but reduces variance. Good for MCAR.
*   **Mode**: For Categorical data.
*   **KNN (K-Nearest Neighbors)**: Finds $k$ similar rows and averages their values. More accurate.
*   **MICE (Multivariate Imputation by Chained Equations)**: Uses regression models iteratively to predict missing values based on all other features. Comparison with "Ground Truth" usually shows MICE wins.
*   **New Category**: Create "Unknown" category for non-numerical (Categorical) data. Preserves the information that it was missing.
