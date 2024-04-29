
# Import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data dictionary
data = {'2018': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                'Oct', 'Nov', 'Dec'],
        'Sales ($)': [500000, 600000, 700000, 800000, 900000, 1000000, 1100000,
                      1200000, 1300000, 1400000, 1500000, 1600000],
        'Revenue ($)': [450000, 550000, 650000, 750000, 850000, 950000, 1050000,
                        1150000, 1250000, 1350000, 1450000, 1550000],
        'Profit ($)': [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000,
                       50000, 50000, 50000, 50000],
        'Customers': [12000, 15000, 18000, 20000, 22000, 25000, 28000, 30000,
                      32000, 35000, 38000, 40000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value and round up to nearest multiple of 10, 100, or 1000
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set x and y limits and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart with transparency and random colors
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4],
             colors=[np.random.rand(4) for i in range(4)], alpha=0.7)

# Set x and y axis labels and tick labels
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Amount ($)', fontsize=12)
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# Set title
plt.title('Retail and E-commerce Performance in 2018', fontsize=14)

# Add legend with labels and units
ax.legend(labels=['Sales', 'Revenue', 'Profit', 'Customers'], loc='upper left')
ax.set_ylabel('Amount ($)', fontsize=12)

# Add grid lines
ax.grid(linestyle='dashed', alpha=0.5)

# Automatically adjust image size and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_2.png', bbox_inches='tight')

# Clear current image state
plt.clf()