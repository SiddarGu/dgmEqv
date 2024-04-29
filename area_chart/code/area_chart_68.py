
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Represent data using dictionary
data = {'Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty & Health', 'Toys & Games', 'Food & Beverage', 'Automotive', 'Sports & Outdoors', 'Pet Supplies', 'Jewelry', 'Furniture', 'Office Supplies', 'Beauty & Personal Care'], 'Retail Sales ($)': [5000, 6000, 4000, 3000, 2500, 7000, 4000, 3000, 2000, 1500, 5000, 2000, 3000], 'E-commerce Sales ($)': [3000, 4000, 2000, 1500, 1000, 5000, 3000, 2000, 1000, 500, 4000, 1000, 2000], 
'Retail Revenue ($)': [3500, 4500, 3000, 2500, 2000, 6500, 3500, 2500, 1500, 1000, 4500, 1500, 2500], 
'E-commerce Revenue ($)': [2500, 3500, 1500, 1000, 500, 4500, 2500, 1500, 500, 250, 3500, 500, 1500]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data as stacked area chart
ax.stackplot(df['Category'], df['Retail Sales ($)'], df['E-commerce Sales ($)'], 
             df['Retail Revenue ($)'], df['E-commerce Revenue ($)'], 
             labels=['Retail Sales', 'E-commerce Sales', 'Retail Revenue', 'E-commerce Revenue'], 
             colors=['#6ca9d2', '#d8c770', '#ff6347', '#98fb98'], alpha=0.7)

# Set x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Sales ($)')
ax.set_title('Retail and E-commerce Sales by Category')

# Set ticks and ticklabels for x axis
ax.set_xticks(np.arange(len(df['Category'])))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Calculate max total value and set suitable y limit and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend and adjust position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Randomly set background grid lines
ax.grid(color='gray', linestyle='--', alpha=0.2)

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_5.png', bbox_inches='tight')

# Clear current image state
plt.clf()