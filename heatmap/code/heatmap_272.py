

# import the required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# define the data
data = {'Country': ['Europe', 'North America', 'Asia', 'South America', 'Africa', 'Australia'],
        'Trucks per 1000 People': [85, 90, 75, 80, 60, 70],
        'Railways per 1000 People': [45, 50, 60, 30, 20, 25],
        'Airports per 1000 People': [20, 15, 18, 10, 8, 10],
        'Ports per 1000 People': [10, 12, 8, 15, 5, 7]}

# convert data to dataframe
df = pd.DataFrame(data)

# set the index to Country
df = df.set_index('Country')

# create a figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# plot the heatmap
im = ax.imshow(df, cmap='Blues')

# add a colorbar
cbar = fig.colorbar(im)

# set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))

ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', fontsize=12)
ax.set_yticklabels(df.index, fontsize=12)

# loop over data dimensions and create text annotations
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='black', fontsize=12)

# add a title
ax.set_title('Transportation Infrastructure by Country', fontsize=16)

# automatically resize the image
fig.tight_layout()

# save the figure
plt.savefig('output/final/heatmap/png/20231228-162116_5.png', bbox_inches='tight')

# clear the current image state
plt.clf()