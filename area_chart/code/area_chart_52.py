
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Electricity Usage (kWh)': [50000, 55000, 60000, 65000, 70000],
        'Natural Gas Usage (MMBTu)': [20000, 22000, 24000, 26000, 28000],
        'Water Usage (gallons)': [100000, 110000, 120000, 130000, 140000],
        'Fuel Usage (gallons)': [50000, 55000, 60000, 65000, 70000],
        'Renewable Energy Usage (kWh)': [10000, 12000, 15000, 18000, 20000]
       }

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and ticklabels
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000 # Round up to nearest multiple of 1000
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='lightgray', linestyle='dashed', linewidth=0.5)

# Plot data with area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.iloc[:, 1:].columns)

# Set legend and title
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_title('Energy and Utilities Usage Trends')

# Automatically resize image and save as .png
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_28.png', bbox_inches='tight')

# Clear current image state
plt.clf()