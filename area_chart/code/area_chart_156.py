

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Category':['Residential', 'Commercial', 'Industrial', 'Transportation'], 'Electricity (kWh)':[10000, 15000, 8000, 12000], 'Natural Gas (mmBTU)':[15000, 10000, 12000, 8000], 'Water (gal)':[12000, 8000, 10000, 15000], 'Petroleum (bbls)':[8000, 12000, 15000, 10000]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Set random background grid lines
ax.grid(color='lightgrey', linestyle='--', linewidth=0.5)

# Plot area chart
ax.stackplot(df['Category'], df['Electricity (kWh)'], df['Natural Gas (mmBTU)'], df['Water (gal)'], df['Petroleum (bbls)'], labels=['Electricity (kWh)', 'Natural Gas (mmBTU)', 'Water (gal)', 'Petroleum (bbls)'], colors=['#ff7f0e', '#2ca02c', '#1f77b4', '#d62728'], alpha=0.75)

# Set x and y axis ticks and ticklabels
if np.random.random() < 0.7:
    ax.set_xticks(np.arange(len(df['Category'])))
    ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_xlim(0, len(df.index) - 1)

    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value <= 10:
        ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    elif max_total_value <= 100:
        ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    elif max_total_value <= 1000:
        ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    else:
        ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend position and labels
ax.legend(loc='upper left')
ax.set_ylabel('Energy Consumption (Units)')

# Set title
ax.set_title('Energy Consumption by Sector')

# Automatically resize image and save
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-140159_75.png', bbox_inches='tight')

# Clear current image state
plt.clf()