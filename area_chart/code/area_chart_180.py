


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Category': ['History (Publications)', 'Psychology (Publications)', 'Political Science (Publications)', 'Sociology (Publications)', 'Anthropology (Publications)'],
        '2005': [300, 250, 200, 150, 100],
        '2010': [350, 300, 250, 200, 150],
        '2015': [400, 350, 300, 250, 200],
        '2020': [450, 400, 350, 300, 250]}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data as an area chart
ax.stackplot(df['Category'], df['2005'], df['2010'], df['2015'], df['2020'], labels=['2005', '2010', '2015', '2020'])

# Set the x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Number of Publications')

# Set the x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up the max total value to the nearest multiple of 100
max_total_value = np.ceil(max_total_value/100) * 100
ax.set_ylim(0, max_total_value)

# Set the y axis ticks and ticklabels
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set the rotation and ha for the x axis labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Set the background grid lines
plt.grid(color='grey', linestyle='-', linewidth=0.2)

# Set the legend and adjust its position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set the title
ax.set_title('Publication Trends in Social Sciences and Humanities')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-145339_10.png', bbox_inches='tight')

# Clear the current image state
plt.clf()