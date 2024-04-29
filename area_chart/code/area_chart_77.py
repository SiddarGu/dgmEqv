
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define data as a dictionary
data = {'Sales': ['January', 'February', 'March', 'April', 'May'],
        'Revenue ($)': [10000, 12000, 15000, 18000, 20000],
        'Profit ($)': [8000, 9000, 11000, 13000, 14000],
        'Expenses ($)': [5000, 5500, 6000, 6500, 7000]}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Set x and y axis labels
ax.set_xlabel('Month')
ax.set_ylabel('Amount ($)')
ax.set_title('Sales and Profit Analysis for Retail and E-commerce Industry')

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/1000) * 1000
ax.set_ylim(0, max_total_value)

# Set x and y axis ticks and tick labels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(len(df)))
    ax.set_xticklabels(df.iloc[:, 0])
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot the data as an area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=['Revenue', 'Profit', 'Expenses'], colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.5)

# Set grid lines
ax.grid(linestyle='--', alpha=0.5)

# Set legend
ax.legend(loc='upper left')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_6.png', bbox_inches='tight')

# Clear the current image state
plt.clf()