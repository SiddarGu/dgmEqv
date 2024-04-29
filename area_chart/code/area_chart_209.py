


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
d = {'Category': ['Apparel', 'Electronics', 'Beauty', 'Home Goods', 'Toys', 'Sports & Outdoors', 'Furniture', 'Food & Beverage', 'Health & Wellness'],
    'Total Sales ($)': [200000, 300000, 100000, 250000, 50000, 150000, 200000, 250000, 100000],
    'Online Sales ($)': [150000, 200000, 50000, 150000, 20000, 100000, 100000, 150000, 50000],
    'In-store Sales ($)': [50000, 100000, 50000, 100000, 30000, 50000, 100000, 100000, 50000]}

# Convert dictionary to pandas dataframe
df = pd.DataFrame(data=d)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and tick labels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set axis labels and title
ax.set_xlabel('Category')
ax.set_ylabel('Sales ($)')
ax.set_title('Retail and E-commerce Sales by Category')

# Set background grid lines
ax.grid(True)

# Plot area chart
ax.stackplot(df['Category'], df['Total Sales ($)'], df['Online Sales ($)'], df['In-store Sales ($)'], labels=['Total Sales', 'Online Sales', 'In-store Sales'], colors=['#ff7f0e', '#1f77b4', '#2ca02c'], alpha=0.7)

# Add legend and adjust position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_45.png', bbox_inches='tight')

# Clear current image state
plt.clf()