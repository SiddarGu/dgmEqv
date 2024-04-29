
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# data
data = {
    'Category': ['Education', 'Health', 'Environment', 'Poverty', 'Human Rights'],
    'Donations ($)': [100, 150, 80, 200, 120],
    'Volunteers (#)': [20, 30, 15, 40, 25],
    'Fundraising Efficiency (%)': [70, 65, 75, 60, 80],
    'Financial Transparency (%)': [80, 75, 70, 85, 90],
    'Program Impact (%)': [90, 85, 80, 75, 80],
    'Community Engagement (%)': [65, 70, 60, 75, 70]
}

# convert data to dataframe
df = pd.DataFrame(data)

# create figure and ax
fig, ax = plt.subplots(figsize=(10, 6))

# create heatmap chart
sns.heatmap(df.iloc[:,1:], annot=True, fmt='.0f', cmap='Blues', cbar=True, ax=ax)

# set x and y tick labels
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df['Category'], rotation=0, ha='right', rotation_mode='anchor', wrap=True)

# set x and y ticks in the center of rows and columns
ax.set_xticks(np.arange(df.shape[1]-1)+0.5, minor=False)
ax.set_yticks(np.arange(df.shape[0])+0.5, minor=False)

# set title
ax.set_title('Impact and Engagement in Nonprofits')

# resize image and save
fig.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-130949_4.png', bbox_inches='tight')

# clear figure state
plt.clf()