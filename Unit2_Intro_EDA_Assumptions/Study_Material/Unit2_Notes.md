
# Unit 2: Introduction to Exploratory Data Analysis (EDA)

## 1. What is EDA?
Exploratory Data Analysis (EDA) is an approach/philosophy for data analysis that employs a variety of techniques (mostly graphical) to maximize insight into a data set, uncover underlying structure, extract important variables, detect outliers and test underlying assumptions.

## 2. EDA vs Classical Analysis vs Bayesian
*   **Classical Analysis**:
    1.  Problem => Data => **Model** => Analysis => Conclusions
    2.  Assumes a model (e.g., normal distribution) first, then fits explicitly.
*   **EDA**:
    1.  Problem => Data => **Analysis** => Model => Conclusions
    2.  Does NOT impose a model initially; lets the data suggest the model.
*   **Bayesian Analysis**:
    1.  Problem => Prior Distribution + Data => **Posterior Distribution** => Conclusions
    2.  Incorporates prior knowledge directly into the analysis.

## 3. Underlying Assumptions in EDA
Most statistical techniques assume the data has certain properties:
1.  **Randomness**: The data are a random sample from the population.
2.  **Fixed Distribution**: The data come from a specific distribution family (e.g., Normal).
3.  **Fixed Location**: The distribution has a constant mean (location parameter).
4.  **Fixed Variation**: The distribution has a constant variance (scale parameter).

## 4. The 4-Plot (Lab Exp 2)
The "4-Plot" is a specific visualization to check these assumptions. It consists of:
1.  **Run Sequence Plot**: (Y vs i) Checks for shifts in location/variation over time (Non-Stationarity).
2.  **Lag Plot**: ($Y_i$ vs $Y_{i-1}$) Checks for randomness/serial correlation. If random, it's a blob. If structure, it's not random.
3.  **Histogram**: Checks for the underlying distribution (Bell curve?).
4.  **Normal Probability Plot**: Checks if the data follows a normal distribution (Straight line?).

## 5. Consequences of Violating Assumptions
*   **Non-Randomness**: Independence assumption violated. Standard Error estimates are wrong. Hypothesis tests (t-test) become invalid.
*   **Non-Fixed Parameters**: Known as "Drift" (Location change) or "Heteroscedasticity" (Result variance changes). Models fail to predict accurately.
