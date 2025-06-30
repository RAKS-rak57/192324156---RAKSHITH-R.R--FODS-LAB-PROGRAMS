import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Simulated blood pressure reduction data (50 samples each)
np.random.seed(42)
drug_group = np.random.normal(loc=12, scale=4, size=50)       # Drug group: mean=12 mmHg reduction
placebo_group = np.random.normal(loc=5, scale=3, size=50)     # Placebo group: mean=5 mmHg reduction

# Function to compute 95% confidence interval
def confidence_interval(data, confidence=0.95):
    mean = np.mean(data)
    sem = stats.sem(data)  # Standard error
    margin = sem * stats.t.ppf((1 + confidence) / 2.0, len(data)-1)
    return mean, mean - margin, mean + margin

# Calculate intervals
drug_mean, drug_ci_lower, drug_ci_upper = confidence_interval(drug_group)
placebo_mean, placebo_ci_lower, placebo_ci_upper = confidence_interval(placebo_group)

# Print results
print("95% Confidence Interval Results:")
print(f"Drug Group:      Mean = {drug_mean:.2f} mmHg | 95% CI = [{drug_ci_lower:.2f}, {drug_ci_upper:.2f}]")
print(f"Placebo Group:   Mean = {placebo_mean:.2f} mmHg | 95% CI = [{placebo_ci_lower:.2f}, {placebo_ci_upper:.2f}]")

# Plot with error bars
labels = ['Drug', 'Placebo']
means = [drug_mean, placebo_mean]
errors = [drug_mean - drug_ci_lower, placebo_mean - placebo_ci_lower]

plt.figure(figsize=(8, 5))
bars = plt.bar(labels, means, yerr=errors, capsize=10, color=['mediumseagreen', 'lightcoral'])
plt.ylabel("Mean Blood Pressure Reduction (mmHg)")
plt.title("95% Confidence Intervals: Drug vs. Placebo")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.bar_label(bars, fmt='%.1f')
plt.tight_layout()
plt.show()
