
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Process the data using dict and pandas
data = {'2021 Destination': ['New York City', 'London', 'Paris', 'Rome', 'Tokyo'],
        'Hotel Occupancy (%)': [75, 70, 80, 65, 85],
        'Airbnb Occupancy (%)': [60, 55, 70, 50, 75],
        'Average Daily Rate ($)': [150, 130, 180, 120, 200],
        'RevPAR ($)': [112.50, 104, 144, 78, 170],
        'Total Revenue ($)': [62500, 57200, 84000, 43680, 110500]}

df = pd.DataFrame(data)

# Set figure size
fig = plt.figure(figsize=(10, 6))

# Use ax instead of plt to plot the chart
ax = fig.add_subplot(111)

# Plot the heatmap chart using imshow()
im = ax.imshow(df.iloc[:, 1:6], cmap='RdBu_r')

# Add colorbar
cbar = fig.colorbar(im)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns[1:6])))
ax.set_xticklabels(df.columns[1:6], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df['2021 Destination'])))
ax.set_yticklabels(df['2021 Destination'], wrap=True)

# Set ticks and ticklabels in the center of rows and columns
ax.tick_params(axis='both', which='both', length=0, pad=10)

# Set title
ax.set_title('Occupancy and Revenue Comparison in Top Tourist Cities')

# Automatically resize the image
plt.tight_layout()

# Save the chart
fig.savefig('output/final/heatmap/png/20231228-124154_2.png', bbox_inches='tight')

# Clear the current image state
plt.clf()