
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data
data = {
    "Policy Area": ["Education", "Healthcare", "Transportation", "Taxation", "Environment", "Defense"],
    "Spending (% of GDP)": [25, 20, 15, 10, 5, 2],
    "United States": [7.5, 8.8, 5.0, 3.5, 1.2, 0.5],
    "China": [5.0, 7.5, 6.5, 4.0, 2.0, 1.0],
    "Germany": [4.0, 6.0, 4.5, 3.0, 1.5, 0.8]
}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set Policy Area as index
df.set_index('Policy Area', inplace=True)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 7))

# Plot heatmap
heatmap = ax.imshow(df, cmap='YlGnBu')

# Add colorbar
plt.colorbar(heatmap)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# Set ticks in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns))+0.5, minor=True)
ax.set_yticks(np.arange(len(df.index))+0.5, minor=True)
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

# Rotate x-axis labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Set title
plt.title('Government Spending as a Percentage of GDP')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-124154_80.png', bbox_inches='tight')

# Clear current image state
plt.clf()