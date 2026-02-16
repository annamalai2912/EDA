# Unit 2: Introduction to Exploratory Data Analysis (EDA) - Master Guide

## 1. What is EDA?
**Exploratory Data Analysis (EDA)** is an approach/philosophy for data analysis that employs a variety of techniques (mostly graphical) to:
1.  Maximize insight into a data set.
2.  Uncover underlying structure.
3.  Extract important variables.
4.  Detect outliers and anomalies.
5.  Test underlying assumptions.
6.  Develop parsimonious models.
7.  Determine optimal factor settings.

Most EDA techniques are **graphical** in nature with a few quantitative techniques. The reason for the heavy reliance on graphics is that by its very nature the main role of EDA is to open-mindedly explore, and graphics gives the analyst unparalleled power to do so, enticing the data to reveal its structural secrets, and being always ready to gain some new, often unsuspected, insight into the data. In combination with the natural pattern-recognition capabilities that we all possess, graphics provides, of course, unparalleled power to do this.

---

## 2. Philosophy: EDA vs Classical vs Bayesian

### A. Classical Analysis
Sequence: **Problem => Data => Model => Analysis => Conclusions**
*   **Approach**: Assumes a specific model (e.g., "Data is Normally Distributed") based on theory *before* seeing the data.
*   **Focus**: Estimation (finding parameters like mean, variance) and Hypothesis Testing.
*   **Pros**: Rigorous, objective, widely accepted.
*   **Cons**: If the model assumption is wrong, the entire analysis is invalid. (e.g., Using Mean on skewed income data).

### B. Exploratory Data Analysis (EDA)
Sequence: **Problem => Data => Analysis => Model => Conclusions**
*   **Approach**: Does **not** assume a model initially. Uses graphs and summaries to let the data *suggest* the appropriate model.
*   **Focus**: Discovery, pattern recognition, anomaly detection.
*   **Pros**: Flexible, robust to outliers, uncovers hidden structures.
*   **Cons**: Subjective interpretation of graphs.

### C. Bayesian Analysis
Sequence: **Problem => Prior Distribution + Data => Posterior Distribution => Conclusions**
*   **Approach**: Incorporates prior knowledge/beliefs into the analysis.
*   **Focus**: Updating beliefs given new evidence.
*   **Pros**: Handles uncertainty well, utilizes domain knowledge.
*   **Cons**: Computationally expensive, sensitive to choice of Prior.

---

## 3. Underlying Assumptions in Data Analysis
Most statistical techniques (t-tests, ANOVA, Regression) rely on 4 key assumptions about the data. EDA's first job is to check these.

### 1. Randomness
*   **Assumption**: The data are a random sample from the population. Observations are independent.
*   **Violation**: Autocorrelation (Time Series), Cluster sampling bias.
*   **Consequence**: Standard Error estimates are too small, leading to false positives (Type I error).

### 2. Fixed Distribution
*   **Assumption**: The data come from a single, specific distribution family (usually Normal).
*   **Violation**: Mixture of distributions (Bimodal), Heavy tails (Cauchy).
*   **Consequence**: Mean and Std Dev are meaningless summaries.

### 3. Fixed Location
*   **Assumption**: The distribution has a constant mean (location parameter) over time/space.
*   **Violation**: **Drift**, Trend, Seasonality.
*   **Consequence**: The "average" value doesn't represent the process today vs yesterday.

### 4. Fixed Variation
*   **Assumption**: The distribution has a constant variance (scale parameter). Homoscedasticity.
*   **Violation**: **Heteroscedasticity** (Variance increases with time or value).
*   **Consequence**: Prediction intervals are wrong (too narrow or too wide).

---

## 4. Techniques for Testing Assumptions: The 4-Plot
The **4-Plot** is a powerful graphical technique to check all 4 assumptions simultaneously.

1.  **Run Sequence Plot** ($Y_i$ vs $i$):
    *   **Checks**: Fixed Location & Variation.
    *   **Look for**: Shifts in mean (Drift), changes in spread (Heteroscedasticity).
    *   **Ideal**: A flat, constant band of noise.

2.  **Lag Plot** ($Y_i$ vs $Y_{i-1}$):
    *   **Checks**: Randomness (Independence).
    *   **Look for**: Structure, loops, lines.
    *   **Ideal**: A structureless blob. If linear, there is Autocorrelation.

3.  **Histogram**:
    *   **Checks**: Distribution.
    *   **Look for**: Bell shape, skewness, multiple peaks (Bimodal).
    *   **Ideal**: Symmetric bell curve (for Normal assumption).

4.  **Normal Probability Plot (QQ Plot)**:
    *   **Checks**: Normality (specifically).
    *   **Look for**: Deviations from the straight line.
    *   **Ideal**: Points falling exactly on the red diagonal line.

---

## 5. Comparison of EDA with Classical Data Summary Measures
Classical measures (Mean, Std Dev) are **single numbers**. They collapse all information into a summary.
EDA uses **graphs** (Box Plot, Histogram) to show the **entire distribution**.

*   **Example**: Anscombe's Quartet. Four datasets with identical Mean, Variance, and Correlation, but completely different graphs.
    1.  Standard simple regression.
    2.  Non-linear curve (Parabola).
    3.  Linear with one massive outlier.
    4.  All x-values same, one outlier defines the line.
*   **Lesson**: "Always plot your data." Summary statistics can lie.

## 6. Graphical Representation of Data
*   **Unidimensional**: Histogram, Box Plot, Stem-and-Leaf, Density Plot. (Shows distribution of 1 variable).
*   **Bidimensional**: Scatter Plot, Lag Plot, Box Plot by Group. (Shows relationship between 2 variables).
*   **Multidimensional**: Parallel Coordinates, Scatter Plot Matrix (Pairplot), 3D Scatter, Glyphs/Chernoff Faces. (Shows interaction of 3+ variables).
