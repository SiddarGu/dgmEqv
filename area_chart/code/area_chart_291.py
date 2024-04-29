

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Represent the data using a dictionary
data = {'Year': ['2019', '2020', '2021', '2022', '2023'],
        'Medical Expenses ($)': [5000, 5200, 5500, 4800, 5100],
        'Prescription Costs ($)': [2000, 2200, 2400, 2100, 2300],
        'Hospital Visits': [400, 380, 350, 390, 370]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set up figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data with an area chart
ax.stackplot(df['Year'], df['Medical Expenses ($)'], df['Prescription Costs ($)'], df['Hospital Visits'],
             labels=['Medical Expenses', 'Prescription Costs', 'Hospital Visits'], alpha=0.7)

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 100:
    ax.set_ylim(0, 100)
    ax.set_yticks(np.linspace(0, 100, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
elif max_total_value > 100 and max_total_value <= 1000:
    ax.set_ylim(0, np.ceil(max_total_value / 100) * 100)
    ax.set_yticks(np.linspace(0, np.ceil(max_total_value / 100) * 100, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
elif max_total_value > 1000 and max_total_value <= 10000:
    ax.set_ylim(0, np.ceil(max_total_value / 1000) * 1000)
    ax.set_yticks(np.linspace(0, np.ceil(max_total_value / 1000) * 1000, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
else:
    ax.set_ylim(0, np.ceil(max_total_value / 10000) * 10000)
    ax.set_yticks(np.linspace(0, np.ceil(max_total_value / 10000) * 10000, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y tick labels
ax.set_xticklabels(df['Year'], wrap=True, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticks(), wrap=True, rotation=0, ha='right', rotation_mode='anchor')

# Set background grid lines
ax.grid(True, linestyle='--', alpha=0.3)

# Set legend and resize it
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-155112_6.png', bbox_inches='tight')

# Clear the current image state
plt.clf()

# Print a title
print('Healthcare Expenses and Utilization Analysis')