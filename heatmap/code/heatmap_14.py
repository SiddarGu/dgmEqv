
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process the data
data = {
    'Category': ['Chemical Engineering', 'Mechanical Engineering', 'Electrical Engineering', 'Civil Engineering', 'Biomedical Engineering'],
    '3D Printing (Percentage)': [10, 18, 25, 15, 12],
    'Robotics (Percentage)': [12, 20, 30, 18, 15],
    'Nanotechnology (Percentage)': [5, 25, 28, 20, 20],
    'Biotechnology (Percentage)': [8, 30, 32, 22, 25],
    'Materials Science (Percentage)': [15, 32, 35, 24, 28]
}

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Plot the heatmap chart
fig, ax = plt.subplots(figsize=(12, 8))

# Use seaborn to plot the heatmap
sns.heatmap(df, annot=True, fmt='g', cmap='Blues', ax=ax)

# Set ticks and ticklabels for the x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='center')

# Set the title of the figure
plt.title('Growth of Science and Engineering Fields')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/heatmap/png/20231225-210514_46.png', bbox_inches='tight')

# Clear the current image state
plt.clf()