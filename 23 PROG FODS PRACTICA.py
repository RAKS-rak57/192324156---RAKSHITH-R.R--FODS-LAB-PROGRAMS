import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Simulated blood pressure reduction data (mmHg)
np.random.seed(42)
placebo = np.random.normal(loc=2.5, scale=1.2, size=50)     # Mild reduction
treatment = np.random.normal(loc=6.0, scale=1.5, size=50)   # Stronger reduction

# Perform two-sample t-test
t_stat, p_value = stats.ttest_ind(treatment, placebo)

# Print results
print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_value:.5f}")
if p_value < 0.05:
    print("✅ Statistically significant difference (p < 0.05)")
else:
    print("❌ No statistically significant difference (p ≥ 0.05)")

# Visualization
labels = ['Placebo', 'Treatment']
means = [np.mean(placebo), np.mean(treatment)]
errors = [np.std(placebo)/np.sqrt(len(placebo)), np.std(treatment)/np.sqrt(len(treatment))]

plt.figure(figsize=(8, 5))
bars = plt.bar(labels, means, yerr=errors, capsize=10, color=['lightcoral', 'mediumseagreen'])
plt.title("Mean Blood Pressure Reduction by Group")
plt.ylabel("Reduction (mmHg)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.bar_label(bars, fmt='%.2f')

# Annotate p-value
plt.text(0.5, max(means)+0.5, f"P-value = {p_value:.5f}", ha='center', fontsize=12, color='navy')
plt.tight_layout()
plt.show()
