
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data processing
data = {'Category': ['Clothing', 'Electronics', 'Beauty', 'Home Goods', 'Grocery', 'Accessories', 'Toys', 'Health and Wellness', 'Furniture'], 
        'E-commerce Revenue (Billion USD)': [100, 150, 75, 50, 200, 40, 30, 60, 50], 
        'Online Sales Growth (%)': [25, 20, 30, 15, 35, 10, 5, 12, 10], 
        'Store Sales Growth (%)': [5, 10, 7, 3, 2, 4, 7, 8, 3], 
        'E-commerce Share of Total Sales (%)': [20, 25, 15, 10, 40, 5, 3, 6, 7], 
        'Average Order Value (USD)': [50, 100, 40, 30, 75, 20, 15, 35, 45]}

df = pd.DataFrame(data)
df = df.set_index('Category')

# Plotting the heatmap chart
fig, ax = plt.subplots(figsize=(12,8)) # Setting the size of the figure

# Using the 30% probability of sns.heatmap()
sns.heatmap(data=df, annot=True, cbar=False, cmap='Blues', fmt='g', square=True)

# Using the 70% probability of imshow() or pcolor()
# ax.pcolor(df, cmap='Blues')
# ax.set_xticks(np.arange(0.5, len(df.columns), 1))
# ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
# ax.set_yticks(np.arange(0.5, len(df.index), 1))
# ax.set_yticklabels(df.index, rotation=0, ha='center')
# ax.set_xlabel('E-commerce Metrics')
# ax.set_ylabel('Retail Categories')

# Adding colorbar
# cbar = plt.colorbar()
# cbar.ax.set_ylabel('Value', rotation=90)

# Setting the title and labels
ax.set_title('E-commerce Growth by Retail Category')
ax.set_xlabel('E-commerce Metrics')
ax.set_ylabel('Retail Categories')

# Automatically resizing the image
plt.tight_layout()

# Saving the image
plt.savefig('output/final/heatmap/png/20231226-140552_18.png', bbox_inches='tight')

# Clearing the current image state
plt.clf()