
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create dataframe from data
data = {'Region': ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania'],
        'Total Revenue ($)': [500000, 400000, 600000, 200000, 100000, 50000],
        'Online Revenue ($)': [300000, 200000, 400000, 100000, 50000, 30000],
        'In-store Revenue ($)': [200000, 200000, 200000, 100000, 50000, 20000]}

df = pd.DataFrame(data)

# convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
plt.figure(figsize=(10, 6))

# plot area chart
ax = plt.subplot()
ax.stackplot(df['Region'], df['Total Revenue ($)'], df['Online Revenue ($)'], df['In-store Revenue ($)'], labels=['Total Revenue', 'Online Revenue', 'In-store Revenue'])

# randomly set background grid lines
ax.grid(linestyle='--', linewidth=0.5, alpha=0.5)

# set x and y axis ticks and tick labels
if np.random.rand() < 0.7:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Region'])
    ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000)
    ax.set_yticks(np.linspace(0, ax.get_ylim()[1], np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(ax.get_yticks())

# set rotation and wrap for long x labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# add legend
ax.legend(loc='upper left')

# set title
ax.set_title('Retail and E-commerce Revenue by Region')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_66.png', bbox_inches='tight')

# clear figure state
plt.close()