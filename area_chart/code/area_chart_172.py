
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Category': ['Entertainment', 'News', 'Lifestyle', 'Sports', 'Travel', 'Food', 'Fashion', 'Politics', 'Technology', 'Beauty', 'Music', 'Education', 'Health'], 'Facebook (Users)': [200, 150, 100, 200, 150, 180, 130, 250, 120, 180, 150, 120, 100], 'Twitter (Users)': [180, 180, 200, 180, 200, 150, 100, 130, 100, 200, 180, 150, 200], 'Instagram (Users)': [150, 200, 250, 150, 100, 100, 150, 100, 200, 150, 130, 200, 250], 'LinkedIn (Users)': [130, 150, 180, 130, 250, 200, 180, 200, 180, 100, 200, 170, 150], 'YouTube (Users)': [100, 250, 150, 100, 120, 170, 200, 150, 150, 250, 100, 130, 180]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data with the type of area chart
ax.stackplot(df['Category'], df['Facebook (Users)'], df['Twitter (Users)'], df['Instagram (Users)'], df['LinkedIn (Users)'], df['YouTube (Users)'], labels=['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'YouTube'])

# Set x and y axis ticks and ticklabels
if np.random.random() < 0.7:
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
else:
    ax.set_xticks([])
    ax.set_yticks([])

# Set suitable colors and transparency
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b2', '#ccb974']
for patch, color in zip(ax.patches, colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

# Set background grid lines
ax.grid(axis='y', alpha=0.5)

# Set legend's position and labels
ax.legend(loc='upper left')
ax.set_ylabel('Number of Users')

# Set title
ax.set_title('Social Media Usage by Category')

# Automatically resize the image
fig.tight_layout()

# Save the image
fig.savefig('output/final/area_chart/png/20231228-140159_92.png', bbox_inches='tight')

# Clear the current image state
plt.clf()