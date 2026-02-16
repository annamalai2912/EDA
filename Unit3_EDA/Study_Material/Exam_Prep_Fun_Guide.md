# Unit 3: Data Analysis Tools - The Fun Exam Guide 🎓

## Table of Contents
1.  **The Process of EDA** (The Recipe)
2.  **Data Quality Issues** (The Dirty Kitchen)
    *   Consistency vs Pollution
    *   Duplicates vs Redundancy
3.  **Missing Values** (The Missing Ingredients)
    *   MCAR, MAR, MNAR (The Ghosting Game)
    *   Handling Techniques (Replacing Ingredients)
4.  **Outliers and Leverage** (The Billionaire in a Bar)
    *   Influential Points (Cook's Distance)
    *   Detection (IQR, Z-Score)
5.  **Autocorrelation** (The Echo)

---

## 1. Introduction to Data Exploration Process

### 📝 Exam Definition
A systematic approach to uncovering structure, patterns, and anomalies in data. The sequence is: Discover -> Characterize -> Prepare -> Model.

### 🤪 The Funny Explanation
**"Cleaning Your Room Before Guests Arrive"**.
*   **Discover**: Where is the mess? (Under the bed, in the closet).
*   **Characterize**: Is it dirty laundry or just books? (Quantity vs Quality).
*   **Prepare**: Throw clothes in the hamper, put books on the shelf.
*   **Model**: Now your room looks clean and you can invite people over. (Making predictions).

---

## 2. Issues Related with Data Access & Quality

### A. Data Consistency vs Pollution
### 📝 Exam Definition
*   **Consistency**: Data follows logical rules (e.g., Age > 0).
*   **Pollution**: Presence of erroneous or irrelevant data (System errors).

### 🤪 The Funny Explanation
**"The Fake vs The Gross"**.
*   **Consistency Error**: Buying a shoe size -5. That's impossible. Physics says no.
*   **Pollution**: Finding a banana peel in your shoe box. It's theoretically possible, but definitely wrong and gross.

### B. Duplicate vs Redundant Variables
### 📝 Exam Definition
*   **Duplicate**: Identical rows (Same person counted twice).
*   **Redundant**: Two variables carrying the same information (High Correlation).

### 🤪 The Funny Explanation
**"The Clone vs The Translator"**.
*   **Duplicate**: Two clones of you show up to class. The teacher marks you present twice. (Bad).
*   **Redundant**: You say "I am hot" in English, and your friend says "Mujhe garmi lag rahi hai" in Hindi. You both said the exact same thing. We only need to listen to *one* of you. (Multicollinearity).

---

## 3. Handling Missing Values (IMPORTANT!)

Why is data missing? This is huge for exams.

### A. Missing Mechanisms (Why?)
1.  **MCAR (Missing Completely at Random)**:
    *   **Funny**: A dog ate your homework. It could have happened to anyone.
    *   **Exam**: Probability of missingness is unrelated to data. Safe to ignore.
2.  **MAR (Missing at Random)**:
    *   **Funny**: The shy kid didn't answer the question. It's related to *who* they are (shy), but not *what* the answer was.
    *   **Exam**: Missingness depends on observed data (e.g., Personality Type). Can impute.
3.  **MNAR (Missing Not at Random)**:
    *   **Funny**: Someone asks "How much do you weigh?" and you stay silent. You are silent *because* the number is high.
    *   **Exam**: Missingness depends on the unobserved value itself. Dangerous bias!

### B. Imputation Techniques (How to fix?)
1.  **Mean/Median**: Fill with the average.
    *   *Funny*: Everyone gets a 'C' grade because the teacher lost the papers.
2.  **KNN (K-Nearest Neighbors)**: Look at similar people.
    *   *Funny*: "You dress like Ram, talk like Ram... I bet you scored like Ram."
3.  **New Category**: Label it "Unknown".
    *   *Funny*: "I don't know who this is, so I'll call him Bob." at least you admit it!

---

## 4. Outliers and Leverage Data

### 📝 Exam Definition
*   **Outlier**: An observation with an extreme Y-value (Response) given its X-value.
*   **Leverage Point**: An observation with an extreme X-value (Predictor).

### 🤪 The Funny Explanation
**"The Billionaire in a Bar"**.
*   Imagine 10 regular guys in a bar. Average income: ₹50k/month.
*   **Bill Gates walks in (Leverage)**:
    *   His income is ₹5 Billion/month.
    *   Suddenly, the "Average Income" of the bar becomes ₹500 Million.
    *   Does everyone feel rich? No! The average is a lie because of **one outlier**.
    *   Bill Gates has **High Leverage** because he pulls the average toward him.

### Cook's Distance
### 📝 Exam Definition
A measure of how much the regression mode changes if you delete a specific point.
*   **Funny**: "If Bill Gates leaves the bar, does the average drop back to normal?" Yes. So his Cook's Distance is HUGE. (High Influence).

---

## 5. Autocorrelation Analysis

### 📝 Exam Definition
Correlation of a time series with its own past values ($Y_t$ vs $Y_{t-k}$).

### 🤪 The Funny Explanation
**"The Echo"**.
*   You shout "Hello!".
*   1 second later: "Hello... lo... lo".
*   The sound at Time $t$ depends on the sound at Time $t-1$.
*   **Random Data**: No Echo. You shout, silence follows.
*   **Sinusoidal Correlation**: You shout, "Hello", wait 5 seconds, shout again. A repeating wave. (Seasonality).

---

## 📝 Important Exam Questions (Unit 3)

1.  **What is the difference between an Outlier and a Leverage Point?**
    *   Weird Y vs Weird X. Give the Billionaire example.
2.  **Explain MCAR, MAR, and MNAR with examples.**
    *   Dog ate homework, Shy kid, Hiding weight.
3.  **What is Data Pollution? How is it different from Inconsistency?**
    *   Garbage data vs Impossible data.
4.  **How do you interpret an Autocorrelation Plot for Random Data?**
    *   Ideally, all bars are near zero. No pattern.
