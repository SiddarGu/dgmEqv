
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Electricity (kWh)': [5000, 4800, 4500, 4700, 4900],
        'Water (gal)': [3000, 3100, 3200, 3300, 3400],
        'Gas (m3)': [1000, 1100, 1200, 1300, 1400],
        'Oil (L)': [500, 600, 700, 800, 900]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data as an area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].values.T, labels=df.columns[1:], alpha=0.8)

# Set x and y axis ticks and ticklabels with 70% probability
if np.random.rand() < 0.7:
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0])
    ax.set_xlim(0, len(df.index) - 1)
if np.random.rand() < 0.7:
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_ylim(0, max_total_value)

# Set suitable colors and transparency
colors = ['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728']
for i, c in enumerate(ax.collections):
    c.set_color(colors[i])
    c.set_alpha(0.8)

# Set background grid lines
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Set legend position and labels
ax.legend(loc='upper left')
ax.set_ylabel('Energy Consumption')
ax.set_xlabel('Year')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-103019_1.png', bbox_inches='tight')

# Clear the current image state
plt.clf()