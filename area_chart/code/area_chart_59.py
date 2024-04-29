
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary of data
data = {'Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Furniture', 'Groceries', 'Books', 'Sporting Goods', 'Toys', 'Pet Supplies', 'Auto Parts', 'Health & Wellness', 'Arts & Crafts', 'Appliances'], 'Online Sales (in $)': [50000,40000,30000,20000,40000,50000,30000,40000,20000,50000,40000,30000,20000,40000], 'In-store Sales (in $)': [30000,35000,25000,15000,35000,30000,25000,35000,15000,30000,35000,25000,15000,35000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 10:
    ax.set_yticks(np.linspace(0, max_total_value, 3, dtype=np.int32))
elif max_total_value <= 100:
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5]), dtype=np.int32))
elif max_total_value <= 1000:
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7]), dtype=np.int32))
elif max_total_value <= 10000:
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9]), dtype=np.int32))
else:
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], labels=['Online Sales (in $)', 'In-store Sales (in $)'], alpha=0.8)

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.2)

# Set legend and position
ax.legend(loc='upper right')

# Set title
plt.title('Retail and E-commerce Sales by Category')

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-131755_39.png', bbox_inches='tight')

# Clear figure
plt.close()