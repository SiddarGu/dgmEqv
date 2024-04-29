
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import data
data = {'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'], 
        'Crop Yield (Tonnes per Hectare)': [3.2, 2.8, 3.5, 4.0, 1.8, 3.1], 
        'Crop Diversity (Number of Crops)': [5, 4, 6, 7, 3, 5], 
        'Land Usage (%)': [55, 40, 60, 65, 35, 50], 
        'Water Usage (%)': [45, 35, 50, 60, 30, 40], 
        'Fertilizer Usage (%)': [60, 50, 65, 70, 40, 55]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(8,6))

# Plot heatmap
plt.imshow(df.iloc[:,1:].values, cmap='viridis')

# Add colorbar
plt.colorbar()

# Set x and y ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_xticklabels(df.columns[1:])
ax.set_yticks(np.arange(len(df['Region'])))
ax.set_yticklabels(df['Region'])

# Set ticks and ticklabels in the center of rows and columns
plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=True, left=False, right=False, labelleft=True)
plt.gca().set_xticks(np.arange(-.5, len(df.columns[1:]), 1), minor=True)
plt.gca().set_yticks(np.arange(-.5, len(df['Region']), 1), minor=True)
plt.grid(which='minor', color='w', linestyle='-', linewidth=2)

# Rotate x ticks and set rotation_mode and ha
plt.xticks(rotation=45, rotation_mode='anchor', ha='right')

# Set title
plt.title('Agriculture Metrics by Region')

# Show value of each cell
for i in range(len(df['Region'])):
    for j in range(len(df.columns[1:])):
        plt.text(j, i, df.iloc[i,j+1], ha='center', va='center', color='w')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-134212_89.png', bbox_inches='tight')

# Clear current image state
plt.clf()