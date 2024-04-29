
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import seaborn for heatmap
import seaborn as sns

# Set data
data = {'Category':['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Toys', 'Sports', 'Furniture'],
        'Revenue (millions)':[500, 800, 350, 300, 400, 600, 700],
        'Profit (millions)':[100, 200, 50, 50, 80, 120, 150],
        'Expenses (millions)':[200, 300, 100, 100, 150, 200, 250],
        'Sales (millions)':[400, 700, 300, 250, 350, 500, 600],
        'Customers (millions)':[10, 15, 5, 7, 8, 12, 14],
        'Inventory (thousands)':[50, 75, 25, 30, 40, 60, 70]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set figure size
fig = plt.figure(figsize=(10, 8))

# Set title
plt.title('Retail and E-commerce Performance Metrics')

# Set x and y ticks
xticks = ['Revenue (millions)', 'Profit (millions)', 'Expenses (millions)', 'Sales (millions)', 'Customers (millions)', 'Inventory (thousands)']
yticks = ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Toys', 'Sports', 'Furniture']

# Set x and y labels
plt.xlabel('Metrics')
plt.ylabel('Categories')

# Set x and y tick labels
plt.xticks(np.arange(len(xticks)), xticks, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(len(yticks)), yticks)

# Plot heatmap using seaborn
sns.heatmap(df.set_index('Category'), annot=True, fmt='g')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-124154_38.png', bbox_inches='tight')

# Clear current image state
plt.clf()