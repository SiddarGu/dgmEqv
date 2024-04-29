
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary from the data
data = {
    'Country': ['France', 'Spain', 'Italy', 'Greece', 'Portugal'],
    'Hotel Occupancy Rate (%)': [80, 75, 70, 65, 60],
    'Average Daily Rate ($)': [150, 130, 120, 110, 100],
    'Revenue per Available Room ($)': [120, 110, 100, 90, 80],
    'Guest Satisfaction (%)': [85, 80, 75, 70, 65],
    'Hotel Reviews': [500, 450, 400, 350, 300]
}

# Create a dataframe from the dictionary
df = pd.DataFrame(data)

# Set the figure size
fig = plt.figure(figsize=(10, 8))

# Plot the heatmap using seaborn
import seaborn as sns
ax = sns.heatmap(df[['Hotel Occupancy Rate (%)', 'Average Daily Rate ($)', 'Revenue per Available Room ($)', 'Guest Satisfaction (%)']].transpose(), cmap='YlGnBu', annot=True, fmt='g', linewidths=.5, cbar=False)

# Set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(0, len(data['Country'])) + 0.5, minor=False)
ax.set_yticks(np.arange(0, 4) + 0.5, minor=False)
ax.set_xticklabels(data['Country'], minor=False)
ax.set_yticklabels(df[['Hotel Occupancy Rate (%)', 'Average Daily Rate ($)', 'Revenue per Available Room ($)', 'Guest Satisfaction (%)']].columns, minor=False)

# Center the ticks and ticklabels
ax.xaxis.set_ticks_position('top')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='center')

# Add a colorbar
cbar = plt.colorbar(ax.collections[0])
cbar.set_label('Value')

# Set the title
plt.title('Hotel Performance Metrics by Country')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231226-140552_17.png', bbox_inches='tight')

# Clear the current image state
plt.clf()
plt.close()