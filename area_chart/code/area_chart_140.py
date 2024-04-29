
#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# define data
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December'],
        'Logistics Companies ($)': [250, 270, 280, 300, 350, 400, 450, 500, 550, 600, 650, 700],
        'Transportation Services ($)': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 350],
        'Storage Facilities ($)': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 300],
        'Packaging Materials ($)': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 250]}

# process data
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# plot data as stacked area chart
ax.stackplot(df['Month'], df['Logistics Companies ($)'], df['Transportation Services ($)'],
             df['Storage Facilities ($)'], df['Packaging Materials ($)'], labels=['Logistics Companies', 'Transportation Services',
                                                                                  'Storage Facilities', 'Packaging Materials'],
             colors=['#003f5c', '#ffa600', '#665191', '#f95d6a'], alpha=0.75)

# set ticks and tick labels for x axis
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Month'])

# set rotation for x axis labels
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# randomly set background grid lines
plt.grid(axis='y', linestyle='--', alpha=0.25)

# calculate max total value and set y limits and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))

# set title
ax.set_title('Yearly Expenses for Transportation and Logistics')

# automatically resize image
plt.tight_layout()

# save image
plt.savefig('output/final/area_chart/png/20231228-140159_54.png', bbox_inches='tight')

# clear current image state
plt.clf()