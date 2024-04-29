
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# define data
data = {'Revenue Stream': ['Advertising', 'Product Sales', 'Subscription Fees', 'Licensing Fees', 'Investment Income'],
        'Company A': [40, 50, 5, 3, 2],
        'Company B': [20, 10, 50, 15, 5],
        'Company C': [60, 25, 10, 2, 3],
        'Company D': [5, 5, 70, 15, 5],
        'Company E': [30, 20, 40, 5, 5],
        'Company F': [10, 20, 50, 10, 10],
        'Company G': [20, 30, 35, 10, 5],
        'Company H': [50, 30, 10, 5, 5],
        'Company I': [10, 30, 40, 10, 10]}

# create dataframe
df = pd.DataFrame(data)

# set index
df.set_index('Revenue Stream', inplace=True)

# plot heatmap
fig, ax = plt.subplots(figsize=(10, 6))
heatmap = ax.imshow(df, cmap='Blues', interpolation='nearest')

# add colorbar
plt.colorbar(heatmap)

# show values
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        text = ax.text(j, i, df.iloc[i, j],
                       ha="center", va="center", color="w")

# set x and y ticks and labels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# rotate x ticks
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# set ticks to be in the center of cells
ax.set_xticks(np.arange(df.shape[1]+1)-0.5, minor=True)
ax.set_yticks(np.arange(df.shape[0]+1)-0.5, minor=True)
ax.tick_params(which="minor", bottom=False, left=False)

# set title
plt.title('Revenue Distribution by Company')

# resize and save figure
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_37.png', bbox_inches='tight')

# clear current image state
plt.clf()