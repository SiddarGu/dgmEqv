
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import data and process using dict and pandas
data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'Brazil'],
    'CO2 Emissions (Tonnes)': [6.2, 9.8, 4.5, 5.5, 11.5, 3.5],
    'Renewable Energy (%)': [20, 15, 30, 40, 10, 25],
    'Air Pollution (ppm)': [50, 70, 40, 35, 80, 60],
    'Water Usage (Litres)': [500, 600, 350, 300, 700, 400],
    'Waste Production (Tonnes)': [2, 2.5, 1.5, 1, 3, 1.2],
    'Land Use (Hectares)': [100, 120, 80, 70, 150, 90]
}

df = pd.DataFrame(data).set_index('Country')

# set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# plot heatmap using pcolor()
heatmap = ax.pcolor(df, cmap='BuPu')

# add colorbar
cbar = fig.colorbar(heatmap, ax=ax)

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# add title
ax.set_title('Environmental Impact by Country')

# automatically resize image
fig.tight_layout()

# save image
fig.savefig('output/final/heatmap/png/20231228-131639_88.png', bbox_inches='tight')

# clear current image state
plt.clf()