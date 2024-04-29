
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import data
data = {'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Per Capita Meat Consumption (kg)': [120, 90, 100, 60, 40, 80],
        'Per Capita Dairy Consumption (kg)': [80, 60, 70, 50, 30, 60],
        'Per Capita Fruit Consumption (kg)': [60, 50, 70, 80, 40, 70],
        'Per Capita Vegetable Consumption (kg)': [100, 80, 90, 120, 60, 110],
        'Per Capita Grain Consumption (kg)': [150, 120, 130, 180, 90, 160],
        'Per Capita Sugar Consumption (kg)': [40, 30, 50, 60, 20, 40]}

# Convert to dataframe
df = pd.DataFrame(data)

# Set index to Region
df.set_index('Region', inplace=True)

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Create heatmap
heatmap = ax.imshow(df, cmap='YlGnBu')

# Set ticks and tick labels for x-axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')

# Set ticks and tick labels for y-axis
ax.set_yticks(np.arange(len(df.index)))
ax.set_yticklabels(df.index, rotation=0)

# Center ticks
ax.set_xticks(np.arange(len(df.columns)) - 0.5, minor=True)
ax.set_yticks(np.arange(len(df.index)) - 0.5, minor=True)

# Add colorbar
cbar = plt.colorbar(heatmap, ax=ax)

# Set colorbar label
cbar.set_label('Consumption (kg)')

# Set title
ax.set_title('Per Capita Food Consumption by Region')

# Add values to cells
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='w')

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-163105_27.png', bbox_inches='tight')

# Clear figure
plt.clf()