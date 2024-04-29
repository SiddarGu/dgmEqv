

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# import data and create dataframe
data = {'Crop Type': ['Wheat', 'Corn', 'Rice', 'Soybeans', 'Barley', 'Potatoes'], 
        'Yield per Acre (Bushels)': [35, 45, 55, 40, 30, 25], 
        'Total Production (Tonnes)': [150, 200, 250, 180, 130, 100], 
        'Average Price per Tonnes ($)': [200, 175, 150, 225, 180, 300], 
        'Revenue ($)': [4500, 3500, 3000, 4500, 3150, 5000]}
df = pd.DataFrame(data)

# create pivot table to rearrange data
# df_pivot = df.pivot(index='Crop Type', columns='Average Price per Tonnes ($)', values='Revenue ($)')

# set figure size and create heatmap chart
fig, ax = plt.subplots(figsize=(10, 6))
chart = sns.heatmap(df.set_index('Crop Type'), cmap='Blues', annot=True, fmt='g', cbar=True)

# set rotation and alignment for x and y axis tick labels
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(rotation=0, ha='center')

# add title and axis labels
chart.set_title('Crop Production and Revenue by Type')
chart.set_xlabel('Average Price per Tonnes ($)')
chart.set_ylabel('Crop Type')

# resize and save image
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_4.png', bbox_inches='tight')

# clear current image state
plt.clf()