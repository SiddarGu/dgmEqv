
# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'], 'Revenue ($)': [500000, 520000, 550000, 580000], 'Expenses ($)': [400000, 410000, 430000, 450000], 'Profit ($)': [100000, 110000, 120000, 130000], 'Growth (%)': [10, 12, 15, 17]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10,6))

# Plot area chart
ax.stackplot(df['Quarter'], df['Revenue ($)'], df['Expenses ($)'], labels=['Revenue ($)', 'Expenses ($)'], colors=['#4d4dff', '#ff4d4d'], alpha=0.8)

# Set x and y axis limits and ticks
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis labels
ax.set_xlabel('Quarter')
ax.set_ylabel('Amount ($)')

# Set title
ax.set_title('Business Performance Trends')

# Add background grid lines
ax.grid(axis='y', alpha=0.5)

# Adjust legend position
ax.legend(loc='upper right')

# Automatically resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_0.png', bbox_inches='tight')

# Clear current image state
plt.clf()