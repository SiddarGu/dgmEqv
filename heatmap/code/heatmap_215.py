

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {'Website':[50,30,25,30,20],
        'Facebook':[40,25,30,40,25],
        'Twitter':[30,20,35,50,30],
        'Instagram':[20,15,40,60,35],
        'Youtube':[10,10,45,70,40],
        'LinkedIn/Pages':[10,10,45,70,40]}

df = pd.DataFrame(data, index=['Ads','Engagement','Content','Influencers','Reach'])

fig, ax = plt.subplots(figsize=(10,8))

# Using seaborn heatmap
sns.heatmap(df, cmap='Blues', annot=True, cbar=False, linewidths=.5, ax=ax)

# Set tick positions and labels for x and y axis
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set ticks in the center of rows and columns
ax.tick_params(axis='x', which='both', length=0, pad=10)
ax.tick_params(axis='y', which='both', length=0, pad=10)

# Set title
plt.title('Social Media and Web Metrics')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-134212_92.png', bbox_inches='tight')

# Clear current image state
plt.clf()