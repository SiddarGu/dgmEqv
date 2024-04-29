
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data = {
    'Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty & Cosmetics', 'Toys & Games', 'Food & Beverage', 'Sporting Goods', 'Furniture'],
    'Revenue ($)': [50000, 80000, 40000, 30000, 60000, 100000, 70000, 40000],
    'Online Sales ($)': [30000, 50000, 20000, 15000, 40000, 60000, 50000, 30000],
    'In-store Sales ($)': [20000, 30000, 20000, 15000, 20000, 40000, 20000, 10000],
    'Total Sales ($)': [50000, 80000, 40000, 30000, 60000, 100000, 70000, 40000]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set the colors and transparency for the area chart
colors = ['#b2d8d8', '#e1b2e1', '#e1d8b2', '#98fb98']
alpha = 0.7

# Plot the area chart
ax.stackplot(df.index, df['Revenue ($)'], df['Online Sales ($)'], df['In-store Sales ($)'],
    df['Total Sales ($)'], labels=['Revenue ($)', 'Online Sales ($)', 'In-store Sales ($)', 'Total Sales ($)'], colors=colors, alpha=alpha)
ax.legend(loc='upper left')

# Set the background grid lines
ax.grid(axis='y', alpha=0.3)

# Set the x and y ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)

# Calculate the max total value and set the yticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set the tick labels
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(['$' + str(int(i)) for i in ax.get_yticks()], wrap=True, rotation=0)

# Set the title and labels
ax.set_title('Retail and E-commerce Sales by Category', fontsize=16)
ax.set_xlabel('Category', fontsize=12)
ax.set_ylabel('Sales ($)', fontsize=12)

# Automatically resize the image and save it
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_29.png', bbox_inches='tight')

# Clear the current image state
plt.clf()