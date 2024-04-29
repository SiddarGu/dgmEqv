
#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create dictionary
data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Single Family Home Sales (Units)': [800, 750, 700, 650, 600],
        'Condo Sales (Units)': [500, 550, 600, 650, 700],
        'Multi-Family Home Sales (Units)': [200, 250, 300, 350, 400],
        'New Construction Sales (Units)': [300, 350, 400, 450, 500]}

# convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
fig = plt.figure(figsize=(12, 8), dpi=80)

# plot area chart
ax = fig.add_subplot(111)
ax.stackplot(df['Year'], df['Single Family Home Sales (Units)'],
             df['Condo Sales (Units)'], df['Multi-Family Home Sales (Units)'],
             df['New Construction Sales (Units)'], colors=['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c'], alpha=0.7)

# set x and y ticks and ticklabels
if np.random.random() < 0.7:
    ax.set_xticks(np.arange(len(df['Year'])))
    ax.set_xticklabels(df['Year'])
if np.random.random() < 0.7:
    # set rotation and wrap for longer labels
    ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
if np.random.random() < 0.7:
    ax.set_yticks(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max()), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# set ylimit
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max())
if max_total_value <= 10:
    ax.set_ylim(0, max_total_value)
elif 10 < max_total_value <= 100:
    ax.set_ylim(0, np.ceil(max_total_value / 10) * 10)
elif 100 < max_total_value <= 1000:
    ax.set_ylim(0, np.ceil(max_total_value / 100) * 100)

# randomly set background grid lines
if np.random.random() < 0.5:
    ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.3)

# set legend
ax.legend(['Single Family Home Sales', 'Condo Sales', 'Multi-Family Home Sales', 'New Construction Sales'], loc='upper right')

# set title and labels
ax.set_title('Housing Sales Trends by Property Type from 2019 to 2023')
ax.set_xlabel('Year')
ax.set_ylabel('Sales (Units)')

# automatically resize image
fig.tight_layout()

# save figure
fig.savefig('output/final/area_chart/png/20231226-103019_7.png', bbox_inches='tight')

# clear current image state
plt.clf()