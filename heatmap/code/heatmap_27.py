
# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary with the given data
data = {'Category': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Population (million)': [365, 430, 741, 4621, 1281, 43],
        'Life Expectancy (years)': [78, 73, 81, 74, 66, 82],
        'Health Expenditure (% of GDP)': [16, 12, 14, 10, 8, 15],
        'Infant Mortality Rate (per 1,000 live births)': [5, 10, 3, 20, 25, 3],
        'Physicians per 1,000 People': [2.5, 1.8, 3.5, 1.5, 0.8, 4.5],
        'Hospital Beds per 1,000 People': [2.3, 1.5, 3.2, 1.2, 0.7, 4.1]}

# Convert the dictionary into a pandas dataframe
df = pd.DataFrame(data)

# Set the category column as the index
df.set_index('Category', inplace=True)

# Create a figure and axes object
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the heatmap using imshow()
heatmap = ax.imshow(df, cmap='Blues')

# Add the colorbar
cbar = plt.colorbar(heatmap, ax=ax)

# Set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_xticklabels(df.columns)
ax.set_yticks(np.arange(len(df.index)))
ax.set_yticklabels(df.index)

# Rotate the x-tick labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Set the tick labels in the center of the cells
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xticks(np.arange(df.shape[1]+1)-.5, minor=True)
ax.set_yticks(np.arange(df.shape[0]+1)-.5, minor=True)
ax.grid(which='minor', color='w', linestyle='-', linewidth=3)

# Add the value of each cell
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='w', fontsize=12)

# Set the title
ax.set_title('Healthcare Indicators by Region', fontsize=16)

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231226-140552_7.png', bbox_inches='tight')

# Clear the current image state
plt.clf()