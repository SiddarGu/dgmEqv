

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# define data
data = {'Product':['Widget A', 'Widget B', 'Widget C', 'Widget D', 'Widget E'],
        'Material Cost ($)':[10.50, 15.70, 8.25, 12.60, 9.80],
        'Production Time (Days)':[5, 7, 4, 6, 5],
        'Labor Cost ($)':[150, 175, 125, 200, 150],
        'Efficiency (%)':[92, 88, 95, 90, 94],
        'Defect Rate (%)':[1, 2, 0.5, 1.5, 1],
        'Maintenance Cost ($)':[50, 75, 25, 60, 40]}

# convert data to dataframe
df = pd.DataFrame(data)

# set figure size
fig = plt.figure(figsize=(12, 8))

# plot heatmap using ax
ax = fig.add_subplot(111)
heatmap = ax.imshow(df.iloc[:, 1:].values, cmap='coolwarm', interpolation='nearest')

# add colorbar
cbar = plt.colorbar(heatmap)

# set ticks and tick labels for x-axis
plt.xticks(np.arange(len(df.columns)-1), df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
# set ticks and tick labels for y-axis
plt.yticks(np.arange(len(df)), df['Product'])

# add title
plt.title('Production Costs and Efficiency')

# add value of each cell as text
for i in range(len(df)):
    for j in range(1, len(df.columns)):
        text = ax.text(j-1, i, df.iloc[i, j], ha='center', va='center', color='w')

# automatically resize the image
plt.tight_layout()

# save image
plt.savefig('output/final/heatmap/png/20231228-124154_33.png', bbox_inches='tight')

# clear current image state
plt.clf()