# Unit 5: Simulations & Case Studies - Master Guide

## 1. Simulations: EDA Case Studies

### A. Random Walk Simulation (1D)
A **Random Walk** is a mathematical object, known as a stochastic or random process, that describes a path that consists of a succession of random steps on some mathematical space such as the integers.
*   **Simple Random Walk**: 
    1.  Start at $X_0 = 0$.
    2.  At each time $t$, move $+1$ with probability $0.5$ or $-1$ with probability $0.5$.
    3.  $X_t = X_{t-1} + \epsilon_t$.
*   **Case Study Importance**: Models stock prices (Efficient Market Hypothesis), molecular diffusion (Brownian Motion), genetic drift.
*   **Key Insight**: $E[X_t] = 0$, but variance $\text{Var}(X_t) = t$. The longer you walk, the further you *can* stray from zero (Diffusion).

### B. Standard Resistor Simulation (Quality Control)
This case study involves analyzing the distribution of resistance values in a batch of resistors. Resistors have a **nominal value** (e.g., 1000 $\Omega$) and a **tolerance** (e.g., $\pm 5\%$).
*   **Objective**: Verify if the **process capability** index ($CpK$) is sufficient. Is the manufacturing process producing parts within specification limits (LSL, USL)?
*   **Key Insight**: If the distribution is skewed or shifted (Mean $\neq$ Nominal), the process is "Out of Control".

### C. Heat Flow Meter (Calibration Curve)
Calibration of a heat flow meter involves measuring heat flux ($q$) vs thermocouple output ($V$).
*   **Model**: $q = C \cdot V + \text{Intercept}$.
*   **Objective**: Determine the **sensitivity** ($C$) and check for **non-linearity** (Sensor Saturation).
*   **Key Insight**: Residual Analysis is critical. If residuals show a U-shape, the linear model is invalid (Sensor is non-linear).

---

## 2. Bivariate Distributions & Association

### A. Nominal Variables: Chi-Square Test & Phi Coefficient
How do we measure association between two categorical variables (e.g., Gender vs Voting Preference)?
1.  **Chi-Square Test of Independence ($\chi^2$)**: Compares Observed Frequencies ($O$) vs Expected Frequencies ($E$) under the assumption of independence.
    *   $\chi^2 = \sum \frac{(O - E)^2}{E}$.
    *   Degrees of Freedom: $(R-1)(C-1)$.
    *   If $\chi^2 > \text{Critical Value}$, reject Independence.
2.  **Phi Coefficient ($\phi$)**: A **measure of effect size** for 2x2 tables.
    *   $\phi = \sqrt{\frac{\chi^2}{n}}$. Range: $[0, 1]$.
    *   Similar to Correlation Coefficient $r$ but for nominal data.

### B. Ordinal Variables: Spearman & Kendall
How do we measure association between two ranked variables (e.g., Exam Rank vs IQ Rank)?
1.  **Spearman Rank Correlation ($\rho$)**: Pearson correlation on the *ranks* of the data.
    *   **Monotonic Relationship**: Captures non-linear but strictly increasing relationships (e.g., $Y = X^2$).
    *   **Robustness**: Not affected by outliers (since outliers are just ranked "highest").
2.  **Kendall’s Tau ($\tau$)**: Based on concordant and discordant pairs.
    *   For any pair of observations $(x_i, y_i)$ and $(x_j, y_j)$:
        *   **Concordant** if $(x_i - x_j)(y_i - y_j) > 0$. (Both increase).
        *   **Discordant** if $(x_i - x_j)(y_i - y_j) < 0$. (One increases, one decreases).
    *   $\tau = \frac{C - D}{\frac{1}{2}n(n-1)}$.
    *   **Key Insight**: Interpretation is probability-based. "Probability of observing agreement minus disagreement."

### C. Interval/Ratio Variables: Pearson Correlation
1.  **Pearson Correlation ($r$)**: Measures linear strength.
    *   Range: $[-1, +1]$.
    *   **Limitation**: Sensitive to outliers. Only captures linear relationships. (Anscombe's Quartet).

---

## 3. Scatter Plot & Causal Interpretations
*   **Scatter Plot**: Visualizes relationship between two quantitative variables.
*   **Correlation does not imply Causation**:
    *   *Spurious Correlation*: Ice cream sales correlate with drowning deaths (Confounding Variable: Summer Usage/Temperature).
    *   *Reverse Causality*: "Police presence correlates with crime." (Do police cause crime? Or does crime attract police?).

## 4. Measuring Association: Mixed Combinations
1.  **Numerical + Numerical**: Pearson/Spearman Correlation.
2.  **Ordinal + Ordinal**: Spearman/Kendall Rank Correlation.
3.  **Nominal + Nominal**: Chi-Square / Cramér's V / Phi Coefficient.
4.  **Numerical + Nominal (2 Groups)**: Point-Biserial Correlation / T-Test / Cohen's d.
5.  **Numerical + Nominal (>2 Groups)**: ANOVA ($F$-statistic) / Eta Squared ($\eta^2$).
