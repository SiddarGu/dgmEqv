
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Plant': ['Corn', 'Rice', 'Wheat', 'Soybean', 'Sugar', 'Cotton', 'Coffee', 'Cocoa', 'Tea', 'Palm Oil', 'Fish', 'Poultry', 'Cattle'],
        'Production (kg)': [500, 600, 800, 700, 400, 300, 100, 200, 300, 400, 500, 600, 700],
        'Selling Price ($)': [200, 250, 300, 280, 220, 180, 150, 160, 170, 200, 250, 300, 350]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up to nearest multiple of 10, 100, or 1000
max_total_value = np.ceil(max_total_value / 10) * 10

# Set background grid lines
ax.grid(color='gray', linestyle='dashed')

# Plot area chart
ax.stackplot(df['Plant'], df['Production (kg)'], df['Selling Price ($)'], labels=['Production (kg)', 'Selling Price ($)'], colors=['#1f78b4', '#33a02c'], alpha=0.7)

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, max_total_value)

# Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    # Set x ticks and ticklabels
    xticks = np.arange(0, len(df.index))
    xticklabels = df['Plant'].tolist()
    # Check length of x ticklabels
    if max([len(label) for label in xticklabels]) > 6:
        # Set rotation and wrap for longer labels
        ax.set_xticklabels(xticklabels, rotation=45, rotation_mode="anchor", ha="right", wrap=True)
    else:
        # Set default rotation for shorter labels
        ax.set_xticklabels(xticklabels, rotation=0)
    ax.set_xticks(xticks)

    # Set y ticks and ticklabels
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
    yticklabels = yticks.tolist()
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Agriculture and Food Production by Plant and Selling Price')

# Automatically resize image
fig.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-140159_80.png', bbox_inches='tight')

# Clear image state
plt.clf()