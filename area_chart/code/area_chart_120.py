
#import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#convert data to dictionary format
data = {'Category': ['State', 'Federal', 'Local', 'International'],
        'Tax Revenue ($)': [200000, 100000, 150000, 100000],
        'Public Health Spending ($)': [150000, 120000, 180000, 200000],
        'Education Funding ($)': [180000, 150000, 200000, 250000],
        'Infrastructure Budget ($)': [130000, 100000, 150000, 180000]}

#convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

#plot the chart using ax.stackplot()
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df['Category'], df['Tax Revenue ($)'], df['Public Health Spending ($)'], df['Education Funding ($)'], df['Infrastructure Budget ($)'], labels=['Tax Revenue', 'Public Health Spending', 'Education Funding', 'Infrastructure Budget'], colors=['#FFD700', '#FF8C00', '#E9967A', '#FF69B4'], alpha=0.8)

#set x and y axis ticks and tick labels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df['Category'])

#calculate max total value and set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_value)
ax.set_yticks(np.linspace(0, max_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

#set background grid lines
ax.grid(axis='both', color='#DCDCDC', linestyle='-', linewidth=1, alpha=0.5)

#adjust legend position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

#set title and labels
plt.title('Government Expenditure by Level and Sector')
plt.xlabel('Category')
plt.ylabel('Amount ($ in millions)')

#resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_31.png', bbox_inches='tight')

#clear current image state
plt.clf()