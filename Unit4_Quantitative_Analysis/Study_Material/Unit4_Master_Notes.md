# Unit 4: Quantitative Techniques & Statistical Analysis - Master Guide

## 1. ANOVA (Analysis of Variance)
**ANOVA** is a collection of statistical models and their associated estimation procedures used to analyze the differences among means.

### 1.1 Why not multiple t-tests?
If Group A, Group B, Group C.
*   Pairs: (A vs B), (B vs C), (A vs C).
*   Problem: Multiple Testing Problem. The **Type I Error** (False Positive) rate increases with each test. $\alpha = 1 - (1 - 0.05)^k$.

### 1.2 One-Way ANOVA F-Test
*   **H0**: $\mu_1 = \mu_2 = \mu_3 = \dots = \mu_k$ (All means are equal).
*   **H1**: At least one mean is different.
*   **Equation**: $F = \frac{\text{Variance Between Groups}}{\text{Variance Within Groups}} = \frac{MS_{Between}}{MS_{Within}}$.
    *   If $F \gg 1$, the variation between groups is large relative to the variation within groups => Groups are distinct.

### 1.3 Bartlett's Test for Homogeneity of Variances
ANOVA assumes **Homogeneity of Variances** (all groups have roughly same spread).
*   **H0**: $\sigma_1^2 = \sigma_2^2 = \dots = \sigma_k^2$.
*   **H1**: At least one variance is different.
*   **Interpretation**: If p-value < 0.05, assume Heteroscedasticity. Use Welch’s ANOVA instead.

---

## 2. Probability Distributions
A **Probability Distribution** is a mathematical function that provides the probabilities of occurrence of different possible outcomes for an experiment.

### A. Discrete Distributions
1.  **Binomial Distribution**: Describes the number of successes ($k$) in $n$ independent Bernoulli trials (Success/Failure).
    *   *Real-World*: Flipping a coin 10 times. Number of customers buying a product (Conversion Rate).
2.  **Poisson Distribution**: Describes the number of events occurring in a fixed interval of time or space.
    *   *Real-World*: Calls per hour at a call center. Defects per meter of fabric.

### B. Continuous Distributions
1.  **Normal (Gaussian)**: Symmetric bell curve. Defined by $\mu$ (Mean) and $\sigma$ (Std Dev).
    *   *Real-World*: Heights, IQ Scores, Measurement Errors. "Central Limit Theorem" implies averages tend to be Normal.
2.  **Student's t-Distribution**: Like Normal but with heavier tails (more outliers). Used for small sample sizes ($n < 30$).
3.  **Exponential Distribution**: Describes the time between events in a Poisson process.
    *   *Real-World*: Time until next customer arrives. Time until a lightbulb fails.

---

## 3. Measures of Central Tendency
Summarizing a dataset with a single value that represents the center.

### A. Mean (Average)
1.  **Arithmetic Mean ($\bar{x}$ = $\sum x_i / n$)**: Standard average. Valid for Interval/Ratio data. Sensitive to outliers.
2.  **Geometric Mean ($GM = \sqrt[n]{x_1 \cdot x_2 \dots}$)**: Valid for positive Ratio data. Appropriate for **Growth Rates** (e.g., Investment returns: +10%, +50%).
3.  **Harmonic Mean ($HM = n / \sum(1/x_i)$)**: Appropriate for **Rates/Ratios** (e.g., Speed: km/h). Answers "Average Speed" correctly.

### B. Median
The middle value when data is sorted. Robust to outliers. Valid for Ordinal/Interval/Ratio.

### C. Mode
The most frequent value. Valid for Nominal (Categorical) data.

### D. Quartiles & Percentiles
*   **Quartiles**: Divide data into 4 equal parts (Q1=25%, Q2=Median, Q3=75%).
*   **Percentiles**: The value below which $P\%$ of observations fall. e.g., "99th Percentile" score means you beat 99% of students.

---

## 4. Measures of Dispersion
Describing the spread or variability of data.

### A. Range
*   **Range**: Max - Min. (Sensitive to outliers).
*   **Interquartile Range (IQR = Q3 - Q1)**: The spread of the middle 50%. (Robust).

### B. Variance & Standard Deviation
*   **Variance ($\sigma^2$)**: Average squared deviation from the mean.
*   **Std Deviation ($\sigma$)**: Square root of Variance. Same units as original data.
*   **Confidence Limit/Interval**: $\bar{x} \pm Z \times \frac{\sigma}{\sqrt{n}}$. E.g., "We are 95% confident the true mean is between 10.2 and 10.8."

### C. Relative Measures
*   **Coefficient of Variation (CV = $\sigma / \mu$)**: Unitless. Allows comparing variability of data with different units (e.g., Variability of Elephant Weight vs Ant Weight).
*   **Mean Absolute Deviation (MAD)**: Average absolute distance from mean. More robust than Variance.

---

## 5. Shape of Data: Skewness & Kurtosis
1.  **Skewness**: Asymmetry of the distribution.
    *   **Positive Skew**: Long tail on the Right (Mean > Median). e.g., Income Distribution.
    *   **Negative Skew**: Long tail on the Left (Mean < Median). e.g., Age at Death.
2.  **Kurtosis**: Tailedness (Wait in the tails).
    *   **Leptokurtic (High)**: Sharp peak, heavy tails. Prone to extreme outliers (Black Swan events).
    *   **Platykurtic (Low)**: Flat peak, light tails. Uniform-like.
