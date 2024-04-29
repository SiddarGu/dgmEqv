


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Process the data using dict and pandas
raw_data = {
    'City': ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Median Home Price ($)': [1300000, 1100000, 900000, 700000, 500000],
    'Average Rent ($)': [2250000, 2000000, 1800000, 1500000, 1200000],
    'Vacancy Rate (%)': [3, 2, 3, 5, 4],
    'Population Density (per sq mile)': [4500, 3800, 3000, 2500, 2000],
    'Median Household Income ($)': [80000, 75000, 60000, 55000, 50000]
}
df = pd.DataFrame(raw_data, columns=['City', 'Median Home Price ($)', 'Average Rent ($)', 'Vacancy Rate (%)', 'Population Density (per sq mile)', 'Median Household Income ($)'])
df.set_index('City', inplace=True)

# Set figure size and plot the heatmap chart
plt.figure(figsize=(10, 7))
ax = sns.heatmap(df, annot=True, fmt='.0f', cmap='Blues', cbar=True, cbar_kws={'label': 'Amount in Dollars'})

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor', wrap=True)
ax.invert_yaxis()

# Set title and labels
plt.title('Housing and Demographic Metrics')
plt.xlabel('Metrics')
plt.ylabel('City')

# Automatically resize the image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_26.png', bbox_inches='tight')

# Clear the current image state
plt.clf()