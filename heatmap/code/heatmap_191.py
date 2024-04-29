
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Import data
data = {'Category':['Apparel', 'Electronics', 'Home Goods', 'Beauty', 'Groceries', 'Furniture', 'Automotive', 'Sports', 'Toys'],
        'Online Sales ($)':[300, 500, 400, 200, 600, 200, 400, 300, 100],
        'In-store Sales ($)':[500, 700, 600, 300, 800, 400, 500, 400, 200],
        'Total Sales ($)':[800, 1200, 1000, 500, 1400, 600, 900, 700, 300],
        'Online Sales Growth (%)':[8, 12, 10, 5, 15, 4, 8, 6, 2],
        'In-store Sales Growth (%)':[6, 8, 7, 4, 12, 6, 5, 5, 3],
        'Total Sales Growth (%)':[7, 10, 9, 4, 14, 5, 6, 5, 2]
       }

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10,8))

# Create heatmap chart
ax = sns.heatmap(df.iloc[:,1:], annot=True, fmt='.0f', cmap='Blues', linewidths=0.5, cbar=False)

# Set title
plt.title('Retail and E-commerce Sales by Category')

# Set tick positions and labels
ax.set_xticks(np.arange(len(df.columns)-1) + 0.5)
ax.set_yticks(np.arange(len(df)) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Category'], rotation=0, ha='right')

# Set tick positions in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns)-1) + 0.5, minor=True)
ax.set_yticks(np.arange(len(df)) + 0.5, minor=True)

# Add grid lines
ax.grid(which='minor', color='w', linestyle='-', linewidth=3)

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-134212_51.png', bbox_inches='tight')

# Clear image
plt.clf()