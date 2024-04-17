#whether a new medication reduces blood pressure. Two groups: Group A, which received the medication, and Group B, which received a placebo.


import numpy as np
from scipy import stats

# Generate sample data for Group A (medication) and Group B (placebo)
group_a = np.random.normal(loc=100, scale=10, size=30)  # Mean blood pressure of 100 with standard deviation of 10
group_b = np.random.normal(loc=105, scale=10, size=30)  # Mean blood pressure of 105 with standard deviation of 10

# Perform independent two-sample t-test
t_statistic, p_value = stats.ttest_ind(group_a, group_b)

# Output results
print("T-value:", t_statistic)
print("P-value:", p_value)

# Interpret the results
if p_value < 0.05:
    print("The difference in blood pressure between Group A and Group B is statistically significant.")
else:
    print("There is no statistically significant difference in blood pressure between Group A and Group B.")
