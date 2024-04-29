
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
data = {'Country': ['USA', 'China', 'Japan', 'Germany', 'France', 'UK', 'India', 'Brazil', 'Canada', 'Australia'],
        'GDP (Billion USD)': [20.5, 14.3, 5.1, 4.4, 3.9, 3.0, 2.9, 2.2, 1.8, 1.5],
        'Population (Millions)': [330, 1400, 126, 83, 67, 67, 1400, 212, 38, 25],
        'Education Index': [8.2, 7.5, 8.7, 8.6, 8.3, 8.2, 6.5, 7.2, 8.5, 8.9],
        'Healthcare Index': [9.5, 8.5, 9.2, 9.0, 9.1, 9.0, 7.5, 8.0, 9.2, 9.5],
        'Income Inequality Index': [6.5, 7.2, 7.8, 6.9, 7.1, 7.5, 8.5, 8.0, 7.0, 6.8],
        'Government Effectiveness Index': [8.7, 6.5, 9.0, 8.5, 8.0, 7.5, 6.0, 7.0, 8.8, 9.2]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set country as index
df = df.set_index('Country')

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot heatmap
heatmap = sns.heatmap(df, annot=True, cmap='Blues', linewidths=1, linecolor='white', cbar_kws={'label': 'Value'})

# Set ticks and ticklabels for x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set ticks to be in the center of each cell
ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=False)
ax.set_yticks(np.arange(len(df.index)) + 0.5, minor=False)

# Add title
ax.set_title('Government and Public Policy Metrics by Country', fontsize=16)

# Automatically resize image and save
fig.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-124154_6.png', bbox_inches='tight')

# Clear current image state
plt.clf()