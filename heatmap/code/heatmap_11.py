
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import seaborn as sns

# create data
data = {'Field': ['Research', 'Education', 'Industry', 'Government'], 'Engineering': [20, 30, 35, 15], 'Chemistry': [10, 25, 30, 35], 'Biology': [15, 15, 15, 25], 'Physics': [30, 10, 20, 20], 'Computer Science': [25, 20, 25, 30], 'Mathematics': [12, 30, 28, 30]}

# convert data to pandas dataframe
df = pd.DataFrame(data)

# set index to Field column
df.set_index('Field', inplace=True)

# plot heatmap using pcolor()
fig, ax = plt.subplots(figsize=(10, 6))
im = ax.pcolor(df, cmap='Blues')

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns))+0.5, minor=False)
ax.set_yticks(np.arange(len(df.index))+0.5, minor=False)
ax.set_xticklabels(df.columns, minor=False)
ax.set_yticklabels(df.index, minor=False)

# set ticks and ticklabels in the center of rows and columns
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top')
ax.invert_yaxis()

# rotate x-axis labels
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# add colorbar
plt.colorbar(im)

# set title
plt.title('Scientific Fields and Their Involvement in Various Areas')

# automatically resize the image
plt.tight_layout()

# save figure
plt.savefig('output/final/heatmap/png/20231225-210514_33.png', bbox_inches='tight')

# clear current image state
plt.clf()