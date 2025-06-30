import pandas as pd

df = pd.read_csv('customer_data1.csv')
df.columns = df.columns.str.strip()

# Define spending segments
q1, q2 = df['Total Spending'].quantile([0.33, 0.67])
df['Spending Segment'] = pd.cut(df['Total Spending'], bins=[-1, q1, q2, float('inf')],
                                labels=['Low Spenders', 'Medium Spenders', 'High Spenders'])

# Average age per segment
avg_age = df.groupby('Spending Segment', observed=True)['Age'].mean()

# Gender count per segment
gender_counts = df.groupby(['Spending Segment', 'Gender'], observed=True).size().unstack(fill_value=0)

# Output
print(df[['Customer ID', 'Gender', 'Spending Segment']])
print("\nAverage Age per Spending Segment:\n", avg_age)
print("\nGender Distribution per Segment:\n", gender_counts)
print("\nData Info:\n", df.info())
print("\nMissing Values:\n", df.isnull().sum())
