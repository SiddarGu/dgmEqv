

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# import data
data = {'State': ['California', 'New York', 'Florida', 'Texas', 'Illinois'],
        'Median Home Price ($)': [500000, 400000, 300000, 250000, 200000],
        'Median Rent ($)': [2200, 1800, 1500, 1300, 1100],
        'Average Mortgage Payment ($)': [2500, 2000, 1800, 1600, 1400],
        'Average Property Taxes ($)': [500, 450, 375, 350, 300],
        'Average Home Insurance ($)': [200, 180, 160, 150, 120],
        'Average Utilities ($)': [500, 450, 375, 350, 300]}

# convert data to dataframe
df = pd.DataFrame(data)
# set State column as index
df = df.set_index('State')

# create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# plot heatmap using seaborn
sns.heatmap(df, cmap='Blues', annot=True, fmt='g', cbar=False)

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# set title
ax.set_title('Housing Costs by State')

# automatically resize image
fig.tight_layout()

# save figure
plt.savefig('output/final/heatmap/png/20231228-131639_30.png', bbox_inches='tight')

# clear current image state
plt.clf()