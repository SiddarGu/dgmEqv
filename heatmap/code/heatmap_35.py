
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set data
data = {'Country': ['United States', 'Spain', 'France', 'Italy', 'China'],
        'Number of Tourists (Millions)': [80, 60, 50, 40, 30],
        'Hotel Occupancy Rate (%)': [75, 80, 70, 65, 60],
        'Average Daily Rate (USD)': [150, 120, 180, 200, 100],
        'Revenue per Available Room (USD)': [112.5, 96, 126, 130, 60],
        'Total Revenue (USD)': [9000, 5760, 6300, 5200, 1800]}

# Create dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6))

# Set colormap
cmap = plt.cm.get_cmap('Blues')

# Set labels for x and y axes
x_labels = df['Country']
y_labels = ['Number of Tourists (Millions)', 'Hotel Occupancy Rate (%)', 'Average Daily Rate (USD)', 'Revenue per Available Room (USD)', 'Total Revenue (USD)']

# Set rotation and wrap for x-axis labels
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.xticks(np.arange(len(y_labels)), y_labels, wrap=True)

# Set ticks and ticklabels for y-axis
plt.yticks(np.arange(len(x_labels)), x_labels)

# Plot heatmap
ax = plt.imshow(df.iloc[:, 1:], cmap=cmap, interpolation='nearest')

# Add colorbar
plt.colorbar(ax)

# Add title
plt.title('Tourism and Hospitality Metrics by Country')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-124154_19.png', bbox_inches='tight')

# Clear current image state
plt.clf()