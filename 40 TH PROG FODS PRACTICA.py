import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create and save sample dataset
data = {
    'Name': ['Messi', 'Ronaldo', 'Mbappe', 'Neymar', 'De Bruyne', 'Modric', 'Haaland', 'Salah', 'Kane', 'Vinicius'],
    'Age': [36, 38, 25, 31, 32, 37, 23, 30, 29, 22],
    'Position': ['Forward', 'Forward', 'Forward', 'Forward', 'Midfielder', 'Midfielder', 'Forward', 'Forward', 'Forward', 'Forward'],
    'Goals': [25, 22, 30, 18, 10, 5, 35, 20, 24, 15],
    'WeeklySalary': [1000000, 950000, 800000, 850000, 700000, 600000, 900000, 750000, 720000, 680000]
}

df = pd.DataFrame(data)
df.to_csv('soccer_players.csv', index=False)
print("✅ Sample dataset 'soccer_players.csv' created.\n")

# Step 2: Load dataset
df = pd.read_csv('soccer_players.csv')

# Step 3: Top 5 goal scorers
top_goals = df.sort_values(by='Goals', ascending=False).head(5)
print("⚽ Top 5 Goal Scorers:")
print(top_goals[['Name', 'Goals']], "\n")

# Step 4: Top 5 highest salaries
top_salary = df.sort_values(by='WeeklySalary', ascending=False).head(5)
print("💰 Top 5 Highest Paid Players:")
print(top_salary[['Name', 'WeeklySalary']], "\n")

# Step 5: Average age and players above average
avg_age = df['Age'].mean()
above_avg_age = df[df['Age'] > avg_age]
print(f"📊 Average Age: {avg_age:.2f}")
print("👴 Players Above Average Age:")
print(above_avg_age[['Name', 'Age']], "\n")

# Step 6: Visualize position distribution
plt.figure(figsize=(8, 5))
df['Position'].value_counts().plot(kind='bar', color='mediumseagreen')
plt.title("Player Distribution by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
