
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Single Family Homes (Units)': [300, 290, 310, 300, 305],
        'Multi-Family Homes (Units)': [200, 210, 190, 205, 195],
        'Condos (Units)': [100, 120, 110, 115, 105],
        'Townhomes (Units)': [150, 140, 160, 155, 160]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--', linewidth=0.5, alpha=0.5)

# Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Month'])
    ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set max total value and y limits
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)

# Set suitable colors and transparency
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
alpha = 0.7

# Plot the data with area chart
ax.stackplot(df['Month'], df['Single Family Homes (Units)'], df['Multi-Family Homes (Units)'], df['Condos (Units)'], df['Townhomes (Units)'], labels=['Single Family Homes', 'Multi-Family Homes', 'Condos', 'Townhomes'], colors=colors, alpha=alpha)

# Set legend and position
ax.legend(loc='upper right')

# Set title
ax.set_title('Housing Market Trends in 2021')

# Automatically resize the image
fig.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231226-103019_24.png', bbox_inches='tight')

# Clear current image state
plt.clf()