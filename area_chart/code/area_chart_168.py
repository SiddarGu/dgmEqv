
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create dictionary for data
data = {'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021],
        'Revenue ($)': [100000, 110000, 120000, 130000, 140000, 150000, 160000],
        'Expenses ($)': [80000, 85000, 90000, 95000, 100000, 105000, 110000],
        'Profit ($)': [20000, 25000, 30000, 35000, 40000, 45000, 50000]}

# convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# plot the data as an area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df['Year'], df['Revenue ($)'], df['Expenses ($)'], df['Profit ($)'], labels=['Revenue', 'Expenses', 'Profit'], colors=['#6baed6', '#fd8d3c', '#74c476'], alpha=0.75)

# randomly set background grid lines
ax.grid(axis='y', alpha=0.5)

# set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 1000) * 1000
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# set legend and position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# set title
ax.set_title('Business Revenue, Expenses, and Profit Analysis from 2015 to 2021')

# automatically resize image
fig.tight_layout()

# save figure
plt.savefig('output/final/area_chart/png/20231228-140159_88.png', bbox_inches='tight')

# clear current image state
plt.clf()