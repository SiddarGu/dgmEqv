
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
       'Tax ($)': [5000, 5200, 4500, 5100],
       'Investment ($)': [4000, 4100, 4900, 3500],
       'Profit ($)': [6000, 5500, 3300, 3200],
       'Revenue ($)': [3000, 2200, 2800, 2500]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create axes
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value and set y limit and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df['Quarter'], df['Tax ($)'], df['Investment ($)'], df['Profit ($)'], df['Revenue ($)'], labels=['Tax', 'Investment', 'Profit', 'Revenue'], colors=['#4d79ff', '#66cc33', '#ff9933', '#ff0066'], alpha=0.8)

# Set background grid lines
ax.grid(color='#cccccc')

# Set legend and position
ax.legend(loc='upper left', frameon=False)

# Set ticks and tick labels for x axis
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Quarter'], rotation=45, ha='right', rotation_mode='anchor')

# Set title
ax.set_title('Financial Performance by Quarter')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-130527_10.png', bbox_inches='tight')

# Clear figure
plt.clf()