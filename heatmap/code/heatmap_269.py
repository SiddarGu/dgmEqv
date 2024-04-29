
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set data
data = {'Product Category': ['Clothing', 'Electronics', 'Home Goods', 'Toys', 'Beauty', 'Sports', 'Food', 'Furniture', 'Shoes'],
        'April 2020 Sales ($)': [500, 1000, 600, 300, 400, 700, 1200, 900, 800],
        'May 2020 Sales ($)': [600, 1100, 700, 400, 500, 800, 1300, 1000, 900],
        'June 2020 Sales ($)': [700, 1200, 800, 500, 600, 900, 1400, 1100, 1000],
        'July 2020 Sales ($)': [800, 1300, 900, 600, 700, 1000, 1500, 1200, 1100],
        'August 2020 Sales ($)': [900, 1400, 1000, 700, 800, 1100, 1600, 1300, 1200]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set figure size
fig = plt.figure(figsize=(10,8))

# Set title
plt.title('Retail Sales by Product Category')

# Create heatmap using seaborn
sns.heatmap(df.set_index('Product Category'), cmap='YlGnBu', annot=True, fmt='.0f', cbar=True)

# Set rotation and alignment of x and y ticks
plt.yticks(rotation=45, ha='right', rotation_mode='anchor')
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-162116_26.png', bbox_inches='tight')

# Clear current image state
plt.clf()