import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Sample dataset
data = {
    'StudyHours': [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0],
    'ExamScore':  [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

# Calculate Pearson correlation
corr_coef, p_value = pearsonr(df['StudyHours'], df['ExamScore'])

print(f"📈 Pearson Correlation Coefficient: {corr_coef:.3f}")
print(f"📊 P-value: {p_value:.5f}")
if p_value < 0.05:
    print("✅ Significant positive correlation between study time and exam score.")
else:
    print("⚠️ No statistically significant correlation.")

# Scatter plot with regression line
plt.figure(figsize=(8, 5))
sns.regplot(x='StudyHours', y='ExamScore', data=df, color='teal', marker='o')
plt.title("Study Time vs Exam Score")
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Score")
plt.grid(True)
plt.tight_layout()
plt.show()

# Heatmap of correlation matrix
plt.figure(figsize=(5, 4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
