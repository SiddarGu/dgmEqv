
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Category': ['Meat', 'Dairy', 'Bakery', 'Produce', 'Beverages'], 'Restaurant Sales ($)': [5000, 4500, 3500, 4000, 6000], 'Grocery Sales ($)': [4000, 3500, 3000, 3500, 5000], 'Food Production ($)': [3000, 2500, 2000, 4000, 4000], 'Beverage Production ($)': [6000, 5000, 4000, 3000, 7000]}

# Process data
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create axes
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Ceil up to nearest multiple of 1000
max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y limits and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot data as stacked area chart
ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.iloc[:, 1:].columns, colors=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3'], alpha=0.8)

# Set x limits and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(df.index)
ax.set_xticklabels(df.iloc[:, 0])

# Set x and y labels
ax.set_xlabel('Category')
ax.set_ylabel('Sales and Production ($)')

# Set title
ax.set_title('Sales and Production in the Food and Beverage Industry')

# Add grid lines
ax.grid(color='lightgrey', linestyle='--')

# Add legend
ax.legend(loc='upper left')

# Automatically resize image before saving
fig.tight_layout()

# Save image
fig.savefig('output/final/area_chart/png/20231228-155112_52.png', bbox_inches='tight')

# Clear current image state
plt.clf()