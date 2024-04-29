


# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set data as dictionary
data = {'Platform': ['Facebook', 'Instagram', 'Twitter', 'LinkedIn'],
        'Number of Users (Millions)': [2000, 800, 400, 300],
        'Average Time Spent (Hours)': [5, 4, 3, 2],
        'Engagement Rate (%)': [60, 65, 50, 35],
        'Bounce Rate (%)': [30, 25, 35, 40],
        'Conversion Rate (%)': [20, 25, 15, 10]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)
# Set platform as index
df = df.set_index('Platform')

# Set figure size
plt.figure(figsize=(8, 6))

# Use seaborn heatmap to plot data
ax = sns.heatmap(df, annot=True, cmap='YlGnBu', cbar=False)

# Set x and y tick positions and labels
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)

# Set tick labels in the center of each cell
ax.tick_params(axis='x', which='major', pad=10, labelsize=10, length=0)
ax.tick_params(axis='y', which='major', pad=10, labelsize=10, length=0)

# Set title and remove axis labels
plt.title('Social Media Metrics by Platform')
plt.xlabel('')
plt.ylabel('')

# Automatically resize image
plt.tight_layout()

# Save figure as png
plt.savefig('output/final/heatmap/png/20231228-124154_36.png', bbox_inches='tight')

# Clear current image state
plt.clf()