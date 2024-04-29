

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# set data
data = {'Category': ['Soccer', 'Football', 'Basketball', 'Baseball', 'Tennis'],
        'Players': [500, 300, 400, 200, 100],
        'Coaches': [100, 200, 300, 400, 500],
        'Referees': [50, 100, 150, 200, 250],
        'Stadiums': [200, 300, 400, 500, 600],
        'Fans': [600, 500, 400, 300, 200]}

# convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# calculate max total value and set y-axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

# create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# plot stacked area chart
ax.stackplot(df.index, df.iloc[:, 1:].values.T, labels=df.columns[1:])

# set ticks and ticklabels for x-axis
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(df.index)
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# set ticks and ticklabels for y-axis
ax.set_ylim(0, max_total_value)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)

# add grid lines
ax.grid(color='lightgrey', linestyle='--')

# set legend and title
ax.legend(loc='upper left')
ax.set_title('Sports and Entertainment by Category')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_69.png', bbox_inches='tight')

# clear current image state
plt.clf()