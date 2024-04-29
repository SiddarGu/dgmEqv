




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Product': ['Corn', 'Apples', 'Oranges', 'Tomatoes', 'Potatoes', 'Carrots'],
        'Farm A': [500, 100, 200, 300, 400, 200],
        'Farm B': [400, 150, 250, 350, 450, 300],
        'Farm C': [600, 200, 150, 250, 400, 350],
        'Farm D': [300, 250, 350, 450, 500, 400],
        'Farm E': [700, 300, 400, 500, 600, 450]}

# Convert data to dataframe
df = pd.DataFrame(data)
df.set_index('Product', inplace=True)

# Set figure size
fig = plt.figure(figsize=(10, 8))

# Plot the heatmap using seaborn
import seaborn as sns
ax = sns.heatmap(df, annot=True, cmap='coolwarm')

# Set ticks and ticklabels for x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set tick marks in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=False)
ax.set_yticks(np.arange(len(df.index)) + 0.5, minor=False)

# Add title
plt.title('Crop Production Comparison by Farm')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231226-140552_4.png', bbox_inches='tight')

# Clear the current image state
plt.clf()