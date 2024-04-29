
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process data using dict and pandas
data = {'Country': ['USA', 'China', 'India', 'Russia', 'Brazil', 'Canada', 'Australia'], 
        'Carbon Emissions per Capita (tonnes)': [15.2, 8.5, 4.1, 17.8, 5.2, 18.5, 19.2], 
        'Renewable Energy Consumption (%)': [18, 9, 12, 16, 6, 20, 24], 
        'Waste Generation per Capita (kg)': [400, 300, 250, 450, 200, 500, 550], 
        'Air Pollution (ppm)': [43, 78, 102, 35, 65, 38, 40], 
        'Forest Coverage (%)': [23, 18, 15, 22, 13, 24, 25], 
        'Water Usage (m^3)': [5000, 6000, 7000, 4500, 5500, 4000, 3500]}

df = pd.DataFrame(data)
df = df.set_index('Country')

# Plot the data with heatmap chart
fig, ax = plt.subplots(figsize=(12, 8))
heatmap = sns.heatmap(df, annot=True, cmap='BuPu', cbar=False, annot_kws={'size': 12})

# Set ticks and ticklabels for x and y axis
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticklabels(df.index, rotation=45, ha='right', rotation_mode='anchor', size=12)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', size=12)

# Set ticks and ticklabels in the center of rows and columns
ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=False)
ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=False)

# Set title and remove extra space
plt.title('Environmental Indicators by Country', size=16, y=1.07)
plt.tight_layout()

# Automatically resize the image and save
fig.savefig('output/final/heatmap/png/20231228-163105_7.png', bbox_inches='tight')

# Clear the current image state
plt.clf()