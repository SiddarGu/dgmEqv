


# python code

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# create dictionary with data
data = {
    'Organization': ['Red Cross', 'UNICEF', 'Doctors Without Borders', 'World Wildlife Fund', 'Habitat for Humanity', 'American Cancer Society', 'St. Jude Children\'s Research Hospital', 'Salvation Army', 'Feeding America', 'United Way'],
    'Donations (thousands)': [100, 120, 80, 150, 90, 110, 130, 70, 140, 160],
    'Volunteers (thousands)': [50, 80, 40, 100, 60, 70, 90, 30, 95, 110],
    'Programs/Projects': [20, 30, 25, 35, 40, 28, 32, 22, 36, 38],
    'Impact (in millions)': [10, 15, 8, 20, 12, 14, 16, 6, 18, 22],
    'Awareness Campaigns': [5, 10, 7, 12, 8, 9, 10, 5, 11, 13],
    'Fundraising Events': [10, 12, 8, 15, 10, 11, 13, 6, 14, 16]
}

# convert dictionary to pandas dataframe
df = pd.DataFrame(data)

# set index as 'Organization'
df.set_index('Organization', inplace=True)

# create heatmap chart
fig, ax = plt.subplots(figsize=(10, 8))
heatmap = sns.heatmap(df, annot=True, fmt='g', cmap='Blues', cbar=False)

# set x and y ticks and labels
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_yticklabels(df.index, rotation=0)

# set ticks and labels in the center of rows and columns
ax.tick_params(axis='both', which='both', length=0)
ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=True)
ax.set_yticks(np.arange(len(df.index)) + 0.5, minor=True)
ax.set_xticklabels('', minor=True)
ax.set_yticklabels('', minor=True)

# set title
plt.title('Impact of Leading Nonprofit Organizations')

# resize and save chart
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_15.png', bbox_inches='tight')

# clear current image state
plt.clf()