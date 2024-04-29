
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define the data as a dictionary
data = {'Research Area': ['Energy Storage', 'Nanomaterials', 'Biomaterials', 'Robotics', 'Structural Engineering', 'Power Systems'],
        'Materials Science': [35, 20, 15, 10, 5, 15],
        'Chemical Engineering': [25, 20, 25, 10, 5, 15],
        'Mechanical Engineering': [20, 20, 15, 30, 15, 20],
        'Biomedical Engineering': [10, 20, 15, 35, 25, 10],
        'Civil Engineering': [5, 15, 10, 5, 25, 15],
        'Electrical Engineering': [5, 5, 10, 10, 25, 25]}

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data).set_index('Research Area')

# Create a figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the heatmap using sns.heatmap()
sns.heatmap(df, cmap='Blues', annot=True, fmt='g', cbar=False)

# Set the ticks and ticklabels for the x and y axis
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set the title of the figure
plt.title('Percentage of Research in Different Engineering Disciplines')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure as a png file
plt.savefig('output/final/heatmap/png/20231228-124154_49.png', bbox_inches='tight')

# Clear the current image state
plt.clf()

# Check the generated code to make sure it doesn't report errors, do not include undefined functions, and save path is relative path which is completely the same as output/final/heatmap/png.
