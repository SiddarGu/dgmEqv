


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# convert data to dictionary
data = {'Sport': ['MLB', 'NFL', 'NBA', 'NHL'],
        'Football (%)': [30, 35, 25, 10],
        'Basketball (%)': [35, 30, 25, 10],
        'Soccer (%)': [40, 25, 30, 5],
        'Tennis (%)': [25, 35, 35, 5],
        'Golf (%)': [20, 30, 40, 10]}

# convert data to dataframe
df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(8, 6))

# create heatmap using seaborn
ax = sns.heatmap(df.iloc[:, 1:], annot=True, cmap='Blues')

# set x and y ticks and labels
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df['Sport'])))
ax.set_yticklabels(df['Sport'], rotation=0, ha='right', rotation_mode='anchor')

# set ticks and ticklabels in the center
ax.set_xticks(np.arange(len(df.columns[1:])) + 0.5, minor=True)
ax.set_yticks(np.arange(len(df['Sport'])) + 0.5, minor=True)
ax.set_xticklabels(df.columns[1:], minor=False)
ax.set_yticklabels(df['Sport'], minor=False)

# add colorbar
cbar = ax.collections[0].colorbar
cbar.set_ticks(np.arange(0, 41, 10))
cbar.set_ticklabels(np.arange(0, 41, 10))

# set title
plt.title('Popularity of Major Sports Leagues')

# resize image
plt.tight_layout()

# save figure
plt.savefig('output/final/heatmap/png/20231228-124154_84.png', bbox_inches='tight')

# clear current image state
plt.clf()