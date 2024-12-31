import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency
import sys
import os
# Load dataset
sys.path.append(os.path.abspath("../data"))
data = pd.read_csv(r"C:\Users\user\Projects\Insurance-Data-Analysis-for-Alpha_Care_Solutions\data\cleaned_insurance_data.csv")

# Metrics
metric = 'TotalClaims'

# Data Segmentation
group_a = data[data['Province'] == 'Gauteng']
group_b = data[data['Province'] != 'Gauteng']

# Statistical Testing
# Numerical: t-test
stat, p_value_ttest = ttest_ind(group_a[metric], group_b[metric])
print(f"T-test p-value for {metric}: {p_value_ttest}")

# Categorical: chi-squared
contingency_table = pd.crosstab(data['Gender'], data['Province'])
chi2_stat, p_value_chi2, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-squared p-value for Gender vs Province: {p_value_chi2}")

# Analyze and Report
if p_value_ttest < 0.05:
    print(f"Reject the null hypothesis: Significant difference in {metric} across provinces.")
else:
    print(f"Fail to reject the null hypothesis: No significant difference in {metric} across provinces.")

if p_value_chi2 < 0.05:
    print("Reject the null hypothesis: Significant association between Gender and Province.")
else:
    print("Fail to reject the null hypothesis: No significant association between Gender and Province.")
