
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define the data
data = {'Country': ['United States', 'Germany', 'Japan', 'Canada', 'Australia'], 
        'Healthcare Spending per Capita ($)': [10000, 8000, 9000, 7000, 8000], 
        'Number of Physicians per 1000 Inhabitants': [2.5, 3.0, 3.2, 2.8, 3.5], 
        'Number of Hospital Beds per 1000 Inhabitants': [3.2, 4.5, 4.2, 3.8, 4.0], 
        'Life Expectancy (years)': [78, 82, 84, 80, 80], 
        'Infant Mortality Rate (per 1000 live births)': [5.1, 3.5, 2.8, 4.2, 3.2]}

# Create a pandas dataframe from the data
df = pd.DataFrame(data)

# Set the country column as the index
df = df.set_index('Country')

# Create a figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Create the heatmap chart using seaborn
sns.heatmap(df, cmap='Blues', annot=True, fmt='.1f', cbar=True, ax=ax)

# Set the x and y axis ticks and labels
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set the ticks and tick labels in the center of the cells
ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=True)
ax.set_yticks(np.arange(len(df.index)) + 0.5, minor=True)
ax.tick_params(which='minor', length=0)
ax.tick_params(which='major', pad=15)

# Set the title
ax.set_title('Healthcare Comparisons Across Countries')

# Automatically resize the image and save it
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-130949_10.png', bbox_inches='tight')

# Clear the current image state
plt.clf()