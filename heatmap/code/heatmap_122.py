
# import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# define data
data = {'Field': ['Biology', 'Chemistry', 'Physics', 'Engineering', 'Computer Science', 'Math'],
        'Research Papers Published': [230, 120, 80, 300, 400, 50],
        'Patents Filed': [20, 10, 5, 30, 40, 3],
        'Citations Per Paper': [12, 14, 20, 10, 8, 25],
        'Grant Funding (in Millions)': [5.2, 3.5, 2.0, 6.0, 8.0, 1.0],
        'Collaboration Index': [0.8, 0.6, 0.5, 0.9, 0.7, 0.4]}

# convert data to dataframe
df = pd.DataFrame(data)

# set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# plot heatmap
heatmap = ax.imshow(df.iloc[:, 1:], cmap='Blues')

# add colorbar
plt.colorbar(heatmap)

# set ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Field'])))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Field'], rotation=0)

# set ticks and ticklabels in the center of rows and columns
# ax.set_xticks(np.arange(len(df.columns[1:]))+0.5, minor=True)
# ax.set_yticks(np.arange(len(df['Field']))+0.5, minor=True)
# ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor', minor=True)
# ax.set_yticklabels(df['Field'], rotation=0, minor=True)
# ax.tick_params(which='minor', length=0)

# add title
ax.set_title('Research and Collaboration in Science and Engineering')

# show values in each cell
for i in range(len(df['Field'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j+1],
                       ha='center', va='center', color='k')

# automatically resize the image
plt.tight_layout()

# save figure
plt.savefig('output/final/heatmap/png/20231228-131639_26.png', bbox_inches='tight')

# clear current image state
plt.clf()