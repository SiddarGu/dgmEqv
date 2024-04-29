
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define data
data = {'Sport': ['Football', 'Basketball', 'Soccer', 'Baseball', 'Hockey'],
        'Rating': [9.5, 8.7, 8.0, 7.8, 7.2],
        'Viewership (%)': [65, 55, 60, 45, 40],
        'Ticket Sales (Millions)': [500, 400, 300, 200, 150],
        'Merchandise Sales (Millions)': [100, 80, 70, 60, 50],
        'Social Media Followers (Millions)': [25, 20, 15, 10, 8]}

# Create dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6))

# Create heatmap
ax = plt.axes()
heatmap = ax.pcolor(df[['Rating', 'Viewership (%)', 'Ticket Sales (Millions)', 'Merchandise Sales (Millions)', 'Social Media Followers (Millions)']], cmap='YlOrBr')

# Set ticks and ticklabels
ax.set_xticks(np.arange(0.5, len(df.columns[1:]), 1))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_yticklabels(df['Sport'], wrap=True)

# Set ticks to be in the center of each cell
# ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=False)
# ax.set_yticks(np.arange(len(df.index)) + 0.5, minor=False)

# Add colorbar
cb = plt.colorbar(heatmap)

# Set title
plt.title('Sports and Entertainment Industry Metrics')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-134212_78.png', bbox_inches='tight')

# Clear figure
plt.clf()