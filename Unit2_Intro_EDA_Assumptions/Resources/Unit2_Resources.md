# Unit 2 Resources: EDA Philosophy & Assumptions 📚

## 📖 Recommended Textbooks
1.  **"Exploratory Data Analysis"** by John Tukey.
    *   *Why*: The **Bible** of EDA.
    *   *Focus*: The original "Detective" vs "Judge" philosophy.
    *   *Chapters*: 1 (Looking at Data), 2 (Plots).
2.  **"The Art of Statistics: Learning from Data"** by David Spiegelhalter.
    *   *Why*: Excellent for understanding *Assumptions* like randomness and bias.
    *   *Chapters*: 3 (Why we need to look at data).

## 📺 Video Tutorials (Free)
1.  **StatQuest with Josh Starmer** (YouTube)
    *   *Playlist*: "StatQuest: Exploratory Data Analysis"
    *   *Video*: "The BoxPlot" (Crucial for Outliers).
    *   *Video*: "StatQuest: Maximum Likelihood, clearly explained!!!" (Good for assumptions).
2.  **3Blue1Brown** (YouTube)
    *   *Video*: "But what is the Central Limit Theorem?"
    *   *Why*: Helps understand the "Normal Distribution" assumption.

## 📊 Datasets for Practice
1.  **Anscombe's Quartet** (Crucial)
    *   [Link](https://en.wikipedia.org/wiki/Anscombe%27s_quartet)
    *   *Practice*: Calculate same stats for 4 datasets, plot them to see the huge difference.
    *   *Code*: Just `import seaborn as sns; sns.load_dataset('anscombe')`
2.  **Daily Minimum Temperatures in Melbourne** (Time Series)
    *   [Link](https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv)
    *   *Practice*: Run Sequence Plot, Lag Plot. (Check for Seasonality).

## 📄 Key Articles & Guides
*   **"The 4-Plot" NIST Handbook**:
    *   [Link](https://www.itl.nist.gov/div898/handbook/eda/section3/eda33e.htm)
    *   *Summary*: The definitive guide on using the 4-Plot to check assumptions.
*   **"Box Plot Interpretation" Guide**:
    *   [Link](https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51)
    *   *Summary*: Learn what the "whiskers" actually mean (1.5 IQR).
