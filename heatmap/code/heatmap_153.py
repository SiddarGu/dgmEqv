


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {'Category': ['Education', 'Healthcare', 'Environment', 'Economy'],
        'Policy A (%)': [35, 25, 15, 20],
        'Policy B (%)': [28, 30, 20, 22],
        'Policy C (%)': [40, 35, 25, 25],
        'Policy D (%)': [45, 40, 30, 28],
        'Policy E (%)': [50, 45, 35, 30],
        'Policy F (%)': [55, 50, 40, 35]}
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Set seaborn style
sns.set()

# Plot heatmap using seaborn
ax = sns.heatmap(df.iloc[:, 1:], annot=True, cmap='YlGnBu')

# Set x and y tick labels
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Category'], rotation=0)

# Add title
plt.title('Government Policy Effectiveness')

# Automatically resize image
plt.tight_layout()

# Save figure as png
plt.savefig('output/final/heatmap/png/20231228-131639_74.png', bbox_inches='tight')

# Clear image state
plt.clf()