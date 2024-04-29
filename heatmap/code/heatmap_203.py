

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'League': ['NFL', 'MLB', 'NBA', 'NHL', 'Soccer', 'Cricket'],
        'Ratings': [40, 35, 30, 25, 20, 15],
        'Revenue (Billion)': [10, 15, 20, 25, 30, 35],
        'Attendance (Million)': [5, 10, 15, 20, 25, 30]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(8, 6))

# Plot heatmap
heatmap = ax.imshow(df[['Ratings', 'Revenue (Billion)', 'Attendance (Million)']].transpose(),
                     cmap='Blues',
                     interpolation='nearest',
                     vmin=0,
                     vmax=40)

# Add colorbar
cbar = plt.colorbar(heatmap)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df['League'])))
ax.set_yticks(np.arange(3))
ax.set_xticklabels(df['League'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(['Ratings', 'Revenue (Billion)', 'Attendance (Million)'])

# Make ticks and ticklabels in the center of rows and columns
ax.set_xticks(np.arange(len(df['League'])) + 0.5, minor=True)
ax.set_yticks(np.arange(3) + 0.5, minor=True)
ax.set_xticklabels('')
ax.set_yticklabels('')

# Set ticks and ticklabels for minor axes
ax.set_xticks(np.arange(len(df['League'])) + 0.5, minor=True)
ax.set_yticks(np.arange(3) + 0.5, minor=True)
ax.set_xticklabels(df['League'], minor=True, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(['Ratings', 'Revenue (Billion)', 'Attendance (Million)'], minor=True)

# Turn off grid for minor axes
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)

# Set title
ax.set_title('Major Sports Leagues Performance')

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-134212_76.png', bbox_inches='tight')

# Clear current image state
plt.clf()