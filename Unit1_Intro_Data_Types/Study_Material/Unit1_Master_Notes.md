# Unit 1: Introduction to Data & Descriptive Statistics - Master Guide

## 1. Introduction to Data
**Data** refers to facts, figures, and information collected for reference or analysis. In the context of business and science, data is the fuel for decision-making.

### 1.1 Types of Data based on Observation (Temporal Dimension)
Understanding *when* data is collected is crucial for choosing the right analysis model.

#### **A. Cross-Sectional Data**
*   **Definition**: Data collected at a **single point in time** (or a very short window) across multiple subjects (individuals, companies, countries).
*   **Real-Tme Example**: 
    *   *Real Estate*: The selling prices of all houses in New York City sold in *January 2023*.
    *   *Healthcare*: Blood pressure readings of 1,000 patients taken on *Monday morning*.
*   **Key Characteristic**: No temporal ordering. Order of rows doesn't matter.

#### **B. Time Series Data**
*   **Definition**: Data collected for a **single subject** over **multiple time intervals**. Using the past to predict the future.
*   **Real-Time Example**: 
    *   *Finance*: The daily closing price of Tesla (TSLA) stock from 2020 to 2024.
    *   *Meteorology*: Hourly temperature readings at a specific weather station for one month.
*   **Key Characteristic**: Order is critical. $t-1$ affects $t$. Autocorrelation exists.

#### **C. Panel Data (Longitudinal Data)**
*   **Definition**: A combination of Cross-Sectional and Time Series. Data collected for **multiple subjects** over **multiple time points**.
*   **Real-Time Example**: 
    *   *Economics*: The GDP, Inflation Rate, and Unemployment Rate for *20 different countries* over a *10-year period*.
    *   *Clinical Trials*: Measuring the cholesterol levels of *50 specific patients* every week for *6 months*.
*   **Key Characteristic**: Allows controlling for unobserved subject-specific factors (e.g., genetics in patients).

---

## 2. Classification based on Measurement (Scales)
Stevens' Scales of Measurement determine which statistical operations are valid.

| Scale | Properties | Allowed Statistics | Real-World Example |
| :--- | :--- | :--- | :--- |
| **Nominal** (Names) | Classification only. No order. | Mode, Frequency, Chi-Square | **Blood Type** (A, B, O), **Department** (HR, IT, Sales), **Color** (Red, Blue). |
| **Ordinal** (Order) | Classification + Order. Difference is unknown. | Median, Percentile, Rank Correlation | **Satisfaction** (1-5 Star), **Pain Scale** (Mild, Moderate, Severe), **Rank** (1st, 2nd). |
| **Interval** (Equal Intervals) | Order + Equal Distance. **No True Zero**. | Mean, Std Dev, Correlation | **Temperature (°C/°F)** (0°C is not "no heat"), **IQ Score**, **Calendar Year** (Year 0 is arbitrary). |
| **Ratio** (True Zero) | Order + Equal Distance + **True Zero**. | Geometric/Harmonic Mean, CV, Ratios | **Salary** ($0 means no money), **Height**, **Weight**, **Distance**, **Time duration**. |

*   **Real-Time Insight**: You cannot say "It is twice as hot today" if it goes from 10°C to 20°C (Interval). But you *can* say "I observed twice as many customers" if count goes from 10 to 20 (Ratio).

---

## 3. Classification based on Source & Structure

### 3.1 Availability (Source)
1.  **Primary Data**: Collected *specifically* for the problem at hand.
    *   *Methods*: Surveys, Interviews, Lab Experiments, Sensor logs.
    *   *Pros/Cons*: High accuracy/relevance, but expensive and time-consuming.
2.  **Secondary Data**: Collected by someone else for a different purpose.
    *   *Sources*: Government Census, Kaggle Datasets, Financial Reports.
    *   *Pros/Cons*: Cheap and fast, but may be outdated or biased.
3.  **Tertiary Data**: Compiled summaries of primary/secondary data.
    *   *Examples*: Encyclopedias, Indexes, Bibliography.

### 3.2 Structural Form
1.  **Structured**: Highly organized, rigid schema. (e.g., SQL Tables, Excel sheets). Easy to query.
2.  **Semi-Structured**: Tags/Keys separate elements, but no rigid schema. (e.g., JSON, XML, NoSQL DBs).
3.  **Unstructured**: No pre-defined model. (e.g., Text approach, Video feeds, Audio recordings, Images). *Requires NLP/Computer Vision.*

---

## 4. Sampling Concepts
How do we gather data without measuring everything?

*   **Population ($N$)**: The entire group of interest (e.g., "All voters in India").
*   **Sample ($n$)**: A subset of the population (e.g., "1,000 voters surveyed").
*   **Parameter ($\mu, \sigma$)**: A numerical characteristic of the *Population*. (Truth, usually unknown).
*   **Statistic ($\bar{x}, s$)**: A numerical characteristic of the *Sample*. (Estimate, calculated).

### Types of Statistics
1.  **Descriptive Statistics**: Summarizes data (Mean, Median, Graphs). "What happened?"
2.  **Inferential Statistics**: Uses sample data to make predictions about the population (Hypothesis Testing, Confidence Intervals). "What *will* happen?"

## 5. Frequency Distribution
A table that displays the number of observations within a given interval.
*   **Discrete Frequency**: Count of distinct categories (e.g., Number of cars per household).
*   **Continuous Frequency**: Count of values within ranges (bins) (e.g., Ages 0-10, 11-20).
