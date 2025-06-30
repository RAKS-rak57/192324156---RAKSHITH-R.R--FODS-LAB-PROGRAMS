import pandas as pd, matplotlib.pyplot as plt, seaborn as sns, scipy.stats as stats, tkinter as tk

# Create the dataset
df = pd.DataFrame({'age':[23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61], 
                   '%fat':[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]})

# Print basic statistics
print(f"Mean Age: {df.age.mean():.2f}, Median Age: {df.age.median()}, Std Age: {df.age.std():.2f}")
print(f"Mean %Fat: {df['%fat'].mean():.2f}, Median %Fat: {df['%fat'].median()}, Std %Fat: {df['%fat'].std():.2f}")

# Plot functions
def show_boxplots():
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    sns.boxplot(y=df.age, ax=axs[0])
    axs[0].set_title("Boxplot of Age")
    sns.boxplot(y=df['%fat'], ax=axs[1])
    axs[1].set_title("Boxplot of %Fat")
    plt.tight_layout()
    plt.show()

def show_scatter():
    plt.figure(figsize=(6, 5))
    sns.scatterplot(x=df.age, y=df['%fat'])
    plt.title("Scatterplot of Age vs %Fat")
    plt.xlabel("Age")
    plt.ylabel("%Fat")
    plt.show()

def show_qq_age():
    plt.figure(figsize=(6, 5))
    stats.probplot(df.age, dist="norm", plot=plt)
    plt.title("Q-Q Plot of Age")
    plt.show()

def show_qq_fat():
    plt.figure(figsize=(6, 5))
    stats.probplot(df['%fat'], dist="norm", plot=plt)
    plt.title("Q-Q Plot of %Fat")
    plt.show()

def show_histograms():
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    sns.histplot(df.age, kde=True, ax=axs[0], bins=6, color='skyblue')
    axs[0].set_title("Histogram of Age")
    sns.histplot(df['%fat'], kde=True, ax=axs[1], bins=6, color='salmon')
    axs[1].set_title("Histogram of %Fat")
    plt.tight_layout()
    plt.show()

# Mapping plot names to functions
plot_options = {
    "Boxplots": show_boxplots,
    "Scatterplot": show_scatter,
    "Q-Q Plot Age": show_qq_age,
    "Q-Q Plot %Fat": show_qq_fat,
    "Histograms": show_histograms
}

# GUI setup
root = tk.Tk()
root.title("Plot Viewer")
root.geometry("300x250")

tk.Label(root, text="Select a Plot to View:", font=("Arial", 12)).pack(pady=10)

listbox = tk.Listbox(root, font=("Arial", 11))
for option in plot_options:
    listbox.insert(tk.END, option)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

def on_select(event):
    selection = listbox.get(listbox.curselection())
    plot_options[selection]()  # Call the corresponding function

listbox.bind('<<ListboxSelect>>', on_select)

root.mainloop()
5
