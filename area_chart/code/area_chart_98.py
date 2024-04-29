
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# define data
data = {'Field': ['Psychology', 'Sociology', 'Anthropology', 'Economics', 'Political Science'],
        '2018': [20, 25, 15, 20, 20],
        '2019': [25, 30, 20, 15, 10],
        '2020': [30, 25, 20, 15, 10],
        '2021': [25, 20, 25, 20, 10],
        '2022': [20, 25, 20, 20, 15]}

# convert data to dataframe
df = pd.DataFrame(data)

# convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figsize
fig, ax = plt.subplots(figsize=(10, 6))

# calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# ceil max total value up to the nearest multiple of 10, 100 or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# set y limit
ax.set_ylim(0, max_total_value)

# set y ticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# set x limit
ax.set_xlim(0, len(df.index) - 1)

# create background grid lines
ax.grid(color='grey', linestyle='dashed', alpha=0.3)

# set colors and transparency
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
alpha = 0.7

# plot stacked area chart
ax.stackplot(df['Field'], df['2018'], df['2019'], df['2020'], df['2021'], df['2022'], labels=['2018', '2019', '2020', '2021', '2022'], colors=colors, alpha=alpha)

# set legend
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

# set title
plt.title('Trends in Social Sciences and Humanities Fields')

# automatically resize image
plt.tight_layout()

# save figure
plt.savefig('output/final/area_chart/png/20231228-131755_88.png', bbox_inches='tight')

# clear current image state
plt.clf()