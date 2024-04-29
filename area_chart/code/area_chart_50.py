

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'], 
        'Revenue ($)': [100000, 95000, 110000, 120000], 
        'Expenses ($)': [80000, 85000, 90000, 95000], 
        'Profit ($)': [20000, 10000, 20000, 25000]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot chart using ax.stackplot()
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df['Quarter'], df['Revenue ($)'], df['Expenses ($)'], labels=['Revenue ($)', 'Expenses ($)'], colors=['#4BFFB8', '#FF5C5C'], alpha=0.6)

# Calculate and set suitable y-axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x-axis ticks and ticklabels
ax.set_xticks(np.arange(len(df['Quarter'])))
ax.set_xticklabels(df['Quarter'], rotation=45, ha='right', rotation_mode='anchor')

# Set y-axis ticklabels
ax.set_yticklabels(['${:,.0f}'.format(x) for x in ax.get_yticks()])

# Set background grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.4)

# Set legend position and labels
ax.legend(loc='upper right', frameon=False)

# Set title and labels
plt.title('Financial Performance Analysis')
plt.xlabel('Quarter')
plt.ylabel('Amount ($)')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_25.png', bbox_inches='tight')

# Clear current image state
plt.clf()