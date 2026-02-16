# Unit 5: Simulations & Case Studies - Comprehensive Textbook

## Table of Contents
1.  **Simulations in Exploratory Data Analysis**
    *   The Role of Simulation: "What If?"
    *   Monte Carlo Methods
    *   Random Number Generation (PRNG)
2.  **Case Study 1: The Random Walk**
    *   Definition and Mechanics
    *   One-Dimensional Random Walk
    *   Two-Dimensional Random Walk
    *   Applications (Stock Prices, Brownian Motion)
    *   Properties (Mean Displacement, Variance)
3.  **Case Study 2: The Standard Resistor**
    *   Quality Control in Manufacturing
    *   Nominal Value & Tolerance
    *   Process Capability Index ($C_p, C_{pk}$)
    *   Simulating Defects and Yield
4.  **Case Study 3: The Heat Flow Meter**
    *   Calibration Curves
    *   Linear Regression Models ($Y = mX + c$)
    *   Residual Analysis (Checking Linearity)
    *   Sensor Drift and Hysteresis
5.  **Introduction to Bivariate Distributions**
    *   Joint Probability Distributions
    *   Marginal and Conditional Distributions
    *   Covariance and Correlation
6.  **Association Between Two Nominal Variables**
    *   Contingency Tables (Crosstabs)
    *   Observed vs. Expected Frequencies
    *   Chi-Square Test of Independence ($\chi^2$)
    *   Measures of Association: Phi Coefficient ($\phi$), Cramér's V
7.  **Association Between Two Ordinal Variables**
    *   Rank Correlation
    *   Spearman's Rank Correlation Coefficient ($\rho$)
    *   Kendall's Tau Coefficient ($\tau$)
    *   Concordant vs. Discordant Pairs
8.  **Association Between Two Numerical Variables**
    *   Scatter Plot Analysis
    *   Pearson Correlation Coefficient ($r$)
    *   Causal Interpretations (Correlation $\neq$ Causation)
    *   Spurious Correlations
9.  **Association Between Mixed Variables**
    *   Numerical + Categorical (2 Groups): Point-Biserial Correlation
    *   Numerical + Categorical (>2 Groups): ANOVA / Eta Squared
    *   Ordinal + Categorical: Rank Biserial

---

## 1. Simulations in Exploratory Data Analysis (EDA)

Simulation is the imitation of the operation of a real-world process or system over time. In EDA, simulations allow us to:
1.  **Validate Assumptions**: "If the data were truly Normal, what would the histogram look like?"
2.  **Estimate Uncertainty**: Bootstrapping (Resampling) to find Confidence Intervals without formulas.
3.  **Stress Test Models**: How does the median behave if 10% of data is outliers? (Robustness check).

### Monte Carlo Methods
A class of computational algorithms that rely on repeated random sampling to obtain numerical results.
*   **Idea**: Solve deterministic problems using randomness.
*   **Example**: Estimate $\pi$ by throwing darts at a square with a circle inside. Ratio of hits $\approx \pi/4$.

---

## 2. Case Study 1: The Random Walk

A **Random Walk** is a stochastic process that describes a path consisting of a succession of random steps.

### One-Dimensional Random Walk
Imagine a particle on a number line starting at $X_0 = 0$.
*   At each time step $t$, it moves:
    *   Right (+1) with probability $p = 0.5$.
    *   Left (-1) with probability $q = 0.5$.
*   Position at time $n$: $X_n = X_{n-1} + Z_n$, where $Z_n \in \{-1, +1\}$.
*   **Expected Value**: $E[X_n] = 0$. (On average, it stays at the origin).
*   **Variance**: $\text{Var}(X_n) = n \cdot \text{Var}(Z) = n$.
*   **Root Mean Square Distance**: $\sqrt{n}$. (Diffusion scale).

### Applications
1.  **Finance**: The "Random Walk Hypothesis" states that stock market prices evolve according to a random walk and thus cannot be predicted. $P_t = P_{t-1} + \epsilon$.
2.  **Physics**: Brownian Motion. Pollen grains jiggling in water due to collisions with molecules.
3.  **Biology**: Genetic Drift. Allele frequencies changing randomly in a population.
4.  **Computer Science**: Pagerank Algorithm (Google) simulates a random surfer walking the web graph.

---

## 3. Case Study 2: The Standard Resistor

This case study focuses on **Statistical Process Control (SPC)**.
A factory manufactures $1000 \Omega$ resistors with a tolerance of $\pm 5\%$.
*   **Nominal Value**: $1000 \Omega$.
*   **Upper Spec Limit (USL)**: $1050 \Omega$.
*   **Lower Spec Limit (LSL)**: $950 \Omega$.

### EDA Questions
1.  **Is the process centered?**: Is the mean $\mu \approx 1000$? Or is there a shift (Drift)?
2.  **Is the process capable?**: Is the standard deviation $\sigma$ small enough?
    *   **$C_p$ (Process Capability)**: $\frac{USL - LSL}{6\sigma}$.
    *   If $C_p > 1.33$, the process is "Six Sigma" capable (very few defects).
3.  **Is the distribution Normal?**: Resistors are often sorted. If the middle values are removed and sold as "1% tolerance", the remaining "5% tolerance" batch will have a **bimodal** distribution (a hole in the middle).

---

## 4. Case Study 3: The Heat Flow Meter

This case involves **Calibration** and **Bivariate EDA**.
A scientist measures the Heat Flux ($q$) using a sensor that outputs Voltage ($V$).
*   **Physical Law**: $q = C \cdot V$ (Linear relationship).
*   **Goal**: Determine the calibration constant $C$ (Slope).

### EDA Steps
1.  **Scatter Plot**: Plot $q$ vs $V$. Is it linear?
2.  **Fit Line**: Use Least Squares Regression to find $\hat{q} = \hat{C} V + \text{intercept}$.
3.  **Residual Plot**: Plot Residuals ($q - \hat{q}$) vs $V$.
    *   **Ideal**: Random scatter around 0.
    *   **Pattern (U-shape)**: Indicates Non-Linearity. The sensor might be saturating at high heat.
    *   **Pattern (Fan-shape)**: Heteroscedasticity. Error increases with Voltage.
    *   **Time Plot of Residuals**: Check for Sensor Drift (aging).

---

## 5. Introduction to Bivariate Distributions

Univariate distributions describe one variable. Bivariate distributions describe the **Joint Probability** of two variables $X$ and $Y$.
*   **Discrete Joint PMF**: $P(X=x, Y=y)$. Table of probabilities.
*   **Marginal Distribution**: Summing rows/cols to get $P(X)$ or $P(Y)$ alone.
*   **Conditional Distribution**: $P(Y|X=x)$. "Given X is 5, what is the probability Y is 10?".

---

## 6. Association Between Two Nominal Variables

When both variables are Categorical (e.g., Gender vs Political Party), we cannot compute a correlation coefficient. We use **Cross-Tabulation**.

### Contingency Table (Crosstab)
A matrix where rows represent categories of variable A and columns represent variable B. Cells contain counts (frequencies).

### Chi-Square Test of Independence ($\chi^2$)
Tests the Null Hypothesis ($H_0$): "The two variables are independent."
*   **Logic**: Compare *Observed Counts* ($O_{ij}$) with *Expected Counts* ($E_{ij}$) if they were truly independent.
*   **Expected Count**: $E_{ij} = \frac{\text{Row Total}_i \times \text{Col Total}_j}{\text{Grand Total}}$.
*   **Statistic**: $\chi^2 = \sum \frac{(O - E)^2}{E}$.
*   **Decision**: If $\chi^2 > \text{Critical Value}$ (based on degrees of freedom $(R-1)(C-1)$), Reject $H_0$. Association exists.

### Phi Coefficient ($\phi$)
Chi-square tells us *if* there is an association, but not *how strong* it is. $\chi^2$ depends on sample size $n$.
*   **Phi**: $\phi = \sqrt{\frac{\chi^2}{n}}$.
*   **Range**: $[0, 1]$. (For 2x2 tables). 0 = No association. 1 = Perfect association.

---

## 7. Association Between Two Ordinal Variables (Rank Correlation)

When data is ranked (1st, 2nd, 3rd) or ordinal (Likert scales), standard Pearson correlation is invalid because the distance between "1" and "2" is unknown.

### Spearman's Rank Correlation ($\rho$)
*   **Method**: Convert raw data to Ranks ($R_X$, $R_Y$). Then calculate Pearson correlation on the ranks.
*   **Formula**: $\rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}$, where $d_i = R_{Xi} - R_{Yi}$.
*   **Use Case**: Monotonic relationships. Sensitive to non-linear but strictly increasing trends (e.g., $Y = e^X$). Pearson would fail here; Spearman works.

### Kendall's Tau Coefficient ($\tau$)
*   **Method**: Compares pairs of observations.
    *   **Concordant Pair**: $(X_i - X_j)(Y_i - Y_j) > 0$. Both go up or both go down. Agreement.
    *   **Discordant Pair**: $(X_i - X_j)(Y_i - Y_j) < 0$. Disagreement.
*   **Formula**: $\tau = \frac{C - D}{\frac{1}{2} n (n-1)}$.
*   **Interpretation**: "Probability of Concordance minus Probability of Discordance".
*   **Advantage**: Better for small sample sizes and many ties than Spearman.

---

## 8. Association Between Two Numerical Variables

### Pearson Correlation Coefficient ($r$)
Measures the strength and direction of the **Linear Relationship** between two interval/ratio variables.
*   **Formula**: $r = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{\sum (X-\bar{X})(Y-\bar{Y})}{\sqrt{\sum (X-\bar{X})^2 \sum (Y-\bar{Y})^2}}$.
*   **Range**: $-1 \le r \le +1$.
    *   $+1$: Perfect positive linear relationship.
    *   $-1$: Perfect negative linear relationship.
    *   $0$: No *linear* relationship (Could still be quadratic!).

### Scatter Plot Analysis
Always visualize before calculating $r$.
*   **Linear**: Points cluster around a line.
*   **Curvilinear**: Points cluster around a curve (Parabola, Exponential). $r$ will underestimate this.
*   **Clusters**: Two distinct blobs might create a "fake" correlation.
*   **Outliers**: One coordinate can swing the correlation line significantly.

### Causal Interpretations
**Correlation does not imply Causation.**
1.  **Spurious Correlation**: Two variables correlate because they share a common cause (Confounding Variable).
    *   *Example*: Ice cream sales correlate with Drowning deaths.
    *   *Confounder*: Heat wave (Summer) causes both.
2.  **Reverse Causality**: $Y$ causes $X$, not $X$ causes $Y$.
    *   *Example*: "Police officers correlate with crime rate." (Crime attracts police).
3.  **Coincidence**: In large datasets, some variables will correlate purely by chance (Bonferroni correction needed).

---

## 9. Association Between Mixed Variables

### Numerical + Nominal (2 Groups)
*   *Example*: Salary vs Gender (Male/Female).
*   **Point-Biserial Correlation**: Special case of Pearson.
*   **t-Test**: Test if Mean(Male) $\neq$ Mean(Female).
*   **Cohen's d**: Effect size (Standardized difference of means).

### Numerical + Nominal (>2 Groups)
*   *Example*: Salary vs Department (HR, IT, Sales).
*   **One-Way ANOVA**: Test if means of groups differ.
*   **Eta Squared ($\eta^2$)**: Proportion of variance in Salary explained by Department. (Like $R^2$).
