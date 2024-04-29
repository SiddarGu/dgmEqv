
# Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Category': ['Aerospace', 'Energy', 'Nanotechnology', 'Robotics', 'Materials Science', 'Transportation', 'Agriculture', 'Medicine', 'Artificial Intelligence', 'Space Exploration', 'Oceanography', 'Climate Change', 'Biotechnology', 'Sustainable Energy'], 
        'Physics (Projects)': [20, 15, 10, 25, 15, 10, 20, 20, 25, 10, 10, 20, 10, 15], 
        'Chemistry (Projects)': [15, 20, 10, 15, 20, 15, 10, 25, 10, 20, 10, 5, 10, 10], 
        'Biology (Projects)': [10, 10, 5, 20, 25, 20, 10, 15, 20, 10, 25, 15, 20, 20], 
        'Environmental Science (Projects)': [5, 10, 15, 10, 5, 10, 15, 5, 10, 15, 10, 20, 15, 15], 
        'Engineering (Projects)': [20, 25, 30, 25, 15, 20, 25, 20, 25, 25, 20, 25, 25, 20]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 100:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
    ylim = (0, max_total_value)
elif max_total_value <= 1000:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
    ylim = (0, max_total_value + (10 - max_total_value % 10))
else:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
    ylim = (0, max_total_value + (100 - max_total_value % 100))

# Plot the data with area chart
ax.stackplot(df['Category'], df.iloc[:, 1:].transpose(), labels=df.columns[1:])
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
# Set colors and transparency
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i in range(len(ax.collections)):
    ax.collections[i].set_facecolor(colors[i])
    ax.collections[i].set_alpha(0.8)

# Set background grid lines
ax.grid(color='#D3D3D3', linestyle='-', linewidth=0.5, alpha=0.5)

# Set x and y axis labels
ax.set_xlabel('Field of Study')
ax.set_ylabel('Number of Projects')

# Set title
ax.set_title('Scientific Projects by Field of Study')

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

# Automatically resize the image
fig.tight_layout()

# Save the chart
plt.savefig('output/final/area_chart/png/20231228-145339_28.png', bbox_inches='tight')

# Clear the current image state
plt.clf()