

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dictionary for organization data
org_data = {
    'Organization': ['Red Cross', 'UNICEF', 'Save the Children', 'World Vision'],
    'Revenue ($)': [100, 150, 80, 120],
    'Expenses ($)': [90, 120, 70, 100],
    'Assets ($)': [500, 600, 400, 550],
    'Program Expenses (%)': [75, 80, 70, 80],
    'Fundraising Expenses (%)': [15, 10, 20, 15],
    'Administrative Expenses (%)': [10, 10, 10, 5]
}

# Convert dictionary to pandas dataframe
org_df = pd.DataFrame(org_data)

# Set index as organization names
org_df.set_index('Organization', inplace=True)

# Calculate total expenses and add as new column
org_df['Total Expenses ($)'] = org_df['Expenses ($)'].sum()

# Calculate percentage of expenses for each category and add as new column
org_df['Program Expenses (%)'] = round((org_df['Expenses ($)'] / org_df['Total Expenses ($)']) * 100, 2)
org_df['Fundraising Expenses (%)'] = round((org_df['Fundraising Expenses (%)'] / org_df['Total Expenses ($)']) * 100, 2)
org_df['Administrative Expenses (%)'] = round((org_df['Administrative Expenses (%)'] / org_df['Total Expenses ($)']) * 100, 2)

# Create heatmap chart using seaborn
plt.figure(figsize=(10,8))
ax = sns.heatmap(org_df, annot=True, linewidths=.5, cmap='YlGnBu', cbar=False, fmt='g')

# Set ticks and ticklabels for x and y axis
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Set title and axis labels
plt.title('Financial Overview of Nonprofit Organizations')
plt.xlabel('Category')
plt.ylabel('Organization')

# Automatically resize image and save as png
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_14.png', bbox_inches='tight')

# Clear current image state
plt.clf()