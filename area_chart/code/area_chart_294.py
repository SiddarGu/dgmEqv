
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Represent the data using a dictionary
data = {'Area': ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania', 'Antarctica'], 
        'Stock Value ($)': [200, 100, 150, 100, 200, 150, 180],
        'Investment ($)': [150, 120, 180, 200, 180, 200, 150],
        'Profit ($)': [180, 150, 200, 250, 150, 100, 100],
        'Revenue ($)': [130, 100, 150, 180, 130, 250, 200]}

# Use pandas "df = pd.DataFrame(data)" to process the data
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Use ax.stackplot() to plot the chart
ax.stackplot(df['Area'], df['Stock Value ($)'], df['Investment ($)'], df['Profit ($)'], df['Revenue ($)'], labels=['Stock Value ($)', 'Investment ($)', 'Profit ($)', 'Revenue ($)'], colors=['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728'], alpha=0.7)

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and round up to nearest multiple of 10, 100 or 1000
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10

# Set y axis range and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis labels
ax.set_xlabel('Area')
ax.set_ylabel('Amount ($)')
ax.set_title('Business and Finance Across Continents')

# Set background grid lines
ax.grid()

# Adjust legend position
ax.legend(loc='upper left')

# Automatically resize image and save
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-161902_1.png', bbox_inches='tight')

# Clear image state
plt.clf()