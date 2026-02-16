
# Unit 4: Quantitative Data Analysis & Distributions

## 1. ANOVA (Analysis of Variance)
**ANOVA** is a statistical method used to test differences between two or more means. It determines whether there are any statistically significant differences between the means of three or more independent (unrelated) groups.
*   **H0 (Null Hypothesis)**: All group means are equal.
*   **H1 (Alternative Hypothesis)**: At least one group mean is different.

## 2. Bartlett's Test
**Bartlett's Test** is used to test if multiple samples have equal variances (Homogeneity of Variances). It is sensitive to departures from normality.
*   **Why use it?** ANOVA assumes equal variances across groups. Bartlett's test checks this assumption *before* running ANOVA.

## 3. Probability Distributions
A **Probability Distribution** lists all possible outcomes of a random variable and their corresponding probabilities.
*   **Discrete Distributions**:
    *   **Binomial**: Number of successes in $n$ trials (Bernoulli trials).
    *   **Poisson**: Number of events occurring in a fixed interval of time/space.
*   **Continuous Distributions**:
    *   **Normal (Gaussian)**: Bell curve, defined by $\mu$ (mean) and $\sigma$ (std dev).
    *   **Uniform**: All outcomes are equally likely.
    *   **Exponential**: Time between events in a Poisson process.

## 4. Location and Scale Parameters
*   **Location Parameter**: Determines the "center" or shift of the distribution (e.g., Mean $\mu$).
*   **Scale Parameter**: Determines the "spread" or stretch of the distribution (e.g., Std Dev $\sigma$).

## 5. Measures of Central Tendency & Dispersion
*   **Central Tendency**: Mean (Arithmetic, Geometric, Harmonic), Median, Mode.
*   **Dispersion**: Range, Variance, Standard Deviation, Interquartile Range (IQR).
*   **Confidence Limit/Interval**: A range of values derived from sample statistics that is likely to contain the value of an unknown population parameter (with a certain confidence level, e.g., 95%).
    *   $CI = \bar{x} \pm Z \times \frac{\sigma}{\sqrt{n}}$

## 6. Skewness and Kurtosis (Symmetry/Concentration)
*   **Skewness**: Measure of asymmetry.
    *   **Positive Skew**: Tail on the right (Mean > Median).
    *   **Negative Skew**: Tail on the left (Mean < Median).
*   **Kurtosis**: Measure of "tailedness" or peakiness.
    *   **Leptokurtic**: High peak, heavy tails (Outlier prone).
    *   **Platykurtic**: Flat peak, light tails.
