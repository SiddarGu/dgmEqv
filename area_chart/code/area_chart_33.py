
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Category': ['Transportation', 'Agriculture', 'Manufacturing', 'Energy', 'Construction', 'Retail', 'Hospitality', 'Healthcare', 'Education', 'Technology', 'Consumer Goods'],
        'C02 Emissions (tons)': [500, 800, 1000, 1200, 1000, 600, 600, 800, 500, 1200, 700],
        'Water Usage (gallons)': [1000, 900, 800, 700, 800, 900, 1000, 800, 900, 700, 800],
        'Waste Generated (pounds)': [300, 500, 600, 800, 500, 300, 400, 300, 400, 500, 600]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplot
fig, ax = plt.subplots(figsize=(12, 8))

# Set background grid lines
plt.grid(color='grey', linestyle=':', linewidth=0.5)

# Set x and y axis ticks and ticklabels
if np.random.uniform() < 0.7:
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_xlim(0, len(df.index) - 1)

if np.random.uniform() < 0.7:
    # Calculate max total value and set yticks
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value > 1000:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    elif max_total_value > 100:
        max_total_value = np.ceil(max_total_value / 100) * 100
    elif max_total_value > 10:
        max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df['Category'], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=['C02 Emissions (tons)', 'Water Usage (gallons)', 'Waste Generated (pounds)'], colors=['#A6CEE3', '#1F78B4', '#B2DF8A'], alpha=0.7)

# Set legend and adjust position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title and labels
ax.set_title('Environmental Impact by Industry')
ax.set_xlabel('Category')
ax.set_ylabel('Amount')

# Automatically resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-130527_18.png', bbox_inches='tight')

# Clear current image state
plt.clf()