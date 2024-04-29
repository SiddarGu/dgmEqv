
# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Energy Consumption (kWh)': [50000, 52000, 55000, 58000, 62000],
        'Water Usage (m3)': [20000, 21000, 22000, 25000, 28000],
        'Waste Production (kg)': [10000, 11000, 13000, 15000, 17000],
        'CO2 Emission (ton)': [5000, 5500, 6000, 6500, 7000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data as stacked area chart
ax.stackplot(df['Year'], df.iloc[:, 1:].values.T, labels=df.columns[1:])

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/100) * 100
ax.set_ylim(0, max_total_value)

# Set y-axis tick labels
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)

# Set x-axis tick labels
xticks = np.arange(0, len(df.index))
ax.set_xticks(xticks)
ax.set_xticklabels(df['Year'])

# Set grid lines
ax.grid(axis='both', linestyle='--')

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Environmental Impact Trends from 2015 to 2019')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_71.png', bbox_inches='tight')

# Clear current image state
plt.clf()