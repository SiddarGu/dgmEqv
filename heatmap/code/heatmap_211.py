
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create a dictionary to store the data
data = {'Category': ['United States', 'United Kingdom', 'France', 'Germany', 'China', 'Japan', 'India', 'Brazil', 'Australia'],
        'Theater': [45, 40, 35, 30, 20, 25, 15, 10, 5],
        'Music': [35, 25, 30, 35, 25, 20, 15, 10, 5],
        'Dance': [20, 30, 40, 45, 30, 35, 25, 20, 15],
        'Film': [40, 35, 25, 20, 40, 35, 30, 25, 20],
        'Visual Art': [50, 45, 55, 60, 65, 70, 65, 60, 55]}

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

# Set the index of the DataFrame to be the 'Category' column
df.set_index('Category', inplace=True)

# Create a figure with a larger figsize
fig = plt.figure(figsize=(10, 8))

# Create a heatmap using seaborn
sns.heatmap(df, annot=True, cmap='Blues', linewidths=0.5, cbar_kws={'label': 'Score'})

# Set the x and y tick labels in the center of rows and columns
# plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns, ha='center', rotation=45, rotation_mode='anchor')
# plt.yticks(np.arange(0.5, len(df.index), 1), df.index, ha='center', rotation=0, rotation_mode='anchor')

# Set the title of the figure
plt.title('Arts and Culture by Country')

# Automatically resize the image
fig.tight_layout()

# Save the figure in the specified path
fig.savefig('output/final/heatmap/png/20231228-134212_87.png', bbox_inches='tight')

# Clear the current image state
plt.clf()