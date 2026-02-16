
import numpy as np
import pandas as pd
import scipy.stats as stats

def nominal_data(categories):
    """
    Nominal Data: Categories with no order. 
    Allowed Ops: Mode, Frequency, Equality check.
    Not Allowed: Mean, Median, Addition, Subtraction.
    """
    print("\n--- Nominal Data (e.g., Blood Types) ---")
    print(f"Values: {categories}")
    print(f"Mode (Most Frequent): {stats.mode(categories).mode[0]}")
    try:
        print(f"Mean: {np.mean(categories)}")
    except TypeError:
        print("Mean: INVALID operation for Nominal Data.")

def ordinal_data(ranks):
    """
    Ordinal Data: Ordered categories.
    Allowed Ops: Median, Percentiles, Rank Correlation.
    Not Allowed: Mean (technically), Std Dev.
    """
    print("\n--- Ordinal Data (e.g., Likert Scale 1-5 where 5>1 but interval unknown) ---")
    data = np.array(ranks)
    print(f"Values: {data}")
    print(f"Median: {np.median(data)}")
    print(f"Unique Ranks: {np.unique(data)}")
    # Note: Mean is often calculated for Ordinal in practice, but statistically debatable.
    print(f"Mean (Use with caution): {np.mean(data):.2f}")

def interval_data(temps):
    """
    Interval Data: Ordered, fixed intervals, NO true zero.
    Allowed Ops: Mean, Std Dev, Addition/Subtraction.
    Not Allowed: Ratio (multiplication/division). 
    Example: 20C is not 'twice as hot' as 10C.
    """
    print("\n--- Interval Data (e.g., Temperature in Celsius) ---")
    print(f"Values: {temps}")
    print(f"Mean: {np.mean(temps):.2f}")
    print(f"Std Dev: {np.std(temps):.2f}")
    # Demonstration of Ratio problem
    t1, t2 = 10, 20
    print(f"Ratio Test: {t2}/{t1} = {t2/t1}. But is 20C twice as hot as 10C? No.")

def ratio_data(salary):
    """
    Ratio Data: Ordered, fixed intervals, True Zero exists.
    Allowed Ops: All (Geometric Mean, Harmonic Mean, Ratios).
    Example: $200 is twice as much as $100.
    """
    print("\n--- Ratio Data (e.g., Salary, Height, Weight) ---")
    print(f"Values: {salary}")
    print(f"Geometric Mean: {stats.gmean(salary):.2f}")
    print(f"Harmonic Mean: {stats.hmean(salary):.2f}")
    print(f"Ratio: {salary[1]} is {salary[1]/salary[0]:.2f}x of {salary[0]}")

if __name__ == "__main__":
    nominal_data(['A', 'B', 'A', 'O', 'AB', 'O', 'A'])
    ordinal_data([1, 2, 5, 4, 3, 5, 1, 2])
    interval_data([10, 20, 15, 30, 0, -5]) # 0 is just a point, not "empty"
    ratio_data([50000, 100000, 75000, 120000])
