
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the data
data = {'Category': ['Dairy', 'Meat', 'Grains', 'Fruits', 'Vegetables', 'Beverages'],
        'Food Production (in tonnes)': [500, 700, 800, 300, 400, 100],
        'Beverage Production (in tonnes)': [200, 500, 600, 400, 300, 100],
        'Food Exports (in tonnes)': [300, 400, 500, 200, 250, 50],
        'Beverage Exports (in tonnes)': [150, 200, 400, 300, 150, 800],
        'Food Imports (in tonnes)': [100, 300, 300, 100, 150, 150],
        'Beverage Imports (in tonnes)': [50, 100, 200, 200, 100, 600],
        'Food Consumption (in tonnes)': [450, 600, 700, 400, 350, 200],
        'Beverage Consumption (in tonnes)': [250, 400, 500, 300, 200, 1000]}

# Create a dataframe using the data
df = pd.DataFrame(data)

# Set the index of the dataframe to be the Category column
df = df.set_index('Category')

# Plot the heatmap chart using seaborn
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(df, annot=True, fmt='.0f', cmap='Blues', linewidths=0.5, cbar=False)

# Set the ticks and tick labels for the x and y axis
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0)

# Set the labels and title of the chart
plt.xlabel('Production/Exports/Imports/Consumption (in tonnes)')
plt.ylabel('Category')
plt.title('Food and Beverage Production and Consumption by Category')

# Automatically resize the image and save it to the specified path
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_30.png', bbox_inches='tight')

# Clear the current image state
plt.clf()