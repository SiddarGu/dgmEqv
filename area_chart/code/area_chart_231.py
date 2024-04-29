
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the data as a dictionary
data = {'Category': ['Apparel', 'Beauty and Personal Care', 'Electronics', 'Furniture and Home Decor', 'Groceries and Household Supplies', 'Health and Wellness', 'Media and Entertainment', 'Sporting Goods', 'Toys and Games', 'Travel and Tourism', 'Automotive', 'Home Improvement', 'Pet Supplies'], 'Total Retail Sales ($)': [50000, 30000, 70000, 40000, 90000, 35000, 60000, 45000, 25000, 80000, 100000, 60000, 30000], 'E-commerce Sales ($)': [20000, 15000, 50000, 30000, 45000, 25000, 40000, 35000, 15000, 70000, 80000, 50000, 20000]}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the data with stackplot
ax.stackplot(df['Category'], df['Total Retail Sales ($)'], df['E-commerce Sales ($)'], labels=['Total Retail Sales ($)', 'E-commerce Sales ($)'], colors=['#FFA07A', '#87CEEB'], alpha=0.7)

# Set random grid lines
ax.grid(linestyle='--', linewidth=0.5, color='gray')

# Calculate the max total value and round up to the nearest multiple of 1000
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/1000)*1000

# Set the suitable y-axis range and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set the x-axis range
ax.set_xlim(0, len(df.index) - 1)

# Set the rotation and alignment for the x-axis tick labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Set the legend and its position
ax.legend(loc='upper left')

# Set the title and labels
ax.set_title('Retail and E-commerce Sales by Category')
ax.set_xlabel('Category')
ax.set_ylabel('Sales ($)')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/area_chart/png/20231228-145339_76.png', bbox_inches='tight')

# Clear the current image state
plt.clf()