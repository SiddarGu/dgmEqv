
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {'Country': ['United States', 'China', 'India', 'Brazil', 'Mexico', 'Germany', 'Australia'],
        'Air Pollution (μg/m³)': [12, 20, 30, 15, 18, 8, 5],
        'Water Pollution (mg/L)': [0.5, 0.7, 0.9, 0.6, 0.8, 0.4, 0.3],
        'Waste Production (kg/person)': [3.2, 4.5, 5.0, 3.8, 3.5, 2.0, 1.5],
        'Renewable Energy Usage (%)': [25, 18, 15, 20, 22, 30, 35],
        'Deforestation (%)': [2, 5, 7, 3, 4, 1, 0.5],
        'Greenhouse Gas Emissions (tonnes/person)': [18, 22, 25, 20, 20, 15, 12]
        }
df = pd.DataFrame(data)
df.set_index('Country', inplace=True)

fig, ax = plt.subplots(figsize=(10, 8))

im = ax.imshow(df, cmap='YlOrBr')

# set ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# center ticks
ax.set_xticks(np.arange(len(df.columns)) - 0.5, minor=True)
ax.set_yticks(np.arange(len(df.index)) - 0.5, minor=True)

# rotate and wrap tick labels if necessary
if len(ax.get_xticklabels()[0].get_text()) > 6:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
if len(ax.get_yticklabels()[0].get_text()) > 6:
    ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# add colorbar
cb = fig.colorbar(im, ax=ax)

# add title
ax.set_title('Environmental Impact by Country')

# show or hide cell values
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j],
                       ha='center', va='center', color='black' if df.iloc[i, j] < 20 else 'white')

# resize and save image
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_14.png', bbox_inches='tight')

# clear current image state
plt.clf()