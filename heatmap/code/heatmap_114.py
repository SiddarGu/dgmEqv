


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {'Topic': ['Education', 'Sociology', 'Psychology', 'History'],
        '2018 (%)': [25, 20, 18, 15],
        '2019 (%)': [28, 22, 20, 18],
        '2020 (%)': [30, 24, 22, 20],
        '2021 (%)': [32, 26, 24, 22],
        '2022 (%)': [35, 28, 26, 24]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6))

# Set color map
cmap = plt.cm.get_cmap('Blues')

# Plot heatmap using seaborn
ax = sns.heatmap(df.iloc[:, 1:], annot=True, fmt='g', cmap=cmap, cbar=False)

# Set ticks and tick labels for x-axis
ax.set_xticks(np.arange(len(df.columns) - 1) + 0.5)
ax.set_xticklabels(df.columns[1:])

# Set ticks and tick labels for y-axis
ax.set_yticks(np.arange(len(df['Topic'])) + 0.5)
ax.set_yticklabels(df['Topic'], rotation=45, ha='right', rotation_mode='anchor')

# Set title
plt.title('Percentage of Funding by Field')

# Automatically adjust layout
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-131639_15.png', bbox_inches='tight')

# Clear current image state
plt.clf()