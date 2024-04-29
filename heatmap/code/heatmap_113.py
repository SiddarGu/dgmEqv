
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# data processing
data = {'Product': ['Starbucks', 'McDonald\'s', 'Coca-Cola', 'Budweiser', 'Lay\'s', 'Kellogg\'s'], 'Coffee': [35, 15, 10, 5, 20, 5], 'Tea': [25, 10, 20, 5, 10, 20], 'Soft Drinks': [15, 20, 30, 10, 10, 5], 'Alcoholic Beverages': [10, 25, 15, 45, 10, 5], 'Snacks': [10, 20, 10, 25, 30, 20], 'Meals/Breakfast': [5, 10, 15, 10, 20, 45]}

df = pd.DataFrame(data)
df = df.set_index('Product')

# plot the chart
fig, ax = plt.subplots(figsize=(10, 8))

# heatmap chart using sns.heatmap()
sns.heatmap(df, annot=True, cmap="Blues", cbar=False, linewidths=.5, fmt='g')

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns))+0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df))+0.5)
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# set ticks and ticklabels in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns))+0.5, minor=True)
ax.set_xticklabels('', minor=True)
ax.set_yticks(np.arange(len(df))+0.5, minor=True)
ax.set_yticklabels('', minor=True)

# add colorbar
cbar = ax.figure.colorbar(ax.collections[0])
cbar.ax.tick_params(labelsize=12)

# set title
plt.title('Product Distribution in Food and Beverage Industry', fontsize=16)

# resize image
plt.tight_layout()

# save image
plt.savefig('output/final/heatmap/png/20231228-131639_14.png', bbox_inches='tight')

# clear current image state
plt.clf()