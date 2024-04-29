
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Create dictionary with data
data = {'Category': ['Aging', 'Education', 'Gender Studies', 'History', 'Linguistics', 'Psychology', 'Sociology'], 
        'Research Institutions': [25, 50, 20, 40, 35, 55, 45],
        'Funding Sources': [15, 30, 10, 25, 20, 35, 25],
        'Publications': [45, 60, 30, 50, 55, 65, 50],
        'Conferences': [72, 90, 40, 65, 80, 100, 75],
        'Collaborations': [38, 45, 25, 35, 40, 50, 40]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Set figure size
fig = plt.figure(figsize=(10,8))

# Set color map
cmap = 'magma'

# Plot heatmap
ax = sns.heatmap(df.iloc[:,1:], cmap=cmap, annot=True, fmt='g', cbar=False)

# Set ticks and ticklabels
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Category'], rotation=0)

# Set tick positions
ax.set_xticks(np.arange(0.5, 5.5, 1))
ax.set_yticks(np.arange(0.5, 7.5, 1))

# Set tick labels in center
ax.tick_params(axis='x', pad=0.5)
ax.tick_params(axis='y', pad=0.5)

# Set title
plt.title('Research in Social Sciences and Humanities')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-124154_59.png', bbox_inches='tight')

# Clear current image state
plt.clf()