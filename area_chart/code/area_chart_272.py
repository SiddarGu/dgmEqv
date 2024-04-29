


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create dictionary for data
data = {'2020': ['Q1', 'Q2', 'Q3', 'Q4'],
        'Revenue ($)': [5000, 5200, 4500, 5100],
        'Expenses ($)': [4000, 4100, 4900, 3500],
        'Profit ($)': [1000, 1100, 400, 1600]}

# process data with pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
fig, ax = plt.subplots(figsize=(12, 6))

# create stacked area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=['Revenue', 'Expenses', 'Profit'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.7)

# randomly set background grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.3)

# set x and y axis ticks and ticklabels with 70% probability
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor', fontsize=12)
    ax.set_xlim(0, len(df.index) - 1)
if np.random.choice([True, False], p=[0.7, 0.3]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    # ceil max_total_value up to the nearest multiple of 10, 100 or 1000
    if max_total_value < 100:
        max_total_value = np.ceil(max_total_value / 10) * 10
    elif max_total_value < 1000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    # set yticks with length in list of [3, 5, 7, 9, 11]
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    # set yticklabels with wrap=true for longer strings
    if max_total_value < 1000:
        ax.set_yticklabels(np.arange(0, max_total_value + 1, max_total_value / len(ax.get_yticks())).astype(int),
                           rotation=0, ha='right', rotation_mode='anchor', fontsize=12, wrap=True)
    else:
        ax.set_yticklabels(np.arange(0, max_total_value + 1, max_total_value / len(ax.get_yticks())).astype(int),
                           rotation=0, ha='right', rotation_mode='anchor', fontsize=12)
    # set ylim with max_total_value
    ax.set_ylim(0, max_total_value)

# set legend and legend title
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=12, frameon=False, title='Performance')
ax.get_legend().get_title().set_fontsize('14')

# set title
ax.set_title('Quarterly Financial Performance in 2020', fontsize=16)

# automatically resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_35.png', bbox_inches='tight')

# clear current image state
plt.clf()