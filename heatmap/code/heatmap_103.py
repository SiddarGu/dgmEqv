
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data Processing
data = {'City': ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Median House Price ($)': [500000, 400000, 350000, 300000, 250000],
        'Average Rent ($)': [2500, 2000, 1500, 1200, 1000],
        'Population': [8300000, 4000000, 2700000, 2300000, 1700000],
        'Unemployment Rate (%)': [4.2, 3.5, 4.8, 5.1, 4.6],
        'Crime Rate (per 100,000 residents)': [350, 250, 200, 150, 100],
        'Average Square Footage': [2500, 2000, 1800, 1600, 1400]}

df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot heatmap chart
heatmap = sns.heatmap(df.set_index('City'), annot=True, cmap='coolwarm', ax=ax)

# Set ticks and ticklabels for x and y axis
# ax.set_xticks(np.arange(0.5, 6.5, 1))
# ax.set_yticks(np.arange(0.5, 6.5, 1))
# ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
# ax.set_yticklabels(df.columns[1:], rotation=0, ha='right', rotation_mode='anchor')

# Add colorbar
# cbar = heatmap.collections[0].colorbar
# cbar.set_ticks([-1, 0, 1])
# cbar.set_ticklabels(['Negative', 'No correlation', 'Positive'])

# Set title
plt.title('Housing Market Comparison in Major US Cities')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-130949_13.png', bbox_inches='tight')

# Clear the current image state
plt.clf()