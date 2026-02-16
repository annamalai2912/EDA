
# BCA 3rd Year Data Science - Complete Semester Resources

This repository is designed to be the definitive resource for your 3rd Year Data Science course. It covers every single topic mentioned in your syllabus, from basic data types to advanced simulations and case studies.

## 📂 Folder Structure & Syllabus Mapping

### **Unit 1: Introduction to Data & Its Types**
*   **Concepts Covered:**
    *   **Data Classification**: Cross-Sectional, Time Series, Panel Data.
    *   **Levels of Measurement**: Nominal, Ordinal, Interval, Ratio.
    *   **Sampling**: Population vs Sample, Statistic vs Parameter.
*   **Practical Scripts (`Unit1_Intro_Data_Types/Practical_Scripts/`):**
    *   `data_classification.py`: Generates different data types and Frequency Distributions.
    *   `Basic_Levels/02_levels_of_measurement.py`: Demonstrates allowed operations on Nominal vs Ratio data.

### **Unit 2: Introduction to Exploratory Data Analysis (EDA)**
*   **Concepts Covered:**
    *   **Philosophy**: EDA vs Classical Analysis vs Bayesian.
    *   **Assumptions**: Randomness, Fixed Location, Fixed Variation, Fixed Distribution.
    *   **Tools**: The 4-Plot (Run Sequence, Lag, Histogram, Normal Probability Plot).
*   **Practical Scripts (`Unit2_Intro_EDA_Assumptions/Practical_Scripts/`):**
    *   `4_plot_assumptions.py`: Implements the 4-Plot to test assumptions using Scipy and Matplotlib.
    *   `Basic_EDA/03_assumptions_and_philosophy.py`: Visualizes Drift, Spread, and Autocorrelation violations.

### **Unit 3: Data Analysis Tools (Deep Dive)**
*   **Concepts Covered:**
    *   **EDA Techniques**: Autocorrelation (Random, Moderate, AR1, Sinusoidal).
    *   **Data Quality**: Pollution, Consistency, Redundancy.
    *   **Missing Data**: MCAR, MAR, MNAR patterns an Imputation (Mean, Median, KNN, MICE).
    *   **Outliers**: Detection via IQR, Z-Score, and Robust MAD.
    *   **Influence**: Leverage Points vs Outliers (Cook's Distance).
*   **Practical Scripts (`Unit3_EDA/Practical_Scripts/`):**
    *   `Complex_Advanced/01_advanced_eda_pipeline.py`: Comprehensive automated cleaning pipeline.
    *   `Complex_Advanced/02_autocorrelation_advanced.py`: Generates specific autocorrelation patterns.
    *   `Complex_Advanced/05_advanced_imputation.py`: Compares imputation techniques.
    *   `Complex_Advanced/06_leverage_vs_outlier.py`: Visualizes Cook's Distance.
    *   `Complex_Advanced/07_missing_pattern_analysis.py`: Visualizes missing data patterns (Matrix, Heatmap).
    *   `Basic_Detection/04_outlier_strategies.py`: Compares IQR vs Z-Score vs MAD.

### **Unit 4: Quantitative Data Analysis**
*   **Concepts Covered:**
    *   **Statistical Tests**: ANOVA, Bartlett’s Test (Homogeneity of Variances).
    *   **Distributions**: Normal, T, Exponential, Binomial.
    *   **Measures**: Central Tendency (Geometric/Harmonic Mean), Dispersion (MAD, CV, IQR).
    *   **Shape**: Skewness and Kurtosis.
*   **Practical Scripts (`Unit4_Quantitative_Analysis/Practical_Scripts/`):**
    *   `anova_distributions.py`: Performs ANOVA and Bartlett's Test.
    *   `Advanced_Measures/02_advanced_central_tendency.py`: Deep dive into Geometric Mean, Harmonic Mean, and Dispersion (MAD, CV).

### **Unit 5: Simulations & Case Studies**
*   **Concepts Covered:**
    *   **Simulations**: Random Walk, Standard Resistor, Heat Flow Meter.
    *   **Bivariate Analysis**: Chi-Square Test, Contingency Tables, Phi Coefficient.
    *   **Correlation**: Pearson, Spearman Rank, Kendall Tau.
*   **Practical Scripts (`Unit5_Simulations_CaseStudies/Practical_Scripts/`):**
    *   `simulations_correlations.py`: 1D Random Walk, Chi-Square, and Rank Correlations.
    *   `Specific_Cases/02_case_studies_resistor_heat.py`: Specific simulations for Standard Resistor (QC) and Heat Flow Meter (Calibration).

## 🚀 How to Use Specifically for Exams/Labs

1.  **For Lab Experiment 1 (Data Types):** Run `Unit1.../data_classification.py`.
2.  **For Lab Experiment 2 (EDA Assumptions):** Run `Unit2.../4_plot_assumptions.py`.
3.  **For Lab Experiment 9 (Imputation):** Run `Unit3.../05_advanced_imputation.py`.
4.  **For Lab Experiment 4 (ANOVA):** Run `Unit4.../anova_distributions.py`.
5.  **For Case Studies:** Run `Unit5.../Specific_Cases/02_case_studies_resistor_heat.py`.

## 📚 Study Resources

Each Unit contains a `Study_Material` folder with:
*   `UnitX_Notes.md`: Comprehensive theoretical notes.
*   `Resources.md`: Links to textbooks (Tukey, Peng) and articles.

## Requirements

Install the complete data science stack:
```bash
pip install numpy pandas matplotlib seaborn scipy statsmodels plotly scikit-learn missingno
```
