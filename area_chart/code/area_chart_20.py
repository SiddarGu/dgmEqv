
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create dictionary
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
        'Electricity (kWh)': [500, 450, 480, 520, 480, 500, 530, 520, 510, 480, 490, 510],
        'Water (Gallons)': [600, 650, 610, 590, 630, 600, 570, 610, 590, 620, 610, 580],
        'Gas (Cubic Feet)': [550, 600, 580, 540, 550, 570, 590, 560, 580, 540, 550, 570],
        'Solar Power (kWh)': [100, 120, 130, 90, 110, 90, 100, 120, 110, 100, 90, 120],
        'Wind Power (kWh)': [150, 180, 160, 140, 170, 160, 180, 150, 170, 160, 170, 150]}

# convert dictionary to dataframe
df = pd.DataFrame(data)

# convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# plot area chart
fig, ax = plt.subplots(figsize=(12, 6))

# set x and y axis range
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)

# randomly set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5)

# set x and y ticks and ticklabels
x_ticks = np.arange(len(df.index))
y_ticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_xticks(x_ticks)
ax.set_xticklabels(df.iloc[:, 0])
ax.set_yticks(y_ticks)

# set x and y axis labels
ax.set_xlabel('Month')
ax.set_ylabel('Energy Usage')

# plot area chart
ax.stackplot(x_ticks, df.iloc[:, 1:].T, labels=df.columns[1:], alpha=0.8)

# set legend
ax.legend(loc='upper left')

# set title
ax.set_title('Energy Usage by Month')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-103019_4.png', bbox_inches='tight')

# clear current image state
plt.clf()