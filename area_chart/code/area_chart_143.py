


# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create data dictionary
data = {'Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Food'],
        'Total Sales ($)': [500000, 800000, 600000, 300000, 400000],
        'Online Sales ($)': [250000, 400000, 300000, 150000, 200000],
        'In-Store Sales ($)': [250000, 400000, 300000, 150000, 200000],
        'E-commerce Sales ($)': [150000, 200000, 180000, 90000, 120000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 7))

# Plot area chart
ax = plt.axes()
ax.stackplot(df.index, df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=['Total Sales', 'Online Sales', 'In-Store Sales', 'E-commerce Sales'], colors=['#FFBF00', '#0080FF', '#FF00FF', '#800000'], alpha=0.5)

# Set x and y axis ticks
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.iloc[:, 0])

    # Rotate x axis labels if length is more than 6 characters
    for tick in ax.get_xticklabels():
        if len(tick.get_text()) > 6:
            tick.set_rotation(45)
            tick.set_ha('right')
            tick.set_rotation_mode('anchor')
else:
    ax.set_xticks([])

if np.random.choice([True, False], p=[0.7, 0.3]):
    # Get max total value
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()

    # Ceil max total value up to nearest multiple of 10, 100, or 1000
    if max_total_value > 1000:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    elif max_total_value > 100:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 10) * 10

    # Set y axis ticks and tick labels
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(ax.get_yticks())

    # Rotate y axis labels if length is more than 6 characters
    for tick in ax.get_yticklabels():
        if len(tick.get_text()) > 6:
            tick.set_rotation(45)
            tick.set_ha('right')
            tick.set_rotation_mode('anchor')
else:
    ax.set_yticks([])

# Set grid lines
plt.grid(color='gray', linestyle='dashed', linewidth=0.5)

# Set legend
ax.legend(loc='upper left')

# Set title
plt.title('Retail and E-commerce Sales Analysis')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-140159_6.png', bbox_inches='tight')

# Clear current image state
plt.clf()