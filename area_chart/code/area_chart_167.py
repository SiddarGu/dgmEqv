
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# Set random seed
np.random.seed(12345)

# Define data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Produce Yield (lbs)': [5000, 4500, 5500, 6000, 6500, 7000, 7500, 8000, 7500, 7000, 6500, 6000],
    'Crop Sales ($)': [2000, 1800, 2200, 2400, 2600, 2800, 3000, 3200, 3000, 2800, 2600, 2400],
    'Seed Cost ($)': [1000, 900, 1100, 1200, 1300, 1400, 1500, 1600, 1500, 1400, 1300, 1200],
    'Fertilizer Cost ($)': [500, 450, 550, 600, 650, 700, 750, 800, 750, 700, 650, 600],
    'Pesticide Cost ($)': [200, 180, 220, 240, 260, 280, 300, 320, 300, 280, 260, 240]
}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Set axis
ax = fig.add_subplot()

# Stack plot
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Produce Yield (lbs)', 'Crop Sales ($)', 'Seed Cost ($)', 'Fertilizer Cost ($)', 'Pesticide Cost ($)'], colors=['#FFB6C1', '#87CEFA', '#F0E68C', '#98FB98', '#FFA07A'], alpha=0.7)

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Ceil max total value up to the nearest multiple of 10, 100 or 1000
if max_total_value <= 10:
    max_total_value = np.ceil(max_total_value)
elif max_total_value <= 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value <= 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y limits
ax.set_ylim(0, max_total_value)

# Set y ticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(axis='y', color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

# Set title
ax.set_title('Crop Production and Sales by Month')

# Set legend
ax.legend(loc='upper right')

# Set x and y labels
ax.set_xlabel('Month')
ax.set_ylabel('Amount (lbs/$)')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-140159_87.png', bbox_inches='tight')

# Clear figure
plt.clf()