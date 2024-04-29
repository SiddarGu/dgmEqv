
# python code
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the data
data = {
    'Year': [2009, 2010, 2011, 2012, 2013],
    'GDP (in billions)': [14.8, 15.0, 15.5, 16.0, 16.5],
    'Unemployment Rate (%)': [8.0, 7.6, 7.2, 6.8, 6.4],
    'Inflation Rate (%)': [2.2, 2.5, 2.8, 3.0, 3.2],
    'Interest Rate (%)': [3.5, 3.2, 3.0, 2.8, 2.5],
    'Stock Market Index': [11, 13, 15, 17, 19],
    'Consumer Spending ($ in billions)': [8.5, 8.7, 9.0, 9.2, 9.5]
}

# Convert data to pandas dataframe
df = pd.DataFrame(data)
df = df.set_index('Year')

# Create a heatmap chart using seaborn
import seaborn as sns
plt.figure(figsize=(10,8))
ax = sns.heatmap(df, cmap='coolwarm', annot=True, linewidths=0.5, vmax=20, vmin=0, fmt='.1f', cbar=False)

# Set x and y ticks and ticklabels at the center of rows and columns
ax.set_xticks(np.arange(len(df.columns))+0.5, minor=False)
ax.set_yticks(np.arange(len(df.index))+0.5, minor=False)
ax.set_xticklabels(df.columns.values, minor=False, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index.values, minor=False, rotation=0, ha='right', rotation_mode='anchor')

# Set title and labels
plt.title('Economic Indicators in the Past Five Years')
plt.xlabel('Indicators')
plt.ylabel('Year')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the chart as a png file
plt.savefig('output/final/heatmap/png/20231226-140552_16.png', bbox_inches='tight')

# Clear the current image state
plt.clf()