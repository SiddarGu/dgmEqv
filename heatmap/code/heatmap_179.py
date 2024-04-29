
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import data
data = {'Subject': ['English', 'Math', 'Science', 'History', 'Art'],
        'Reading (points)': [550, 600, 700, 500, 650],
        'Writing (points)': [600, 700, 750, 550, 700],
        'Math (points)': [650, 750, 800, 600, 750],
        'Science (points)': [700, 800, 850, 650, 800],
        'History (points)': [500, 550, 600, 700, 550]}

# create dataframe
df = pd.DataFrame(data)

# set subject as index
df = df.set_index('Subject')

# create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# plot heatmap
sns.heatmap(df, cmap='YlGnBu', annot=True, linewidths=0.5, ax=ax)

# set x and y ticks and ticklabels
ax.set_xticks(np.arange(0.5, len(df.columns) + 0.5))
ax.set_yticks(np.arange(0.5, len(df.index) + 0.5))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)

# set ticks and ticklabels to be in the center
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)

# set title
ax.set_title('Academic Performance by Subject')

# resize and save figure
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_36.png', bbox_inches='tight')

# clear current image state
plt.clf()