import pandas as pd
import numpy as np
import scipy.stats as stats

# Load dataset
df = pd.read_csv('rare_elements.csv')
data = df['Concentration'].dropna().values

# User inputs
sample_size = int(input("Enter sample size (e.g., 30): "))
confidence_level = float(input("Enter confidence level (e.g., 0.95 for 95%): "))
precision = float(input("Enter desired precision (e.g., 0.5): "))

# Draw random sample
np.random.seed(1)
sample = np.random.choice(data, size=sample_size, replace=False)

# Point estimate (sample mean)
mean = np.mean(sample)

# Standard error
sem = stats.sem(sample)

# Confidence interval
margin = sem * stats.t.ppf((1 + confidence_level) / 2.0, df=sample_size - 1)
ci_lower = mean - margin
ci_upper = mean + margin

# Output
print(f"\nSample Mean Concentration: {mean:.3f}")
print(f"{int(confidence_level*100)}% Confidence Interval: [{ci_lower:.3f}, {ci_upper:.3f}]")
print(f"Desired Precision: ±{precision}")
print("Precision met!" if margin <= precision else "Precision not met. Consider increasing sample size.")
