# Unit 3: Data Analysis Tools & Techniques - Comprehensive Textbook

## Table of Contents
1.  **Introduction to Data Analysis Tools & Techniques**
    *   The Data Analysis Process Pipeline
    *   Formulating Analysis Questions
    *   Exploratory Data Analysis (EDA) Techniques
2.  **Data Discovery and Access**
    *   Finding the Right Data (Internal vs External)
    *   Issues Related with Data Access (Security, Format, Volume, Latency)
    *   Data Dictionary & Metadata
3.  **Data Characterization**
    *   Understanding Structure (Dimensions, Types)
    *   Statistical Summary (Describe)
4.  **Data Quality Issues: Consistency & Pollution**
    *   Data Consistency (Logical Rules)
    *   Data Pollution (Erroneous/Irrelevant Data)
    *   Handling Duplicate or Redundant Variables (Multicollinearity)
5.  **Outliers and Leverage Data**
    *   Definition of Outliers vs. Leverage Points
    *   Influence: Cook's Distance
    *   Detection Techniques (IQR, Z-Score, Grubbs' Test)
    *   Impact on Models
6.  **Noisy Data**
    *   Sources of Noise
    *   Smoothing Techniques (Moving Average, Binning)
7.  **Autocorrelation Analysis**
    *   Autocorrelation Function (ACF) Plot
    *   Interpreting Random Data
    *   Interpreting Moderate Correlation
    *   Interpreting Strong Autoregressive Correlation
    *   Interpreting Sinusoidal Correlation (Seasonality)
8.  **Handling Missing Values**
    *   The Importance of Missing Data
    *   Missing Data Mechanisms (MCAR, MAR, MNAR)
    *   Imputation Techniques for Numerical Data (Mean, Median, KNN, MICE)
    *   Imputation Techniques for Categorical Data (Mode, New Category)
    *   When to Drop vs. When to Impute

---

## 1. Introduction to Data Analysis Tools & Techniques

### The Data Analysis Process Pipeline
Data Analysis is not a single step but a pipeline:
1.  **Objective Definition**: What business problem are we solving?
2.  **Data Discovery**: Creating a catalog of potential data sources.
3.  **Data Ingestion**: Extracting data (ETL).
4.  **Data Preparation (Cleaning)**: Handling missing values, outliers, formats.
5.  **Exploratory Data Analysis (EDA)**: Understanding distributions and relationships.
6.  **Modeling**: Building statistical or ML models.
7.  **Communication**: Visualizing and reporting results.

### EDA Techniques
EDA relies heavily on visual methods but also employs quantitative techniques.
*   **Uni-variate**: Analysis of one variable at a time (Histogram, Box Plot, Summary Stats).
*   **Bi-variate**: Analysis of two variables (Scatter Plot, Correlation Matrix).
*   **Multi-variate**: Analysis of three or more variables (PCA, Manifold Learning).

### Formulating Analysis Questions
Good analysis starts with good questions.
*   **Descriptive Questions**: "What was the average sales in Q1?" (Measures Central Tendency).
*   **Exploratory Questions**: "Does sales correlate with marketing spend?" (Measures Association).
*   **Inferential Questions**: "Did the marketing campaign *cause* the sales increase?" (Measures Causality - requires A/B testing).
*   **Predictive Questions**: "What will sales be next month?" (Forecasting).

---

## 2. Data Discovery and Access

### Finding Data
*   **Internal Data**: Transaction logs, CRM database, Web server logs.
*   **External Data**: Weather API, Social Media firehose, Census data.

### Issues Related with Data Access
1.  **Security & Privacy**:
    *   **PII (Personally Identifiable Information)**: Names, SSNs, Biometrics. Must be hashed or removed (GDPR/HIPAA compliance).
    *   **Access Control**: Who has permission to view this data? (Role-Based Access Control).
2.  **Format Incompatibility**:
    *   Data exists in silos: SQL DB, MongoDB (JSON), CSVs on share drives, PDFs.
    *   **ETL (Extract, Transform, Load)** pipelines are needed to unify formats.
3.  **Volume**:
    *   "Big Data" cannot fit in RAM. Tools like Spark or Dask are needed.
    *   Sampling becomes necessary for initial EDA.
4.  **Latency**:
    *   Real-time streaming data (Kafka) vs Batch processing (Nightly jobs).
    *   Analysis on stale data can lead to wrong decisions.

---

## 3. Data Characterization

### Understanding Structure
Before diving into analysis, characterize the dataset:
*   **Dimensions**: Number of rows ($n$) and columns ($p$). High $p$ (High Dimensionality) brings the "Curse of Dimensionality".
*   **Data Types**: Integer, Float, Boolean, Categorical, Datetime. (Pandas `df.info()`).
    *   *Issue*: Numeric columns stored as strings ("1,000" vs 1000).

---

## 4. Data Quality Issues: Consistency & Pollution

### Data Consistency
Consistency means data follows logical rules and constraints.
The data must be physically possible.
*   **Temporal Consistency**: "End Time" must be > "Start Time". "Date of Death" > "Date of Birth".
*   **Cross-Field Consistency**: If `Age < 18`, then `Driver_License` should be `False` (usually).
*   **Domain Constraints**: `Percentage` must be 0-100. `Height` cannot be negative.

### Data Pollution
Pollution refers to the presence of erroneous, garbage, or irrelevant data that dilutes the analysis.
*   **Test Data**: Engineers leaving `test_user_1`, `test_user_2` in production DB.
*   **System Values**: Default values like `1970-01-01` (Unix Epoch) or `-999`.
*   **Encoding Errors**: `Ã©` instead of `é`.

### Duplicate or Redundant Variables
*   **Duplicates**: Identical rows. Inflate sample size $n$ artificially.
    *   *Solution*: `df.drop_duplicates()`.
*   **Redundant Variables**: Two variables that carry the same information (Perfect Multicollinearity).
    *   *Example*: `Temperature_C` and `Temperature_F`. correlation $r = 1.0$.
    *   *Example*: `Birth_Year` and `Age` (if `Current_Year` is fixed).
    *   *Impact*: Causes singularity in matrix inversion for Regression.
    *   *Solution*: Keep one, drop the rest.

---

## 5. Outliers and Leverage Data

### Definitions
*   **Outlier**: An observation with an unusual value for the response variable ($Y$) given the predictors ($X$). It has a large **Residual**.
*   **Leverage Point**: An observation with an extreme value for the predictor variable ($X$). It is far from the mean of $X$.
    *   *High Leverage*: Far from the center of the X-space.
    *   *Good Leverage*: Points that follow the regression line, increasing precision.
    *   *Bad Leverage (Influential Point)*: Points that are far from the center *and* do not follow the trend. They pull the regression line towards them.

### Cook's Distance
A measure of the influence of a data point. It combines Leverage and Residual size.
*   $D_i = \frac{\sum(\hat{Y}_j - \hat{Y}_{j(i)})^2}{p \cdot MSE}$.
*   Basically: "How much does the model change if I delete this point?"
*   Rule of Thumb: $D_i > 4/n$ indicates an influential point.

### Detection Techniques
1.  **IQR Method**: $X < Q1 - 1.5 \cdot IQR$ or $X > Q3 + 1.5 \cdot IQR$. (Robust).
2.  **Z-Score**: $|Z| > 3$. (Assumes Normality. Sensitive to outliers).
3.  **Grubbs' Test**: Hypothesis test for a single outlier in univariate normal data.

---

## 6. Noisy Data

**Noise** is random error or variance in a measured variable. It obscures the underlying relationship (Signal).
*   **Sources**: Sensor imprecision, quantization error, transmission interference.
*   **Smoothing Techniques**:
    1.  **Moving Average**: Replace $X_t$ with mean of $(X_{t-1}, X_t, X_{t+1})$. Reduces variance but blurs sharp edges.
    2.  **Binning**: Grouping continuous values into bins (Histogram approach).
    3.  **LOESS (Locally Estimated Scatterplot Smoothing)**: Regression fit to localized subsets of data.

---

## 7. Autocorrelation Analysis

**Autocorrelation** occurs when a variable is correlated with itself over successive time intervals. It violates the assumption of independence.

### Autocorrelation Function (ACF) Plot
A bar chart/stem plot showing correlation coefficients ($r$) at lag $k=1, 2, 3...$.

### Interpreting Patterns
1.  **Random Data (White Noise)**:
    *   ACF at Lag 0 is always 1.
    *   ACF at Lag $k > 0$ is near zero (randomly fluctuates within 95% confidence bands).
    *   *Implication*: No prediction is possible.

2.  **Moderate Correlation**:
    *   ACF values drop off slowly.
    *   *Implication*: Short-term dependence exists. Moving Average models might work.

3.  **Strong Autoregressive Correlation (AR1)**:
    *   Lag 1 is high (e.g., 0.9).
    *   Lag 2 is $0.9^2 = 0.81$.
    *   Lag 3 is $0.9^3 = 0.729$.
    *   Exponential decay.
    *   *Implication*: Today heavily depends on Yesterday. $Y_t = \phi Y_{t-1} + \epsilon$.

4.  **Sinusoidal Correlation (Seasonality)**:
    *   ACF shows a wave pattern (Sine wave).
    *   Positive peaks at Lag $S, 2S, 3S$ (e.g., 12 months, 24 months).
    *   Negative troughs at $S/2$.
    *   *Implication*: Seasonal pattern exists. Data must be de-seasonalized (Differencing).

---

## 8. Handling Missing Values

### Mechanisms of Missingness (Why is it missing?)
These determine the safe handling strategy.
1.  **MCAR (Missing Completely at Random)**:
    *   The probability of missingness is unrelated to any observed or unobserved data. It's random (e.g., a server crash).
    *   *Safe*: Listwise Deletion (dropping rows).
2.  **MAR (Missing at Random)**:
    *   Missingness is related to **Observed** data. (e.g., Women (observed) are less likely to report Weight (missing)).
    *   *Safe*: Imputation (predict Weight using Gender).
3.  **MNAR (Missing Not at Random)**:
    *   Missingness is related to the **Unobserved** value itself. (e.g., Obese people are less likely to report Weight).
    *   *Dangerous*: Simple imputation biases the result (underestimates obesity). Requires explicit modeling of the missingness mechanism.

### Imputation Techniques
1.  **Mean/Median Imputation**:
    *   Fill with overall mean.
    *   *Pros*: Simple. Preserves mean.
    *   *Cons*: Underestimates variance (Std Dev shrinks). Distorts correlation between variables.
2.  **Mode Imputation**:
    *   For categorical data. Fill with most frequent category.
3.  **K-Nearest Neighbors (KNN)**:
    *   Find $k$ most similar rows (using other columns) and take their average.
    *   *Pros*: More accurate. Preserves local structure.
    *   *Cons*: Computationally expensive ($O(n^2)$).
4.  **MICE (Multivariate Imputation by Chained Equations)**:
    *   Iterative regression. Predict column A using B+C. Then Predict B using A+C. Repeat.
    *   *Pros*: State-of-the-art accuracy. Handles uncertainty.
5.  **New Category Strategy**:
    *   For categorical data, create a "Missing"/"Unknown" label.
    *   *Pros*: The fact that data is missing might be a predictor itself! (e.g., Missing Credit Score -> High Risk).

### Handling Non-Numerical Data in Missing Places
*   **Most Frequent Category**: Simple but biases the mode.
*   **Predictive Model (Classifier)**: Use Logistic Regression/Decision Tree to classify the missing category based on other features.
*   **"Unknown" Token**: Often the safest bet, as it makes no assumptions.
