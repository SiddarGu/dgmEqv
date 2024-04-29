
# import libs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# data processing
data = {'Category': ['Visual Arts', 'Music', 'Dance', 'Theater', 'Film', 'Literature'],
        'Paintings': [30, 20, 10, 15, 5, 20],
        'Sculpture': [25, 15, 10, 20, 5, 25],
        'Photography': [20, 25, 15, 10, 10, 20],
        'Music Production': [15, 30, 20, 5, 5, 25],
        'Dance Performances': [10, 20, 30, 5, 5, 30],
        'Theater Productions': [5, 10, 10, 30, 20, 25],
        'Film Festivals': [5, 10, 15, 20, 30, 20],
        'Book Publishing': [10, 15, 20, 5, 10, 40]}

df = pd.DataFrame(data).set_index('Category')

# set up figure
fig, ax = plt.subplots(figsize=(10, 6))

# plot heatmap
sns.heatmap(df, annot=True, fmt='g', cmap='Blues', linewidths=1, linecolor='white', ax=ax)

# set x-axis ticks and labels
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_xticks(np.arange(0.5, len(df.columns), 1))

# set y-axis ticks and labels
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(0.5, len(df.index), 1))

# set ticks and labels in the center of cells
ax.tick_params(axis='both', which='both', length=0)
ax.set_yticks(np.arange(len(df.index)) + 0.5, minor=False)
ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=False)

# add colorbar
cb = ax.collections[0].colorbar
cb.set_ticks(np.arange(0, 41, 10))
cb.set_ticklabels(np.arange(0, 41, 10))

# set title
ax.set_title('Art and Culture by Category')

# resize and save image
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_15.png', bbox_inches='tight')

# clear figure
plt.clf()