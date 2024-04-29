
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create a dictionary to store the data
data = {'Art Form': ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Cubism', 'Surrealism'],
        'Painting': [80, 75, 70, 65, 60, 55],
        'Sculpture': [75, 70, 65, 60, 55, 50],
        'Music': [85, 80, 75, 70, 65, 60],
        'Dance': [70, 60, 50, 40, 30, 20],
        'Film': [60, 50, 40, 30, 20, 10],
        'Photography': [90, 85, 80, 75, 70, 65]}

# Convert the dictionary into a pandas dataframe
df = pd.DataFrame(data)
# Set the 'Art Form' column as the index
df = df.set_index('Art Form')

# Create a figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the heatmap using seaborn
sns.heatmap(df, annot=True, cmap='Blues', cbar=False, linewidths=0.5, square=True)

# Set the ticks and ticklabels for x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set the ticks to be in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)

# Set the x and y axis labels
plt.xlabel('Art Forms')
plt.ylabel('Periods')

# Set the title
plt.title('Popularity of Art Forms in Different Periods')

# Automatically resize the image
plt.tight_layout()

# Save the figure as a png file
plt.savefig('output/final/heatmap/png/20231228-155147_17.png', bbox_inches='tight')

# Clear the current image state
plt.clf()