
# Unit 5: Simulations & Case Studies

## 1. Random Walk Simulation (Case Study 1)
A **Random Walk** is a mathematical object, known as a stochastic or random process, that describes a path that consists of a succession of random steps on some mathematical space such as the integers.
*   **Simple Random Walk**: Start at 0. At each step, either move +1 or -1 with equal probability.
*   **Application**: Stock prices, Diffusion of molecules (Brownian Motion).

## 2. Standard Resistor Simulation (Case Study 2)
This case study involves analyzing the distribution of resistance values in a batch of resistors. Resistors have a tolerance (e.g., ±5%). EDA helps verify if the manufacturing process is within control limits.
*   **Objective**: Check if the distribution is Normal and centered at the nominal resistance (e.g., 1000 Ohms).

## 3. Heat Flow Meter (Case Study 3)
Calibration of a heat flow meter involves measuring heat flux vs thermocouple output.
*   **Objective**: Fit a linear model (Calibration Curve), check residuals for non-linearity, and assess drift over time. This mimics the "4-Plot" analysis used in Unit 2.

## 4. Chi-Square Test & Contingency Tables (For Nominal Data)
**Chi-Square Test of Independence** determines whether there is a significant association between two categorical variables.
*   **Contingency Table**: A frequency table for two variables (Rows x Columns).
*   **Formula**: $\chi^2 = \sum \frac{(O - E)^2}{E}$
    *   $O$: Observed Frequency.
    *   $E$: Expected Frequency (Row Total * Col Total / Grand Total).
*   **Phi Coefficient**: Measure of association for 2x2 tables ($\sqrt{\chi^2 / n}$).

## 5. Correlation Coefficients (Bivariate Stats)
*   **Pearson Correlation ($r$)**: Linear relationship between two interval/ratio variables. (-1 to +1).
*   **Spearman Rank Correlation ($\rho$)**: Monotonic relationship between two ordinal/ranked variables. Robust to outliers.
*   **Kendall’s Tau ($\tau$)**: Measure of rank correlation based on concordant and discordant pairs. Better for small samples.
