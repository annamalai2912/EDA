# Unit 2: Intro to EDA - The Fun Exam Guide 🎓

## Table of Contents
1.  **What is EDA?** (The Detective)
    *   Classical vs Bayesian vs EDA (The Judge, The Gambler, The Detective)
    *   Goals of EDA
2.  **Basic Assumptions** (The 4 Rules of the Game)
    *   Randomness (The Shuffle)
    *   Fixed Location (The Dartboard)
    *   Fixed Variation (The Noise)
    *   Fixed Distribution (The Bell)
3.  **The 4-Plot Technique** (The Cheat Sheet)
    *   Run Sequence Plot (The Timeline)
    *   Lag Plot (The Mirror)
    *   Histogram (The Shape)
    *   Normal Probability Plot (The Line)
4.  **Graphical Representation** (The Pictures)

---

## 1. What is EDA? (Exploratory Data Analysis)

### 📝 Exam Definition
**EDA** is an approach to analyzing datasets to summarize their main characteristics, often with visual methods. It is the process of playing with data to find patterns before applying formal models.

### 🤪 The Funny Explanation
**"The First Date"**.
Before you marry someone (Modeling), you go on a date (EDA).
*   You ask questions.
*   You look for red flags (Outliers).
*   You see if they are crazy (Distribution).
*   If you skip this step, you will have a bad marriage (Bad Model).

---

## 2. Ideally, How Should We Analyze Data?

### A. Classical Analysis (The Judge)
*   **Philosophy**: "I am the law! I assume the data is Normal!"
*   **Sequence**: Problem -> Data -> **Model** -> Analysis -> Conclusions.
*   **Flaw**: If your assumption is wrong, your whole case falls apart. (Like assuming the suspect is guilty before even looking at evidence).

### B. EDA (The Detective - Sherlock Holmes)
*   **Philosophy**: "Data, data, data! I cannot make bricks without clay!"
*   **Sequence**: Problem -> Data -> **Analysis** -> Model -> Conclusions.
*   **Strength**: Highly flexible. Finds hidden clues.

### C. Bayesian Analysis (The Gambler)
*   **Philosophy**: "I bet there is a 70% chance it will rain."
*   **Sequence**: Prior Belief + New Data -> Updated Belief.
*   **Strength**: Handles uncertainty well.

---

## 3. Basic Assumptions of EDA (The 4 Pillars)

For any statistical test (t-test, ANOVA) to work, the data must follow 4 rules. EDA checks if these rules are broken.

### Rule 1: Randomness (Independence)
### 📝 Exam Definition
The data must be a random sample from the population. Observations are independent ($Y_i$ does not depend on $Y_{i-1}$).

### 🤪 The Funny Explanation
**"The Shuffled Playlist"**.
*   If your playlist is truly random, you can't guess the next song.
*   If the next song is *always* by the same artist as the last one, it's **Autocorrelated** (Not Random).
*   **Why it matters**: If data isn't random, your sample size "n" is fake news. It looks like you have 100 songs, but really you just have 1 album 10 times.

### Rule 2: Fixed Location (Mean)
### 📝 Exam Definition
The underlying distribution has a constant mean ($\mu$) over time.

### 🤪 The Funny Explanation
**"The Moving Dartboard"**.
*   Imagine throwing darts. Ideally, the bullseye stays in the center.
*   If someone secretly moves the board up while you throw, your average aim will be wrong. This is called **Drift**.
*   **Why it matters**: You can't calculate an "Average Score" if the game keeps changing levels.

### Rule 3: Fixed Variation (Standard Deviation)
### 📝 Exam Definition
The underlying distribution has a constant variance ($\sigma^2$).

### 🤪 The Funny Explanation
**"The Drunk Archer"**.
*   At the start, you are sober. Your arrows hit close together (Low Variance).
*   After 5 drinks, your arrows go wild (High Variance).
*   This is called **Heteroscedasticity**.
*   **Why it matters**: Points with high variance are noisy and should be trusted less.

### Rule 4: Fixed Distribution (Normality)
### 📝 Exam Definition
The dataset follows a single specific probability distribution (usually Normal).

### 🤪 The Funny Explanation
**"The Bell Curve"**.
*   Most things in nature (Height, IQ) follow a bell shape.
*   If your data looks like a Camel (Two humps/Bimodal), you can't just use one Mean. You have two different groups mixed together!

---

## 4. The 4-Plot Technique (The Ultimate Test)

This is a single image with 4 graphs to check all 4 assumptions at once. **Memorize this for exams!**

### 1. Run Sequence Plot ($Y$ vs Time)
*   **Checks**: Fixed Location & Variation.
*   **Look for**:
    *   Drift (Line going up/down).
    *   Fanning out (Funnel shape).
*   **Ideal**: A boring, flat band of noise.

### 2. Lag Plot ($Y_t$ vs $Y_{t-1}$)
*   **Checks**: Randomness.
*   **Look for**: lines, loops, or snakes.
*   **Ideal**: A shapeless blob (Pizza dough).

### 3. Histogram
*   **Checks**: Distribution.
*   **Look for**: Bell shape.
*   **Ideal**: Symmetric Bell Curve.

### 4. Normal Probability Plot (QQ Plot)
*   **Checks**: Normality (Specifically).
*   **Look for**: Straight diagonal line.
*   **Ideal**: All dots hugging the red line.

---

## 5. Graphical Representation

### Unidimensional (1 Variable)
*   **Histogram**: shows the shape.
*   **Box Plot**: Shows the median and outliers.
    *   *Funny*: Like a cat in a box. The "whiskers" show the range. Anything outside is a flea (Outlier).

### Bidimensional (2 Variables)
*   **Scatter Plot**: Relationships (X vs Y).
*   **Lag Plot**: Relationship with itself (Time Series).

### Multidimensional (3+ Variables)
*   **Star Plot**: Spider web shape. Good for comparing stats (Attack, Defense, Speed) in games like FIFA/Pokemon.
*   **Chernoff Faces**: Turns data into a human face. Smile = High Happiness variable. Weird but works!

---

## 📝 Important Exam Questions (Unit 2)

1.  **Define EDA and compare it with Classical Analysis.**
    *   Detective vs Judge. Model-free vs Model-based.
2.  **Explain the 4 Underlying Assumptions of EDA.**
    *   Randomness, Fixed Location, Fixed Variation, Fixed Distribution.
3.  **What is a 4-Plot? Explain its components.**
    *   Draw the 4 squares. Label them. Explain what each checks.
4.  **Why are graphical techniques important in EDA?**
    *   Anscombe's Quartet example (Same stats, different graphs). Humans see patterns computers miss.
