
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Category':['Twitter', 'Facebook', 'Instagram', 'LinkedIn', 'YouTube'],
        'Number of Posts':[500, 750, 1000, 250, 500],
        'Number of Users':[350, 500, 600, 200, 350],
        'Number of Likes':[1500, 2000, 2500, 1000, 1500],
        'Number of Comments':[750, 1000, 1250, 500, 750],
        'Number of Shares':[400, 600, 800, 300, 400]}

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Create heatmap chart
fig, ax = plt.subplots(figsize=(12,8))

# Set ticks and tick labels for x and y axis
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Category'])))
ax.set_xticklabels(df.columns[1:])
ax.set_yticklabels(df['Category'])

# Center x and y axis ticks and labels
ax.tick_params(axis='x', which='major', pad=10)
ax.tick_params(axis='y', which='major', pad=10)

# Set x and y axis label rotation
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Create heatmap using imshow()
im = ax.imshow(df.iloc[:,1:], cmap='viridis')

# Add colorbar with 40% probability
if np.random.randint(0, 10) > 6:
    plt.colorbar(im)

# Show values of each cell with 60% probability
if np.random.randint(0, 10) > 4:
    for i in range(len(df['Category'])):
        for j in range(len(df.columns[1:])):
            text = ax.text(j, i, df.iloc[i,j+1], ha="center", va="center", color="w")

# Set title
ax.set_title('Social Media Engagement Metrics')

# Automatically resize image
fig.tight_layout()

# Save figure with relative path
plt.savefig('output/final/heatmap/png/20231228-155147_48.png', bbox_inches='tight')

# Clear current image state
plt.clf()