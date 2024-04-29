
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# import data using pandas
data = pd.DataFrame({'Policy Area': ['Taxation', 'Education', 'Healthcare', 'Housing', 'Environment'],
                     'United States': [30, 25, 20, 10, 15],
                     'Canada': [28, 26, 20, 12, 14],
                     'United Kingdom': [32, 28, 18, 9, 13],
                     'Australia': [29, 27, 19, 11, 14]})

# set figure size
plt.figure(figsize=(10, 8))

# plot heatmap using seaborn
ax = sns.heatmap(data.iloc[:, 1:], annot=True, cmap='Blues', cbar=False, linewidths=0.5)

# set ticks and ticklabels for x and y axis
ax.set_xticklabels(data.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(data['Policy Area'], rotation=0, wrap=True)

# center ticks
ax.set_xticklabels(ax.get_xticklabels(), ha='center')
ax.set_yticklabels(ax.get_yticklabels(), va='center')

# add title
ax.set_title('Government Spending by Country')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_54.png', bbox_inches='tight')

# clear current image state
plt.clf()