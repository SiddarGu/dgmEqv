
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import data as a pandas dataframe
data = pd.DataFrame({'City': ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia'],
                      'Median Home Price ($)': [800000, 650000, 400000, 300000, 350000, 450000],
                      'Median Rent ($)': [2500, 2000, 1500, 1200, 1300, 1700],
                      'Avg. Days on Market': [45, 40, 50, 55, 60, 35],
                      'Avg. Mortgage Rate (%)': [3.5, 3.7, 4, 4.2, 4.5, 3.9],
                      'Homeownership Rate (%)': [55, 45, 60, 65, 70, 50],
                      'Vacancy Rate (%)': [8, 7, 10, 12, 8, 5]})

# set figure size to prevent content from being cut off
plt.figure(figsize=(10, 8))

# create a heatmap using seaborn
import seaborn as sns
ax = sns.heatmap(data.drop('City', axis=1), annot=True, fmt='.0f', cmap='Blues', linewidths=.5, cbar_kws={'shrink': 0.8})

# set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(0, 6) + 0.5)
ax.set_yticks(np.arange(0, 6) + 0.5)
ax.set_xticklabels(data.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(data['City'], rotation=0, ha='right', rotation_mode='anchor')

# set the title of the figure
plt.title('Housing Market Trends in Major Cities')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231226-140552_1.png', bbox_inches='tight')

# clear the current image state
plt.clf()