
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import seaborn for heatmap chart
import seaborn as sns

# Define data
data = {'Product': ['Soda', 'Chips', 'Cookies', 'Candy', 'Water'],
        'Cost (USD)': [1.25, 0.75, 1.00, 0.50, 0.25],
        'Price (USD)': [2.00, 1.50, 2.00, 1.00, 1.00],
        'Sales (Units)': [500, 800, 600, 700, 1000],
        'Revenue (USD)': [1000, 1200, 1200, 700, 1000],
        'Profit (USD)': [500, 400, 600, 300, 750],
        'Market Share (%)': [10, 8, 12, 6, 15]}

# Convert data into pandas DataFrame
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6))

# Create heatmap chart using seaborn
ax = sns.heatmap(df.set_index('Product'), annot=True, cmap="YlGnBu", cbar=False)

# Set x and y tick labels
# ax.set_xticklabels(['Cost (USD)', 'Price (USD)', 'Sales (Units)', 'Revenue (USD)', 'Profit (USD)', 'Market Share (%)'], rotation=45, ha='right', rotation_mode='anchor')
# ax.set_yticklabels(['Cost (USD)', 'Price (USD)', 'Sales (Units)', 'Revenue (USD)', 'Profit (USD)', 'Market Share (%)'], rotation=0, ha='right', rotation_mode='anchor')

# Set x and y ticks in the center of rows and columns
# ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=False)
# ax.set_yticks(np.arange(len(df.columns)) + 0.5, minor=False)

# Set title
ax.set_title('Sales and Profit in the Food and Beverage Industry')

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-124154_57.png', bbox_inches='tight')

# Clear the current image state
plt.clf()