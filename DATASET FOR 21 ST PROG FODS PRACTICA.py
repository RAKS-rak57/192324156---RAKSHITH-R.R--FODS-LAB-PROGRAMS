import pandas as pd
import numpy as np

# Simulated concentration data (100 measurements)
np.random.seed(42)
concentrations = np.random.normal(loc=15.5, scale=2.3, size=100)

df = pd.DataFrame({'Concentration': concentrations})
df.to_csv('rare_elements.csv', index=False)
print("Sample dataset 'rare_elements.csv' created.")
