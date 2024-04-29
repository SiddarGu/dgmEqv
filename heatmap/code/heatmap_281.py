
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process the data
data = {
    'Category': ['Fertilizer Usage', 'Irrigation Methods', 'Pesticide Usage', 'Seed Quality', 'Farming Techniques'],
    'Corn (Tonnes per Hectare)': [2.5, 3.0, 2.2, 3.5, 3.8],
    'Wheat (Tonnes per Hectare)': [3.0, 3.5, 2.8, 4.0, 4.2],
    'Rice (Tonnes per Hectare)': [2.8, 3.2, 2.5, 3.8, 4.0],
    'Soybeans (Tonnes per Hectare)': [2.2, 2.5, 2.0, 3.2, 3.5],
    'Barley (Tonnes per Hectare)': [2.0, 2.8, 2.2, 3.5, 3.8],
    'Potatoes (Tonnes per Hectare)': [2.5, 3.2, 2.8, 4.2, 4.5]
}

df = pd.DataFrame(data)
df = df.set_index('Category')

# Set figure size
plt.figure(figsize=(12, 8))

# Plot heatmap using sns.heatmap()
ax = sns.heatmap(df, annot=True, cmap='Blues', cbar=False)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')

ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_yticklabels(df.index, rotation=0, wrap=True)

# Set ticks and ticklabels in the center of rows and columns
ax.tick_params(axis='both', which='both', length=0)
ax.tick_params(axis='x', pad=10)
ax.tick_params(axis='y', pad=10)

# Set title of the figure
plt.title('Factors Affecting Crop Yields')

# Automatically resize the image
plt.tight_layout()

# Save figure in png format
plt.savefig('output/final/heatmap/png/20231228-163105_17.png', bbox_inches='tight')

# Clear current image state
plt.clf()