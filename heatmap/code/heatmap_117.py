
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# create dictionary from data
data = {'Category': ['Animal Welfare', 'Education', 'Health', 'Disaster Relief', 'Environmental', 'Poverty Alleviation'],
        'Donation Amount ($)': [100, 200, 300, 400, 500, 600],
        'Donation Percentage (%)': ['10%', '20%', '30%', '40%', '50%', '60%'],
        'Fundraising Expenses (%)': ['20%', '25%', '30%', '35%', '40%', '45%'],
        'Charity Rating (out of 5)': [4.5, 4.2, 4.0, 3.8, 3.5, 3.2],
        'Volunteer Participation (%)': ['50%', '60%', '70%', '80%', '90%', '95%']}

# convert dictionary to pandas dataframe
df = pd.DataFrame.from_dict(data)

# set index to Category column
df = df.set_index('Category')

# convert percentage values to float
df['Donation Percentage (%)'] = df['Donation Percentage (%)'].str.strip('%').astype(float)
df['Fundraising Expenses (%)'] = df['Fundraising Expenses (%)'].str.strip('%').astype(float)
df['Volunteer Participation (%)'] = df['Volunteer Participation (%)'].str.strip('%').astype(float)

# set figure size
plt.figure(figsize=(12, 8))

# plot heatmap using seaborn
ax = sns.heatmap(df, annot=True, cmap='Blues', fmt='.1f', cbar=False)

# set ticks and tick labels for x and y axis
ax.xaxis.tick_top()
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='center')

# add title and labels
plt.title('Nonprofit Organization Performance Metrics', fontsize=16)
plt.xlabel('Metrics')
plt.ylabel('Category')

# automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_21.png', bbox_inches='tight')

# clear current image state
plt.clf()