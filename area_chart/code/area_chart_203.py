
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# convert data to dictionary
data = {
    'Category': ['Art Galleries (Exhibitions)', 'Museums (Exhibitions)', 'Performing Arts (Shows)', 'Street Art (Exhibitions)', 'Cultural Festivals (Events)'],
    '2019': [100, 80, 120, 50, 40],
    '2020': [90, 70, 110, 60, 50],
    '2021': [110, 90, 130, 40, 30],
    '2022': [120, 100, 140, 30, 20],
    '2023': [130, 110, 150, 20, 10]
}

# convert data to dataframe
df = pd.DataFrame(data)

# convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
plt.figure(figsize=(12, 8))

# plot area chart
ax = plt.subplot()
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns)

# randomly set background grid lines
plt.grid(linestyle='dotted', linewidth=1, alpha=0.5)

# set legend position
plt.legend(loc='upper left')

# automatically resize image
plt.tight_layout()

# set title
plt.title('Arts and Culture Events by Category from 2019 to 2023')

# set x and y axis ticks and ticklabels
ax.set_xticks(np.arange(0, len(df.iloc[:, 0])))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
ax.set_xlim(0, len(df.iloc[:, 0]) - 1)

# calculate max total value and set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# set y label
plt.ylabel('Events')

# save figure
plt.savefig('output/final/area_chart/png/20231228-145339_38.png', bbox_inches='tight')

# clear current image state
plt.clf()