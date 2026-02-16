# BCA 3rd Year Data Science - Unit 3: Exploratory Data Analysis (EDA)

This repository is split into two main sections: **Simple Basics** for foundational learning and **Complex Advanced** for deeper understanding and real-world application.

## Folder Structure

### 1. Simple Basics (`Practical_Scripts/Simple_Basics/`)
Designed to understand core concepts one by one.

*   `01_eda_basics.py`: Introductory script (Summary Statisitics + Basic Plots).
*   `02_basic_plots_stats.py`: Simple descriptive statistics (Mean, Median, Mode) and basic histograms/scatter plots.
*   `03_cleaning_intro.py`: Basic data cleaning (finding nulls, dropping duplicates).
*   `04_outlier_detection_iqr.py`: Detecting outliers using the Interquartile Range (IQR) method.

### 2. Complex Advanced (`Practical_Scripts/Complex_Advanced/`)
Designed for professional-level analysis and tackling complex problems.

*   `01_advanced_eda_pipeline.py`: A class-based Python script that automates data cleaning, consistency checks, and multivariate analysis. Included time series decomposition.
*   `02_autocorrelation_advanced.py`: Deep dive into time series patterns (AR, MA, Seasonality).
*   `03_data_handling_advanced.py`: Handling dirty data with regex, consistency checks, and pollution.
*   `04_time_series_decomposition.py`: Seasonal decomposition of time series into Trend, Seasonality, and Residual components.
*   `05_advanced_imputation.py`: Comparing advanced missing value imputation techniques (KNN, MICE/Iterative) against ground truth using RMSE.

## Study Material (`Study_Material/`)

*   `Unit3_EDA_Questions_Answers.md`: Quick revision Q&A.
*   `Detailed_Study_Notes.md`: In-depth textbook-style notes covering every syllabus topic including data access issues, consistency, pollution, and missing patterns.
*   `Resources.md`: Links to books and tutorials.

## How to Run

1.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Simple Scripts:**
    ```bash
    cd Practical_Scripts/Simple_Basics
    python 01_eda_basics.py
    ```

3.  **Run Advanced Scripts:**
    ```bash
    cd ../Complex_Advanced
    python 01_advanced_eda_pipeline.py
    ```
