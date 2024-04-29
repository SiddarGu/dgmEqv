
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

# Set the random seed
random.seed(55)

# Define the data as a dictionary
data = {'Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Sports', 'Food', 'Furniture', 'Toys', 'Health', 'Automotive', 'Music', 'Books', 'Office Supplies', 'Pet Supplies'], 'Revenue Generated ($)': [50000, 80000, 60000, 40000, 30000, 70000, 90000, 20000, 10000, 100000, 5000, 2000, 4000, 3000], 'Online Sales ($)': [30000, 50000, 40000, 25000, 20000, 50000, 60000, 10000, 5000, 70000, 3000, 1000, 2000, 1000], 'In-store Sales ($)': [20000, 30000, 20000, 15000, 10000, 20000, 30000, 10000, 5000, 30000, 2000, 1000, 2000, 2000], 'Total Sales ($)': [50000, 80000, 60000, 40000, 30000, 70000, 90000, 20000, 10000, 100000, 5000, 2000, 4000, 3000], 'Customer Retention (%)': [80, 75, 70, 85, 90, 85, 80, 95, 95, 75, 90, 95, 80, 85]}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig = plt.figure(figsize=(12,8))

# Plot the data as an area chart
ax = fig.add_subplot(1,1,1)
ax.stackplot(df['Category'], df['Revenue Generated ($)'], df['Online Sales ($)'], df['In-store Sales ($)'], df['Total Sales ($)'], labels=['Revenue Generated ($)', 'Online Sales ($)', 'In-store Sales ($)', 'Total Sales ($)'], alpha=0.75)

# Set the x-axis and y-axis labels
ax.set_xlabel('Category', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)

# Set the x-axis and y-axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 100:
    ax.set_ylim(0, max_total_value)
elif max_total_value < 1000:
    ax.set_ylim(0, max_total_value + (10 - (max_total_value % 10)))
elif max_total_value < 10000:
    ax.set_ylim(0, max_total_value + (100 - (max_total_value % 100)))
else:
    ax.set_ylim(0, max_total_value + (1000 - (max_total_value % 1000)))

# Set the y-axis ticks and tick labels
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set the x-axis tick labels
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Set the background grid lines
ax.grid(color='black', linestyle='-', linewidth=0.25, alpha=0.5)

# Set the legend
ax.legend(loc='upper left')

# Set the title
ax.set_title('Retail and E-commerce Revenue and Customer Retention Analysis', fontsize=16)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/area_chart/png/20231228-155112_55.png', bbox_inches='tight')

# Clear the current image state
plt.clf()