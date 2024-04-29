

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import data as pandas dataframe
data = pd.DataFrame({'City': ['New York City', 'San Francisco', 'Los Angeles', 'Chicago', 'Dallas'], 
                     'Median Home Price ($)': [1200000, 1500000, 800000, 500000, 300000], 
                     'Average Price Per Square Foot ($)': [500, 800, 600, 400, 300], 
                     'Year Over Year Change (%)': [5, 8, 6, 4, 3], 
                     'Days on Market': [60, 40, 50, 70, 80], 
                     'Inventory (Units)': [3000000, 1500000, 2000000, 1000000, 500000]})

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot heatmap chart using imshow()
im = ax.imshow(data.iloc[:, 1:].to_numpy(), cmap='BuGn')

# Set x and y ticks and ticklabels
ax.set_xticks(np.arange(len(data.columns[1:])))
ax.set_yticks(np.arange(len(data['City'])))
ax.set_xticklabels(data.columns[1:])
ax.set_yticklabels(data['City'])

# Show all ticks and labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
plt.setp(ax.get_yticklabels(), rotation=0)

# Loop over data dimensions and create text annotations
for i in range(len(data['City'])):
    for j in range(len(data.columns[1:])):
        text = ax.text(j, i, data.iloc[i, j+1], ha='center', va='center', color='black')

# Set title
ax.set_title("Housing Market Data by City")

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-134212_3.png', bbox_inches='tight')

# Clear figure
plt.clf()