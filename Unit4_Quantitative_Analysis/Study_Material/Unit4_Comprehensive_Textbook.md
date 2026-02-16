# Unit 4: Data Analysis & Quantitative Techniques - Comprehensive Textbook

## Table of Contents
1.  **Introduction to Quantitative Data Analysis**
    *   Descriptive vs Inferential Focus
    *   The Role of Summary Statistics
2.  **Probability Distributions**
    *   Discrete Distributions (Binomial, Poisson)
    *   Continuous Distributions (Normal, t-Student, Exponential, Gamma, Beta, Weibull)
    *   Location and Scale Parameters
    *   Estimation of Parameters (Maximum Likelihood vs Method of Moments)
3.  **Analysis of Variance (ANOVA)**
    *   The F-Test Logic: Between-Group vs Within-Group Variance
    *   One-Way ANOVA Assumptions
    *   Interpreting the F-statistic and P-value
4.  **Bartlett's Test for Homogeneity of Variances**
    *   The Assumption of Homoscedasticity
    *   The Bartlett's Test Statistic $B$
    *   Levene's Test (Robust Alternative)
5.  **Measures of Central Tendency**
    *   Characteristics of a Good Average
    *   Arithmetic Mean (Raw vs Grouped Data)
    *   Geometric Mean (For Growth Rates)
    *   Harmonic Mean (For Speed/Rates)
    *   Median (Robustness)
    *   Mode (For Categorical Data)
    *   Quantiles and Percentiles ($P_k$)
6.  **Measures of Dispersion (Spread)**
    *   Absolute vs Relative Measures
    *   Range and Interquartile Range (IQR)
    *   Mean Deviation and Mean Absolute Deviation (MAD)
    *   Variance ($\sigma^2$) and Standard Deviation ($\sigma$)
    *   Coefficient of Variation (CV)
    *   Standard Error of the Mean (SEM)
7.  **Measures of Shape & Concentration**
    *   Skewness (Symmetry)
    *   Kurtosis (Peakedness/Tail Weight)
    *   Moments of a Distribution
8.  **Confidence Limits & Robustness**
    *   Confidence Interval for Mean
    *   Confidence Interval for Variance
    *   Robustness of Parameters (Trimmed Mean, Median)

---

## 1. Introduction to Quantitative Data Analysis

Quantitative analysis focuses on summarizing numerical data to describe phenomena or test hypotheses. While EDA (Unit 2) is visual, Quantitative Analysis is **computational**.

### The Role of Summary Statistics
Summary statistics condense large datasets into single numbers (parameters) that capture key properties:
1.  **Center**: Where is the data located?
2.  **Spread**: How variable is the data?
3.  **Shape**: Is it symmetric or skewed?

---

## 2. Probability Distributions

A probability distribution describes the likelihood of different outcomes.

### 2.1 Discrete Distributions
*   **Binomial Distribution ($n, p$)**:
    *   Describes the number of successes $k$ in $n$ independent Bernoulli trials (Success/Failure).
    *   $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$.
    *   *Real-World*: Coin flips, Conversion rates, Defective items in a batch.
*   **Poisson Distribution ($\lambda$)**:
    *   Describes the number of events occurring in a fixed interval of time or space.
    *   $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$.
    *   *Real-World*: Calls per hour, typos per page, earthquakes per year.

### 2.2 Continuous Distributions
*   **Normal (Gaussian) Distribution ($\mu, \sigma$)**:
    *   Steps: Symmetrical bell curve. Defined solely by Mean and Variance.
    *   *Importance*: Central Limit Theorem (CLT) states that sums/averages of random variables tend toward Normality.
*   **Student's t-Distribution ($df$)**:
    *   Similar to Normal but with heavier tails. Used when sample size is small ($n < 30$) or $\sigma$ is unknown.
*   **Exponential Distribution ($\lambda$)**:
    *   Describes the time *between* events in a Poisson process. Memoryless property.
    *   $f(x) = \lambda e^{-\lambda x}$.
    *   *Real-World*: Time until next customer, time until radioactive decay.

### 2.3 Parameters
*   **Location Parameter**: Determines the "position" or shift of the distribution (e.g., Mean $\mu$).
    *   Shifting $\mu$ moves the curve Left/Right.
*   **Scale Parameter**: Determines the "spread" or stretch (e.g., Std Dev $\sigma$).
    *   Increasing $\sigma$ flattens the curve.
*   **Shape Parameter**: Affects skewness/kurtosis (e.g., $\alpha$ in Gamma dist).

### 2.4 Estimation
*   **Method of Moments (MOM)**: Equate sample moments (mean, variance) to population moments. Simple but less efficient.
*   **Maximum Likelihood Estimation (MLE)**: Find parameters that maximize the likelihood of observing the data. Standard in modern statistics.

---

## 3. Analysis of Variance (ANOVA)

**ANOVA** tests if the means of 3+ groups are significantly different.

### The F-Test Logic
$F = \frac{\text{Variance Between Groups}}{\text{Variance Within Groups}} = \frac{MS_{Between}}{MS_{Within}}$

1.  **Between-Group Variance**: How far are group means ($\bar{x}_1, \bar{x}_2...$) from the Grand Mean ($\bar{\bar{x}}$)? (Signal).
2.  **Within-Group Variance**: How spread out is the data *inside* each group? (Noise).

**Interpretation**:
*   If $F \gg 1$: Groups are far apart relative to their internal noise. Reject $H_0$. (Groups are different).
*   If $F \approx 1$: Groups overlap significantly. Fail to reject $H_0$.

### Assumptions
1.  **Normality**: Residuals are normally distributed.
2.  **Homogeneity of Variances**: All groups have roughly equal spread (Homoscedasticity).
3.  **Independence**: Observations are independent.

---

## 4. Bartlett's Test (Assumption Check)

Before running ANOVA, you MUST check if assumption #2 (Equal Variances) holds.

### Bartlett's Test
*   **Hypotheses**:
    *   $H_0: \sigma_1^2 = \sigma_2^2 = \dots = \sigma_k^2$
    *   $H_1: \sigma_i^2 \neq \sigma_j^2$ (At least one variance is different).
*   **Statistic**: $B = \frac{(N-k) \ln(S_p^2) - \sum(n_i-1)\ln(S_i^2)}{1 + \frac{1}{3(k-1)} (\sum \frac{1}{n_i-1} - \frac{1}{N-k})}$
*   **Sensitivity**: Very sensitive to Non-Normality. If data is non-normal, use **Levene's Test** instead.

---

## 5. Measures of Central Tendency

### 5.1 Arithmetic Mean ($\bar{x}$)
*   **Raw Data**: $\frac{\sum x}{n}$
*   **Grouped Data**: $\frac{\sum f_i m_i}{\sum f_i}$ where $m_i$ is class midpoint.
*   **Pros**: Uses all data points. Mathematical properties allow algebra.
*   **Cons**: Highly sensitive to outliers. (e.g., Bill Gates walks into a bar -> Average income skyrockets).

### 5.2 Geometric Mean (GM)
*   **Formula**: $\sqrt[n]{x_1 \cdot x_2 \cdot \dots \cdot x_n}$ or $\text{antilog}(\frac{1}{n} \sum \log x_i)$.
*   **Use Case**: Averaging ratios, percentages, or growth rates.
*   *Example*: Investment grows +10%, then +50%, then -10%. Arithmetic mean is misleading. GM gives the correct Compound Annual Growth Rate (CAGR).

### 5.3 Harmonic Mean (HM)
*   **Formula**: $\frac{n}{\sum \frac{1}{x_i}}$.
*   **Use Case**: Averaging rates/speeds.
*   *Example*: Speed. Outward 60km/h, Return 40km/h. Distance is same. Average speed is NOT 50. It is 48km/h. HM handles this.

### 5.4 Median
*   The middle value ($50^{th}$ Percentile).
*   **Robust**: Unaffected by extreme outliers.
*   **Calculation**:
    *   Sort data.
    *   If $n$ is odd, middle value.
    *   If $n$ is even, average of two middle values.

### 5.5 Mode
*   Most frequent value.
*   Only measure valid for **Nominal Data**.
*   Datasets can be Bimodal (2 modes) or Multimodal.

---

## 6. Measures of Dispersion (Spread)

### 6.1 Range & IQR
*   **Range**: $Max - Min$. (Uses only 2 points. Very sensitive).
*   **IQR**: $Q3 - Q1$. (Spread of middle 50%. Robust).

### 6.2 Standard Deviation ($\sigma$) & Variance ($\sigma^2$)
*   **Variance**: The average *squared* distance from the mean.
    *   Population: $\frac{\sum(x-\mu)^2}{N}$
    *   Sample: $\frac{\sum(x-\bar{x})^2}{n-1}$ (Bessel's Correction for bias).
*   **Std Deviation**: $\sqrt{\text{Variance}}$.
    *   Bring units back to original scale (e.g., from $\$^2$ to $\$$).
    *   **Rule of Thumb**: For Normal dist, 68% of data is within $\pm 1\sigma$, 95% within $\pm 2\sigma$.

### 6.3 Coefficient of Variation (CV)
*   **Formula**: $\frac{\sigma}{\mu} \times 100\%$.
*   **Use Case**: Comparing relative variability of datasets with different units.
    *   e.g., Variability of Elephant weights (mean=5000kg, std=500kg) vs Ant weights (mean=0.01g, std=0.005g).
    *   Elephant CV = 10%. Ant CV = 50%. Ants are relatively more variable!

---

## 7. Measures of Shape: Skewness & Kurtosis

### 7.1 Skewness ($S_k$)
Measures asymmetry around the mean.
*   **Symetric**: $S_k = 0$ (Normal Dist). Mean = Median.
*   **Positive Skew (Right-tailed)**: $S_k > 0$. Tail extends right. Mean > Median.
    *   *Example*: Income distributions, Housing prices. (High values pull the mean up).
*   **Negative Skew (Left-tailed)**: $S_k < 0$. Tail extends left. Mean < Median.
    *   *Example*: Age at death, Test scores on an easy exam.

### 7.2 Kurtosis ($K_u$)
Measures "tailedness" (probability of extreme values).
*   **Mesokurtic**: $K_u = 3$ (Normal Dist). (Excess Kurtosis = 0).
*   **Leptokurtic**: $K_u > 3$. Sharp peak, fat tails.
    *   *Implication*: Outliers are more frequent than Normal. High risk in finance.
*   **Platykurtic**: $K_u < 3$. Flat peak, thin tails.
    *   *Implication*: Outliers are rare. Uniform-like.

---

## 8. Confidence Limits

### Confidence Interval for Mean ($CI_{\mu}$)
Range of values that likely contains the true population mean.
*   Upper Limit: $\bar{x} + Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$
*   Lower Limit: $\bar{x} - Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$
*   Interpretation: "We are 95% confident that the interval [10, 20] captures the true mean."
*   Note: As $n$ increases, the interval shrinks (Estimate becomes more precise).

### Confidence Interval for Variance ($CI_{\sigma^2}$)
Based on Chi-Square distribution ($\chi^2$).
*   Lower: $\frac{(n-1)s^2}{\chi^2_{upper}}$
*   Upper: $\frac{(n-1)s^2}{\chi^2_{lower}}$
*   Note: Not symmetric around the sample variance.
