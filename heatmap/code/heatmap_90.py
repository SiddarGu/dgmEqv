
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data as dictionary
data = {
    'Category': ['Classical', 'Modern', 'Contemporary', 'Performance'],
    'Painting': [25, 35, 20, 10],
    'Sculpture': [10, 15, 30, 10],
    'Drawing': [15, 10, 15, 10],
    'Photography': [10, 20, 15, 30],
    'Music/Theater': [40, 20, 20, 40]
}

# Convert dictionary to pandas dataframe
df = pd.DataFrame(data)

# Set the index to be the 'Category' column
df.set_index('Category', inplace=True)

# Create figure and axes objects
fig, ax = plt.subplots(figsize=(10, 8))

# Plot heatmap chart
hm = sns.heatmap(df, cmap='Blues', annot=True, linewidths=.5, ax=ax)

# Set ticks and ticklabels for x and y axis
hm.set_xticklabels(hm.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
hm.set_yticklabels(hm.get_yticklabels(), rotation=0, ha='right', rotation_mode='anchor')

# Add colorbar
cbar = hm.collections[0].colorbar
cbar.ax.set_ylabel('Percentage', rotation=-90, va='bottom')

# Set title
ax.set_title('Art Forms by Category and Time Period')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-124154_86.png', bbox_inches='tight')

# Clear current image state
plt.clf()