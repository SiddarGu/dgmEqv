
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# import data
data = {
    'Category': ['Education', 'Health', 'Environment', 'Poverty', 'Arts and Culture'],
    'Donations ($)': [500000, 750000, 300000, 1000000, 200000],
    'Volunteers (hrs)': [1000, 2000, 500, 3000, 250],
    'Fundraising Events': [10, 15, 5, 20, 2],
    'Awareness Campaigns': [5, 8, 3, 10, 1],
    'Programs': [20, 25, 10, 30, 5]
}

# convert data to dataframe
df = pd.DataFrame(data)

# set index to Category column
df.set_index('Category', inplace=True)

# create figure and axes
fig, ax = plt.subplots(figsize=(12,8))

# plot heatmap using seaborn
sns.heatmap(df, cmap='Blues', annot=True, fmt='.0f', cbar=False)

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=False)
ax.set_yticks(np.arange(len(df.index)) + 0.5, minor=False)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# set ticks and ticklabels in the center of rows and columns
# ax.xaxis.set_ticks_position('none')
# ax.yaxis.set_ticks_position('none')
# ax.xaxis.set_tick_params(labeltop='on', labelbottom='off')
# ax.yaxis.set_tick_params(labelright='on', labelleft='off')

# add title
ax.set_title('Impact of Charity and Nonprofit Organizations')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231225-210514_8.png', bbox_inches='tight')

# clear current image state
plt.clf()