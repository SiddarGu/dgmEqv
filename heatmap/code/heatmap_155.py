

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# import data
data = {'Country': ['United States', 'China', 'Brazil', 'India', 'Russia', 'France'], 
        'Wheat (Tonnes per Hectare)': [3.2, 2.8, 3.5, 4.0, 1.8, 3.1], 
        'Corn (Tonnes per Hectare)': [5.5, 4.8, 5.2, 6.0, 2.5, 4.0], 
        'Rice (Tonnes per Hectare)': [3.0, 3.2, 2.7, 6.5, 2.2, 3.6], 
        'Soybeans (Tonnes per Hectare)': [2.5, 2.7, 2.2, 3.0, 1.5, 2.8], 
        'Barley (Tonnes per Hectare)': [4.0, 3.5, 3.0, 5.5, 2.0, 4.2], 
        'Potatoes (Tonnes per Hectare)': [6.1, 5.0, 4.8, 7.2, 3.5, 5.0]}

# convert data to dataframe
df = pd.DataFrame(data)

# set country as index
df.set_index('Country', inplace=True)

# create figure and axes
fig, ax = plt.subplots(figsize=(8,6))

# plot heatmap using seaborn
sns.heatmap(df, cmap='YlGnBu', annot=True, cbar=False, ax=ax)

# set x and y ticks and labels
ax.set_xticks(np.arange(len(df.columns))+0.5)
ax.set_yticks(np.arange(len(df.index))+0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0,)

# add title and adjust layout
plt.title('Crop Yields by Country')
plt.tight_layout()

# save figure
plt.savefig('output/final/heatmap/png/20231228-131639_76.png', bbox_inches='tight')

# clear current image state
plt.clf() 