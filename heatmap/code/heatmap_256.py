
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data into a dataframe
data = {'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Wheat (Tonnes per Hectare)': [3.2, 2.8, 3.5, 4.0, 1.8, 3.1],
        'Corn (Tonnes per Hectare)': [5.5, 4.8, 5.2, 6.0, 2.5, 4.0],
        'Rice (Tonnes per Hectare)': [3.0, 3.2, 2.7, 6.5, 2.2, 3.6],
        'Soybeans (Tonnes per Hectare)': [2.5, 2.7, 2.2, 3.0, 1.5, 2.8],
        'Barley (Tonnes per Hectare)': [4.0, 3.5, 3.0, 5.5, 2.0, 4.2],
        'Potatoes (Tonnes per Hectare)': [6.1, 5.0, 4.8, 7.2, 3.5, 5.0]}

df = pd.DataFrame(data)
df.set_index('Region', inplace=True)

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the heatmap
sns.heatmap(df, annot=True, cmap='Blues', fmt='.1f', linewidths=0.5, ax=ax)

# Set the ticks and tick labels
ax.set_xticks(np.arange(0.5, len(df.columns)+0.5, 1))
ax.set_yticks(np.arange(0.5, len(df.index)+0.5, 1))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df.index, rotation=0)

# Set the title
ax.set_title('Crop Yields by Region in Agriculture')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-155147_55.png', bbox_inches='tight')

# Clear the current image state
plt.clf()