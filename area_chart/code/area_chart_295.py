
## Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Define data as dictionary
data = {'Product': ['2015', '2016', '2017', '2018', '2019'],
        'Corn (lbs)': [800, 850, 900, 950, 1000],
        'Wheat (lbs)': [1000, 950, 900, 850, 800],
        'Rice (lbs)': [1200, 1250, 1300, 1350, 1400],
        'Soybeans (lbs)': [600, 650, 700, 750, 800],
        'Potatoes (lbs)': [500, 550, 600, 650, 700]}

## Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

## Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

## Set x and y axis labels
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Crop Production (lbs)", fontsize=14)

## Set title
ax.set_title("Crop Production by Year and Type", fontsize=16)

## Set x and y axis ticks and ticklabels
if np.random.randint(0, 100) < 70:
  ax.set_xlim(0, len(df.index) - 1)
  ax.set_xticks(np.arange(len(df.index)))
  ax.set_xticklabels(df.iloc[:, 0])
if np.random.randint(0, 100) < 70:
  max_total_value = df.iloc[:, 1:].sum(axis=1).max()
  max_total_value = np.ceil(max_total_value / 100) * 100
  ax.set_ylim(0, max_total_value)
  ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
  ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

## Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:], labels=df.columns[1:], colors=['#4D4D4D', '#5DADE2', '#E74C3C', '#F4D03F', '#27AE60'], alpha=0.5)

## Set background grid lines
ax.grid(color='#B2BABB')

## Set legend
ax.legend(loc='upper left', fontsize=12)

## Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-161902_2.png', bbox_inches='tight')

## Clear current image state
plt.clf()
