
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data processing
df = pd.DataFrame({
    'Category': ['Defense', 'Health', 'Education', 'Social Security', 'Infrastructure', 'Agriculture'],
    'Government Spending (in billions)': [700, 500, 400, 300, 200, 100],
    'Public Services Employees (in millions)': [3.2, 2.5, 2.0, 1.8, 1.5, 1.0],
    'Public Sector Salaries (in thousands)': [60, 55, 50, 45, 40, 35],
    'Tax Revenue (in billions)': [500, 400, 300, 250, 200, 150],
    'Government Debt (in trillions)': [2, 1.5, 1, 0.8, 0.5, 0.3],
    'Public Education Budget (in billions)': [300, 200, 150, 100, 75, 50]
})

# Set figure size
plt.rcParams['figure.figsize'] = (10, 6)

# Plot heatmap
ax = sns.heatmap(df.iloc[:, 1:], cmap='YlGnBu', annot=True, fmt=".0f", linewidths=.5)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)-1) + 0.5)
ax.set_yticks(np.arange(len(df)) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Category'], rotation=0, ha='right', rotation_mode='anchor')

# Set tick position in the center
ax.set_xticks(np.arange(len(df.columns)-1) + 0.5, minor=True)
ax.set_yticks(np.arange(len(df)) + 0.5, minor=True)
ax.set_xticklabels(df.columns[1:], minor=True, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Category'], minor=True, rotation=0, ha='right', rotation_mode='anchor')

# Add colorbar
cbar = ax.collections[0].colorbar
cbar.set_ticks([0.25, 0.75])
cbar.set_ticklabels(['Low', 'High'])

# Set title
plt.title("Government Budget Allocation and Impact")

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig("output/final/heatmap/png/20231228-155147_56.png", bbox_inches='tight')

# Clear current image state
plt.clf()