
data = {
    'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
    'Trucking (Thousands of Tons)': [250, 150, 300, 500, 75, 100],
    'Rail (Thousands of Tons)': [200, 100, 250, 400, 50, 75],
    'Air (Thousands of Tons)': [150, 50, 200, 300, 25, 50],
    'Water (Thousands of Tons)': [100, 25, 150, 200, 10, 25],
    'Pipeline (Thousands of Tons)': [50, 10, 100, 100, 5, 10]
}

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dataframe from data
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot heatmap
heatmap = ax.imshow(df.iloc[:, 1:].values, cmap='Blues')

# Set x and y ticks and labels
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Region'])))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Region'])

# Loop over data dimensions and create text annotations
for i in range(len(df['Region'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j+1], ha='center', va='center', color='w')

# Add colorbar
plt.colorbar(heatmap)

# Add title
plt.title('Freight Volume by Mode and Region')

# Adjust layout and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_85.png', bbox_inches='tight')

# Clear current image state
plt.clf()