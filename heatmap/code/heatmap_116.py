
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define the data as a dictionary
data = {
    'Team': ['Lakers', 'Celtics', 'Warriors', 'Heat'],
    'Wins (%)': [65, 60, 70, 55],
    'Losses (%)': [20, 25, 15, 30],
    'Ties (%)': [15, 15, 15, 15],
    'Points Scored (%)': [75, 70, 80, 65],
    'Points Allowed (%)': [70, 65, 75, 60]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Set the figure size
fig, ax = plt.subplots(figsize=(8, 6))

# Create the heatmap using sns.heatmap()
sns.heatmap(df.iloc[:,1:], annot=True, cmap='RdYlGn', linewidths=0.5, cbar=False)

# Set the x and y ticks and labels
ax.set_yticks(np.arange(len(df.index))+0.5, minor=False)
ax.set_xticks(np.arange(len(df.columns)-1)+0.5, minor=False)
ax.set_xticklabels(df.columns[1:], minor=False, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Team'], minor=False)

# Add a colorbar
cbar = ax.figure.colorbar(ax.collections[0])

# Set the title
plt.title('Team Performance in NBA Regular Season')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_2.png', bbox_inches='tight')

# Clear the current image state
plt.clf()