
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Art Form':['Ancient', 'Medieval', 'Renaissance', 'Baroque', 'Rococo', 'Classical', 'Romantic', 'Modern', 'Contemporary'],
        'Painting':[40, 35, 30, 25, 20, 15, 10, 5, 5],
        'Drawing':[25, 20, 25, 30, 35, 40, 35, 30, 25],
        'Sculpture':[10, 15, 15, 10, 5, 5, 5, 5, 5],
        'Photography':[10, 10, 15, 20, 30, 35, 40, 45, 50],
        'Theater':[5, 5, 5, 5, 5, 5, 5, 5, 5],
        'Dance':[5, 5, 5, 5, 5, 5, 5, 5, 5],
        'Performance':[5, 5, 5, 5, 5, 5, 5, 5, 5],
        'Music':[5, 5, 5, 5, 5, 5, 5, 5, 5],
        'Installation':[5, 5, 5, 5, 5, 5, 5, 5, 5]}

# Convert data into a pandas dataframe
df = pd.DataFrame(data)

# Set figure size and create subplot
fig, ax = plt.subplots(figsize=(12, 8))

# Generate heatmap
heatmap = ax.imshow(df.iloc[:, 1:].values, cmap='YlOrRd')

# Set ticks and tick labels
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Art Form'])))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Art Form'])

# Loop through data to show values in each cell
for i in range(len(df['Art Form'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j+1], ha='center', va='center', color='k')

# Add colorbar
cbar = plt.colorbar(heatmap)

# Set title
plt.title('Popularity of Art Forms throughout History')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/heatmap/png_train/heatmap_182.png', bbox_inches='tight')

# Clear current image state
plt.clf()