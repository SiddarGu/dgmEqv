

#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# data processing
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
        'Number of Houses Sold (Thousands)': [250, 180, 120, 100, 80, 70, 60, 50, 40, 30],
        'Median House Price ($)': [400000, 350000, 300000, 250000, 200000, 180000, 160000, 150000, 140000, 130000],
        'Average House Price ($)': [450000, 400000, 350000, 300000, 250000, 220000, 200000, 180000, 160000, 150000],
        'Median Rent ($)': [2000, 1800, 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900],
        'Average Rent ($)': [2200, 2000, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100]}

df = pd.DataFrame(data)

# plot the chart
fig, ax = plt.subplots(figsize=(9, 6))
ax = sns.heatmap(df.iloc[:, 1:], annot=True, fmt='g', cmap='Blues', cbar=False)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['City'], rotation=0, ha='right', rotation_mode='anchor')
# ax.xaxis.tick_top()
ax.tick_params(axis='both', which='both', length=0, pad=10)
ax.tick_params(axis='x', which='major', pad=20)
plt.title('Housing Market Statistics in Major US Cities')
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_81.png', bbox_inches='tight')
plt.close()

# clear the current image state
plt.clf()