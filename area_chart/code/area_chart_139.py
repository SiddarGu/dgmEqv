
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create dictionary from data
data_dict = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Revenue ($)': [100000, 110000, 120000, 130000],
    'Profit ($)': [25000, 30000, 35000, 40000],
    'Operating Expenses ($)': [40000, 45000, 50000, 55000],
    'Net Income ($)': [20000, 25000, 30000, 35000]
}

# convert first column to string type
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# create figure and axes
fig, ax = plt.subplots(figsize=(10, 8))

# set background grid lines
ax.grid()

# calculate max total value and set y-axis limits and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# plot area chart
ax.stackplot(df['Quarter'], df['Revenue ($)'], df['Profit ($)'], df['Operating Expenses ($)'], df['Net Income ($)'], labels=['Revenue ($)', 'Profit ($)', 'Operating Expenses ($)', 'Net Income ($)'], colors=['#B2FF66', '#FFB266', '#66B2FF', '#FF66B2'], alpha=0.8)

# set legend position and labels
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0, frameon=False)
ax.set_ylabel('($)')
ax.set_xlabel('Quarter')

# set x-axis limits and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))

# rotate and wrap x-axis labels
ax.set_xticklabels(df['Quarter'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# set title
ax.set_title('Quarterly Financial Performance')

# automatically resize image
fig.tight_layout()

# save figure
plt.savefig('output/final/area_chart/png/20231228-140159_53.png', bbox_inches='tight')

# clear current image state
plt.clf()