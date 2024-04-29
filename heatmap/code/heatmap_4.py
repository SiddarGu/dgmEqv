

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Process the data
data = {'Country': ['France', 'Spain', 'United States', 'China', 'Italy'], 'Hotel Occupancy (%)': [75, 68, 70, 65, 72], 'Average Daily Rate (USD)': [150, 130, 180, 120, 140], 'Revenue per Available Room (USD)': [112.5, 88.4, 126, 78, 100.8], 'Tourist Arrivals (Millions)': [85, 83, 100, 90, 80], 'Tourism Contribution to GDP (%)': [10, 8, 12, 10, 10], 'International Tourism Receipts (USD)': [120, 100, 150, 85, 110]}
df = pd.DataFrame(data)

# Plot the heatmap chart
fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(df.iloc[:,1:].values, cmap='YlGn')

# Set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Country'])))
ax.set_xticklabels(df.columns[1:])
ax.set_yticklabels(df['Country'])

# Rotate the x-axis tick labels by 45 degrees and align them to the right
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Center the ticks and ticklabels
ax.tick_params(axis='both', which='both', length=0.5, pad=10)
ax.tick_params(axis='x', which='major', pad=20)
ax.tick_params(axis='y', which='major', pad=10)

# Create a colorbar and add the label
cbar = ax.figure.colorbar(im)
cbar.ax.set_ylabel('Values', rotation=-90, va="bottom", labelpad=20)

# Show the value of each cell
for i in range(len(df['Country'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j+1], ha="center", va="center", color="black")

# Set the title
ax.set_title('Tourism Metrics by Country')

# Automatically resize the image and save it
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231225-210514_19.png', bbox_inches='tight')

# Clear the current image state
plt.clf()
plt.close()