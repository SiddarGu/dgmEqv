
# import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create dictionary from data
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'Website Visits (millions)': [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050],
        'Social Media Accounts (millions)': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
        'Active Users (millions)': [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520],
        'Time Spent (hours)': [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420],
        'Content Posted (millions)': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]}

# convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
fig, ax = plt.subplots(figsize=(12, 7))

# calculate max total value and round up to nearest multiple of 100
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100

# set y limits and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# set background grid lines
ax.grid(axis='y', alpha=0.5)

# plot data as stacked area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Website Visits (millions)', 'Social Media Accounts (millions)', 'Active Users (millions)', 'Time Spent (hours)', 'Content Posted (millions)'], colors=['#0099cc', '#ffcc00', '#ff9900', '#009933', '#cc6699'], alpha=0.7)

# set legend and its position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# set x and y labels
ax.set_xlabel('Month')
ax.set_ylabel('Number (millions)')

# set x ticks and labels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# set title
ax.set_title('Social Media and Web Usage in 2020')

# resize image and save
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-140159_3.png', bbox_inches='tight')

# clear figure
plt.clf()