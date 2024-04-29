
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Team': ['LA Lakers', 'NY Yankees', 'Manchester United', 'Real Madrid', 'Dallas Cowboys', 'FC Barcelona'],
        'Sports Gains (%)': [10, 8, 9, 7, 11, 6],
        'Entertainment Gains (%)': [12, 10, 11, 9, 13, 8],
        'Total Gains (%)': [11, 9, 10, 8, 12, 7],
        'Team Value ($ Million)': [3.5, 4.5, 3.2, 3.0, 3.8, 2.8],
        'Revenue ($ Million)': [440, 400, 450, 380, 480, 360],
        'Profit ($ Million)': [200, 180, 220, 190, 230, 170]}

# Convert data into a pandas DataFrame
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6))

# Create heatmap chart using seaborn
import seaborn as sns
ax = sns.heatmap(df[['Sports Gains (%)', 'Entertainment Gains (%)', 'Total Gains (%)']], cmap='Blues', annot=True, fmt='.1f', linewidths=0.5, cbar_kws={'label': 'Gains (%)'})
ax.set_title('Team Performance and Financials')

# Set ticks and tick labels for x and y axis
ax.set_xticks(np.arange(3) + 0.5)
ax.set_xticklabels(['Sports Gains (%)', 'Entertainment Gains (%)', 'Total Gains (%)'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(6) + 0.5)
ax.set_yticklabels(df['Team'], rotation=0, ha='right', rotation_mode='anchor')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_93.png', bbox_inches='tight')

# Clear current image state
plt.clf() 