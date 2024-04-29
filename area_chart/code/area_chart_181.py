
#import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#convert data to dictionary
data = {'Year': ['2016', '2017', '2018', '2019', '2020'],
       'Food Production (Tons)': [10000, 11000, 12000, 13000, 14000],
       'Beverage Production (Tons)': [8000, 9000, 10000, 11000, 12000],
       'Food Imports (Tons)': [5000, 5500, 6000, 6500, 7000],
       'Beverage Imports (Tons)': [3000, 3200, 3500, 3800, 4000],
       'Food Exports (Tons)': [2000, 2200, 2400, 2600, 2800],
       'Beverage Exports (Tons)': [1000, 1200, 1300, 1400, 1500]}

#convert dictionary to dataframe
df = pd.DataFrame(data)

#convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

#calculate max total value for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

#round up max total value to the nearest multiple of 1000
if max_total_value < 1000:
    max_total_value = 1000
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

#set y ticks and ticklabels
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
yticklabels = [str(x) for x in yticks]

#set figure size
plt.figure(figsize=(12, 8))

#create area chart
ax = plt.gca()
ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.columns[1:], colors=['#E5C4D7', '#B6B6B6', '#FFDAB9', '#A2B5CD', '#7FFFD4', '#C2B280'], alpha=0.5)

#set x and y limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, max_total_value)

#set x and y ticks and ticklabels
ax.set_xticks(df.index)
ax.set_xticklabels(df.iloc[:, 0])

ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)

#set background grid lines
ax.grid(axis='y', color='grey', linestyle='--', linewidth=0.5)

#set legend position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

#set title
ax.set_title('Food and Beverage Production, Import, and Export Trends from 2016 to 2020', fontsize=16)

#resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_12.png', bbox_inches='tight')

#clear current image state
plt.clf()