
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'France', 'United Kingdom'],
    'Healthcare Spending (Billions)': [700, 600, 500, 400, 300, 350],
    'Education Spending (Billions)': [500, 400, 300, 200, 250, 300],
    'Infrastructure Spending (Billions)': [400, 300, 200, 100, 150, 200],
    'Defense Spending (Billions)': [600, 500, 400, 300, 200, 150],
    'Public Housing Spending (Billions)': [200, 300, 100, 150, 100, 100],
    'Social Security Spending (Billions)': [300, 200, 100, 150, 100, 150]
}

# Convert data to pandas dataframe
df = pd.DataFrame(data)
df.set_index('Country', inplace=True)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10,8))

# Create heat map using imshow()
im = ax.imshow(df, cmap='YlGnBu')

# Add colorbar
cbar = ax.figure.colorbar(im, ax=ax)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# Rotate x tick labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Center ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)+1)-0.5, minor=True)
ax.set_yticks(np.arange(len(df.index)+1)-0.5, minor=True)
ax.tick_params(which='minor', length=0)
ax.grid(which='minor')

# Add title and set font size
ax.set_title('Government Spending by Country', fontsize=18)

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-131639_94.png', bbox_inches='tight')

# Clear current image state
plt.clf()