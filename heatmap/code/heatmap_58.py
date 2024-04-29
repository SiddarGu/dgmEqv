

           
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data
data = {'Category': ['US', 'China', 'Japan', 'Germany', 'India', 'Russia'],
        'Hydroelectricity (MW)': [70, 80, 60, 50, 90, 40],
        'Wind (MW)': [50, 60, 40, 30, 70, 20],
        'Solar (MW)': [100, 120, 80, 60, 140, 40],
        'Geothermal (MW)': [40, 50, 30, 20, 60, 10],
        'Biomass (MW)': [60, 70, 50, 40, 80, 30],
        'Nuclear (MW)': [80, 90, 70, 50, 100, 60]}

# create dataframe
df = pd.DataFrame(data)

# set index
df.set_index('Category', inplace=True)

# create figure and axes
fig, ax = plt.subplots(figsize=(10, 7))

# plot heatmap using seaborn
sns.heatmap(df, cmap='RdYlGn_r', annot=True, fmt='g', ax=ax)

# set x and y ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='center')

# set title
ax.set_title('Renewable Energy Capacity by Country')

# resize image
fig.tight_layout()

# save figure
fig.savefig('output/final/heatmap/png/20231228-124154_46.png', bbox_inches='tight')

# clear current image state
plt.clf()