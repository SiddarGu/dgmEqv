
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define data
data = {'Team': ['Manchester United', 'Real Madrid', 'FC Barcelona', 'Bayern Munich', 'Juventus', 'Paris Saint-Germain'],
        'Win Rate (%)': [75, 70, 80, 85, 80, 75],
        'Goal Difference': [25, 20, 30, 35, 30, 25],
        'Total Points': [85, 80, 90, 95, 90, 85],
        'Offensive Rating': [8.5, 9.0, 9.5, 9.2, 9.3, 9.1],
        'Defensive Rating': [7.2, 6.8, 6.9, 6.5, 7.0, 7.5]}

# Convert data into pandas dataframe
df = pd.DataFrame(data)

# Set the index as Team
df.set_index('Team', inplace=True)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot heatmap using seaborn
sns.heatmap(df, cmap='BuPu', annot=True, fmt='.1f', cbar=False)

# Set x and y ticks at the center of each cell
ax.set_xticks(np.arange(0.5, len(df.columns)+0.5, 1))
ax.set_yticks(np.arange(0.5, len(df.index)+0.5, 1))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, va='center')

# Set title and labels
plt.title('Team Performance in Top Football Leagues')
plt.xlabel('Metrics')
plt.ylabel('Teams')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig('output/final/heatmap/png/20231228-124154_40.png', bbox_inches='tight')

# Clear current image state
plt.clf()