
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process data
data = {'Category': ['Art Galleries', 'Museums', 'Theatres', 'Concert Halls', 'Cinemas', 'Exhibitions'],
        'United States': [500, 700, 400, 250, 750, 300],
        'United Kingdom': [400, 600, 350, 200, 600, 250],
        'France': [300, 500, 300, 150, 500, 200],
        'Germany': [200, 400, 250, 125, 400, 150],
        'Japan': [100, 300, 200, 100, 300, 100]}

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot heatmap using sns.heatmap()
sns.heatmap(df, cmap='BuPu', annot=True, fmt='g', linewidths=0.5, cbar_kws={'label': 'Number of Venues'})

# Set ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', fontsize=12)
ax.set_yticklabels(df.index, fontsize=12)

# Set tick positions to be in the center of each cell
ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=True)
ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=True)
ax.set_xticklabels('', minor=True)
ax.set_yticklabels('', minor=True)

# Set title
plt.title('Cultural Venues by Country', fontsize=16)

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_23.png', bbox_inches='tight')

# Clear image state
plt.clf()