
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {
    'Category': ['Restaurant', 'Grocery Store', 'Fast Food', 'Bakery', 'Convenience Store', 'Catering', 'Cafeteria', 'Food Truck', 'Pub', 'Coffee Shop', 'Food Delivery', 'Bar'],
    'Food Sales (in thousands)': [150, 100, 200, 150, 100, 250, 180, 100, 150, 200, 100, 150],
    'Beverage Sales (in thousands)': [100, 150, 100, 200, 120, 100, 120, 150, 200, 150, 180, 120],
    'Food and Beverage Expenses (in thousands)': [120, 80, 120, 100, 50, 150, 100, 120, 100, 100, 50, 100],
    'Net Profit (in thousands)': [80, 70, 100, 80, 70, 80, 80, 70, 70, 80, 70, 80]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)

# Set y ticks
yticks = np.random.choice([3, 5, 7, 9, 11])
ax.set_yticks(np.linspace(0, max_total_value, yticks, dtype=np.int32))

# Set background grid lines
ax.grid(alpha=0.3, linestyle='--')

# Plot area chart
ax.stackplot(df['Category'], df['Food Sales (in thousands)'], df['Beverage Sales (in thousands)'],
df['Food and Beverage Expenses (in thousands)'], df['Net Profit (in thousands)'],
 labels=['Food Sales (in thousands)', 'Beverage Sales (in thousands)', 'Food and Beverage Expenses (in thousands)', 'Net Profit (in thousands)'], 
 colors=['#FFB347', '#77DD77', '#FFA07A', '#B0E0E6'], alpha=0.7)

# Set legend and its position
ax.legend(loc='upper left')

# Set x and y labels and title
ax.set_xlabel('Category')
ax.set_ylabel('Sales (in thousands)')
ax.set_title('Food and Beverage Industry Financial Performance')

# Automatically resize the image
fig.tight_layout()

# Save the image
fig.savefig('output/final/area_chart/png/20231228-140159_84.png', bbox_inches='tight')

# Clear the current image state
plt.clf()