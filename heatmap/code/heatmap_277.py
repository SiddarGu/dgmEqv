
# import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# define data
data = {'Category': ['Fossil Fuel Power Plants', 'Nuclear Power Plants', 'Solar Energy Plants', 'Hydroelectric Power Plants', 'Wind Power Plants', 'Geothermal Power Plants'],
        'United States': [75, 22, 10, 8, 9, 2],
        'China': [85, 26, 12, 10, 11, 4],
        'India': [80, 20, 13, 9, 10, 3],
        'Japan': [70, 25, 15, 6, 9, 2],
        'Germany': [60, 30, 20, 5, 8, 2],
        'United Kingdom': [50, 35, 25, 4, 7, 2]}

# convert data to pandas dataframe
df = pd.DataFrame(data)
df = df.set_index('Category')

# create figure and axes
fig, ax = plt.subplots(figsize=(12,8))

# plot heatmap using imshow()
heatmap = ax.imshow(df, cmap='YlGn')

# add colorbar
plt.colorbar(heatmap)

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)
ax.tick_params(axis='x', which='major', pad=10)

# rotate and align x tick labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# center ticks and ticklabels
ax.set_xticks(np.arange(df.shape[1]+1)-.5, minor=True)
ax.set_yticks(np.arange(df.shape[0]+1)-.5, minor=True)
ax.tick_params(axis='both', which='minor', length=0)
ax.tick_params(axis='both', which='major', length=10, pad=10)

# set title
plt.title('Power Plant Distribution by Country')

# show values in each cell
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='black', size=12)

# automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_10.png', bbox_inches='tight')

# clear current image state
plt.clf()