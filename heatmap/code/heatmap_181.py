
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# define data
data = {'Data Storage (GB)': [250,500,750,1000,1250,1500,1750,2000,2250,2500],
        'Processing Speed (GHz)': [2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0],
        'Energy Efficiency (W)': [10,8,6,4,2,1,0.5,0.3,0.2,0.1],
        'Memory Capacity (GB)': [500,750,1000,1250,1500,1750,2000,2250,2500,2750],
        'Material Strength (MPa)': [50,60,70,80,90,100,110,120,130,140]}
df = pd.DataFrame(data, index=['Category 1','Category 2','Category 3','Category 4','Category 5',
                               'Category 6','Category 7','Category 8','Category 9','Category 10'])

# set up figure size
plt.figure(figsize=(10,8))

# plot the heatmap
ax = sns.heatmap(df, annot=True, fmt='.1f', cmap='Blues', cbar=False)

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# set title
plt.title('Advancements in Science and Engineering')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_38.png', bbox_inches='tight')

# clear current image state
plt.clf()