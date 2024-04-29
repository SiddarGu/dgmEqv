


# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Set data
data = {'Product Type': ['Beer', 'Soft Drinks', 'Fruit Juice', 'Snacks', 'Dairy Products', 'Alcoholic Beverages'],
        'Asia': [35, 30, 25, 20, 15, 10],
        'Europe': [30, 25, 20, 15, 10, 5],
        'North America': [25, 20, 15, 10, 5, 0],
        'South America': [20, 15, 10, 5, 0, 5],
        'Australia': [15, 10, 5, 0, 5, 10]}

# Convert data into pandas dataframe
df = pd.DataFrame(data).set_index('Product Type')

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Plot heatmap using seaborn
sns.heatmap(df, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='white', cbar=False)

# Set x and y tick labels in the center of rows and columns
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor', wrap=True)

# Set title
plt.title('Global Consumption of Food and Beverages', fontsize=18)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-134212_44.png', bbox_inches='tight')

# Clear the current image state
plt.clf()