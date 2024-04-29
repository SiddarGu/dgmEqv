

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# set the data
data = {'Product': ['Widget A', 'Widget B', 'Widget C', 'Widget D', 'Widget E'],
        'Production Rate': [1000, 800, 1200, 900, 1100],
        'Defect Rate': [2, 1.5, 1, 2.5, 2],
        'Packaging Efficiency': [90, 85, 95, 92, 88],
        'Quality Control': [98, 95, 97, 99, 96],
        'Material Waste': [5, 4, 3, 6, 5],
        'Inventory Turnover': [12.5, 11, 10, 13, 11.5]}

# convert data to pandas dataframe
df = pd.DataFrame(data)

# set the index to be the product names
df.set_index('Product', inplace=True)

# set the figure size
fig, ax = plt.subplots(figsize=(10, 8))

# plot the heatmap using seaborn
sns.heatmap(df, annot=True, cmap='Blues', linewidths=.5, ax=ax)

# set the ticks and ticklabels for x and y axis
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='right', rotation_mode='anchor')

# set the ticks and ticklabels in the center of rows and columns
ax.set_xticks(np.arange(0.5, len(df.columns) + 0.5, 1))
ax.set_yticks(np.arange(0.5, len(df.index) + 0.5, 1))

# add a colorbar
cbar = ax.collections[0].colorbar
cbar.set_ticks([0, 20, 40, 60, 80, 100])
cbar.set_ticklabels(['0', '20', '40', '60', '80', '100'])

# set the title
ax.set_title('Manufacturing Metrics by Product')

# automatically resize the image
fig.tight_layout()

# save the figure
plt.savefig('output/final/heatmap/png/20231228-163105_32.png', bbox_inches='tight')

# clear the current image state
plt.clf()
plt.close()