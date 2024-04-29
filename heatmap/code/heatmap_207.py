



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# define data
data = {'Technology': {'Nuclear Energy': 25, 'Biomedical Engineering': 10, 'Computer Science': 35, 'Environmental Science': 10, 'Materials Science': 25},
        'Research': {'Nuclear Energy': 15, 'Biomedical Engineering': 30, 'Computer Science': 25, 'Environmental Science': 5, 'Materials Science': 20},
        'Development': {'Nuclear Energy': 10, 'Biomedical Engineering': 25, 'Computer Science': 20, 'Environmental Science': 5, 'Materials Science': 25},
        'Innovation': {'Nuclear Energy': 5, 'Biomedical Engineering': 15, 'Computer Science': 5, 'Environmental Science': 30, 'Materials Science': 10},
        'Experiment': {'Nuclear Energy': 40, 'Biomedical Engineering': 10, 'Computer Science': 10, 'Environmental Science': 40, 'Materials Science': 15},
        'Testing': {'Nuclear Energy': 5, 'Biomedical Engineering': 10, 'Computer Science': 5, 'Environmental Science': 10, 'Materials Science': 5}}

# convert data into a dataframe
df = pd.DataFrame(data)

# create a figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# plot the heatmap
heatmap = sns.heatmap(df, annot=True, fmt="g", cmap='Blues', cbar=False, ax=ax)

# set x and y ticks and ticklabels to be in the center of each cell
ax.set_xticks(np.arange(len(df.columns))+0.5)
ax.set_yticks(np.arange(len(df))+0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# add a title
ax.set_title('Scientific Fields and their Processes')

# automatically resize the figure
plt.tight_layout()

# save the figure
plt.savefig('output/final/heatmap/png/20231228-134212_82.png', bbox_inches='tight')

# clear the current image state
plt.clf()