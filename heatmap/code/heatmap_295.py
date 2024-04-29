


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# create a dictionary with the given data
data = {'City': ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia'],
        'Median Home Price ($)': [500000, 450000, 300000, 250000, 200000, 350000],
        'Average Rent ($)': [2500, 2200, 1800, 1500, 1200, 1600],
        'Property Tax (%)': [30, 25, 20, 15, 10, 25],
        'Vacancy Rate (%)': [6, 5, 4, 3, 2, 4],
        'Homeownership Rate (%)': [6, 5, 4, 3, 2, 4],
        'Mortgage Rate (%)': [3.5, 3, 2.5, 2, 1.5, 2.75]}

# convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# set the index to be the City column
df.set_index('City', inplace=True)

# create subplots with a figsize of (10,6)
fig, ax = plt.subplots(figsize=(10,6))

# plot the heatmap using seaborn
sns.heatmap(df, cmap='Blues', annot=True, fmt='.1f', linewidths=0.5, ax=ax)

# set the x and y tick labels to be in the center of each row/column
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)

# set the title of the figure
plt.title('Real Estate and Housing Market Data')

# automatically resize the image and save it to the specified path
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_30.png', bbox_inches='tight')

# clear the current image state
plt.clf()