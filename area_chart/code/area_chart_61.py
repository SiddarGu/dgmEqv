

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data
data = {'Year': ['2016', '2017', '2018', '2019', '2020'],
        'Corn Production (tons)': [50000, 55000, 60000, 65000, 70000],
        'Wheat Production (tons)': [60000, 65000, 70000, 75000, 80000],
        'Rice Production (tons)': [30000, 35000, 40000, 45000, 50000],
        'Soybean Production (tons)': [45000, 50000, 55000, 60000, 65000],
        'Potato Production (tons)': [20000, 22000, 25000, 28000, 30000]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Plot area chart
ax = fig.add_subplot()
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], 
             labels=['Corn', 'Wheat', 'Rice', 'Soybean', 'Potato'], colors=['#f49ac1', '#aad3e9', '#f7dc6f', '#8fd2c8', '#f5b5fc'], alpha=0.7)

# Set background grid lines
plt.grid(alpha=0.2)

# Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_xlim(0, len(df.index) - 1)

    # Calculate max total value
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    # Ceil max total value up to the nearest multiple of 10, 100 or 1000
    max_total_value = np.ceil(max_total_value / 10) * 10

    # Set y axis ticks and ticklabels
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels([str(int(x)) for x in ax.get_yticks()], wrap=True)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), framealpha=1)

# Set title
plt.title('Crop Production Trends in Agriculture Industry')

# Automatically resize image
plt.tight_layout()

# Save image
fig.savefig('output/final/area_chart/png/20231228-131755_42.png', bbox_inches='tight')

# Clear current image state
plt.clf()