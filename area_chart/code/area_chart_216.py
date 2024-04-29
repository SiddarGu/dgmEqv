
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# create dataframe
data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Electricity Consumption (kWh)': [5000, 4800, 4600, 4400, 4200],
        'Water Usage (gal)': [10000, 10500, 11000, 11500, 12000],
        'Waste Production (lbs)': [5000, 4800, 4600, 4400, 4200],
        'Carbon Emissions (tons)': [2000, 1900, 1800, 1700, 1600]}

df = pd.DataFrame(data)

# convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# plot area chart
ax.stackplot(df['Year'], df.iloc[:, 1:].values.T, labels=df.columns[1:], alpha=0.8)

# set x and y axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Amount')

# set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)

# calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# ceil max total value up to the nearest multiple of 10, 100, or 1000
if max_total_value > 1000:
    max_total_value = np.ceil(max_total_value / 1000) * 1000
elif max_total_value > 100:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 10) * 10

# set y axis range and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# randomly set background grid lines
ax.grid(color=np.random.rand(3,), linestyle='dashed')

# set legend and legend position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# set title
plt.title('Environmental Impact Trends')

# automatically resize image
plt.tight_layout()

# save figure
plt.savefig(os.path.join('output', 'final', 'area_chart', 'png', '20231228-145339_55.png'), bbox_inches='tight')

# clear current image state
plt.clf()