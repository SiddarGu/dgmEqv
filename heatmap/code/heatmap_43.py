

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# create data
cols = ['Category', 'Sports Team', 'Musician', 'Actor', 'Movie', 'TV Show', 'Video Game']
rows = ['Football', 'Basketball', 'Baseball', 'Soccer', 'Hockey', 'Esports']
values = [[74, 2, 5, 3, 10, 6], [5, 80, 5, 3, 5, 2], [7, 5, 70, 2, 8, 8], [9, 3, 3, 75, 5, 5], [5, 2, 5, 2, 80, 6], [4, 8, 5, 5, 6, 72]]

# create dataframe
df = pd.DataFrame(values, index=rows, columns=cols[1:])

# create figure and axes
fig, ax = plt.subplots(figsize=(10,7))

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(cols[1:])))
ax.set_xticklabels(cols[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(rows)))
ax.set_yticklabels(rows, rotation=0)

# plot heatmap using sns.heatmap()
sns.heatmap(df, ax=ax, cmap='coolwarm', annot=True, cbar=False, linewidths=0.5)

# add title
plt.title('Popularity of Entertainment Categories')

# automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_31.png', bbox_inches='tight')

# clear current image state
plt.clf()