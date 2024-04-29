
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the data
data = {
    'Category': ['Theaters', 'Museums', 'Concert Halls', 'Art Galleries', 'Cinemas'],
    'United States': [1500, 2000, 1000, 3000, 5000],
    'Russia': [1000, 1500, 800, 2000, 4000],
    'United Kingdom': [1200, 1800, 900, 2500, 4500],
    'France': [1300, 1700, 1100, 2700, 4800],
    'Germany': [1100, 1600, 950, 2200, 4200],
    'Japan': [1400, 1900, 1200, 2800, 5200]
}

# Convert the data into a dataframe
df = pd.DataFrame(data, columns=['Category', 'United States', 'Russia', 'United Kingdom', 'France', 'Germany', 'Japan'])

# Set the figure size
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the heatmap chart
heatmap = ax.imshow(df.iloc[:, 1:], cmap='Blues')

# Add the colorbar
cbar = plt.colorbar(heatmap)

# Set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Category'])))
ax.set_xticklabels(df.columns[1:])
ax.set_yticklabels(df['Category'])

# Rotate the x-axis labels and set them to the right
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Set the ticks and ticklabels to be in the center of each cell
ax.set_xticks(np.arange(df.shape[1]-1)+0.5, minor=True)
ax.set_yticks(np.arange(df.shape[0])+0.5, minor=True)
ax.tick_params(which='minor', bottom=False, left=False)

# Loop through the data and add the values to each cell of the heatmap
for i in range(len(df['Category'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j+1], ha='center', va='center', color='black')

# Set the title of the figure
ax.set_title('Cultural Institutions by Country')

# Automatically resize the image and save it
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_7.png', bbox_inches='tight')

# Clear the current image state
plt.clf()