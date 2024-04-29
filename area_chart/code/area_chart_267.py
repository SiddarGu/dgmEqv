
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Field': ['Aerospace', 'Materials Science', 'Energy', 'Environmental Science', 'Robotics', 'Nanotechnology', 'Biomedical Engineering', 'Industrial Engineering', 'Civil Engineering', 'Mechanical Engineering', 'Chemical Engineering', 'Electrical Engineering', 'Computer Engineering'], 
        'Physics': [20, 10, 15, 20, 25, 30, 25, 15, 20, 25, 15, 20, 25], 
        'Chemistry': [25, 30, 25, 20, 20, 10, 15, 20, 25, 15, 20, 25, 15], 
        'Biology': [25, 20, 25, 25, 15, 15, 20, 25, 15, 20, 25, 15, 20], 
        'Computer Science': [15, 25, 10, 10, 20, 25, 25, 15, 20, 25, 15, 20, 25], 
        'Engineering': [15, 15, 25, 25, 20, 20, 15, 25, 20, 15, 25, 20, 15]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12,8))

# Plot the data with the type of area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=['#4c72b0', '#55a868', '#c44e52', '#8172b2', '#ccb974'], alpha=0.8)

# Set background grid lines
ax.grid(axis='y', color='lightgrey', linestyle='--')

# Set x and y axis ticks and ticklabels
if np.random.rand() > 0.3:
    ax.set_xticks(np.arange(len(df)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
if np.random.rand() > 0.3:
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value % 1000 == 0:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    elif max_total_value % 100 == 0:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set title and legend
ax.set_title('Science and Engineering Distribution by Field')
ax.legend(loc='upper left')

# Automatically resize the image
plt.tight_layout()

# Save the chart as png
plt.savefig('output/final/area_chart/png/20231228-155112_28.png', bbox_inches='tight')

# Clear the current image state
plt.clf()