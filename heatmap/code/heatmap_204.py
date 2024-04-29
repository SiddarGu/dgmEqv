
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# import data
data = {'Category': ['Wheat (Tonnes per Hectare)', 'Corn (Tonnes per Hectare)', 'Rice (Tonnes per Hectare)', 'Soybeans (Tonnes per Hectare)', 'Barley (Tonnes per Hectare)', 'Potatoes (Tonnes per Hectare)'],
        'Crop Acreage': [3.2, 5.5, 3.0, 2.5, 4.0, 6.1],
        'Fertilizer Usage': [2.8, 4.8, 3.2, 2.7, 3.5, 5.0],
        'Water Usage': [3.5, 5.2, 2.7, 2.2, 3.0, 4.8],
        'Pesticide Usage': [4.0, 6.0, 6.5, 3.0, 5.5, 7.2]}

# convert data to dataframe
df = pd.DataFrame(data)

# set figure size
fig, ax = plt.subplots(figsize=(10,8))

# create heatmap
hm = sns.heatmap(df.iloc[:,1:], annot=True, cmap='Blues', cbar=False)

# set x and y ticks and labels
ax.set_yticks(np.arange(6)+0.5)
ax.set_yticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_xticks(np.arange(4)+0.5)
ax.set_xticklabels(df.columns[1:], rotation=45)

# set tick labels in center
ax.tick_params(axis='both', which='major', pad=5)

# set title
plt.title('Agriculture Production Factors by Crop Type')

# auto resize image
plt.tight_layout()

# save image
plt.savefig('output/final/heatmap/png/20231228-134212_77.png', bbox_inches='tight')

# clear current image state
plt.clf()