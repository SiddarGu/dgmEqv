
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# process data using dict and pandas
data = {'City': ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Average Home Price ($)': [1200000, 900000, 500000, 400000, 300000],
        'Average Rent ($)': [2500, 2000, 1500, 1200, 1000],
        'Average Mortgage ($)': [3500, 2800, 2000, 1800, 1500],
        'Vacancy Rate (%)': [5, 7, 8, 9, 10],
        'Housing Inventory (Units)': [10000, 8000, 6000, 5000, 4000]}

df = pd.DataFrame(data)
df.set_index('City', inplace=True)

# create heatmap chart
fig, ax = plt.subplots(figsize=(10, 8))

# use sns.heatmap() with colorbar
sns.heatmap(df, annot=True, fmt='g', cmap='Blues', cbar=True, ax=ax)

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(df.shape[1]) + 0.5)
ax.set_yticks(np.arange(df.shape[0]) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# add title
plt.title('Real Estate Market Trends in Major US Cities')

# resize image and save with tight_layout()
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_3.png', bbox_inches='tight')

# clear current image state
plt.clf()