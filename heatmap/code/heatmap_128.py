
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create data
data = {'Country': ['Spain', 'France', 'United States', 'China', 'Italy', 'Mexico'],
        'Number of Tourist Arrivals (Millions)': [83.5, 90.2, 109.5, 120.5, 80.5, 80.5],
        'Average Hotel Occupancy Rate (%)': [72, 68, 75, 80, 70, 75],
        'Average Daily Hotel Rate (USD)': [150, 200, 250, 300, 180, 120],
        'Revenue per Available Room (USD)': [120, 150, 200, 250, 140, 90],
        'Total Tourism Revenue (USD)': [12.5, 15, 20, 25, 13, 10]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set country as index
df = df.set_index('Country')

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot heatmap using seaborn
sns.heatmap(df, annot=True, cmap='YlGnBu', ax=ax)

# Set x and y ticks and labels
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)

# Set ticks and ticklabels in the center of rows and columns
ax.tick_params(axis='both', which='both', length=0)
# ax.set_xticklabels(df.columns, rotation=45, ha='center', rotation_mode='anchor')
# ax.set_yticklabels(df.index, rotation=0, va='center')

# Set title
ax.set_title('Tourism and Hospitality Metrics')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-131639_34.png', bbox_inches='tight')

# Clear current image state
plt.clf()