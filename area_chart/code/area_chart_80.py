


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Represent data using dictionary
data = {'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
        'Revenue ($)': [500000, 520000, 540000, 550000],
        'Profit ($)': [200000, 220000, 230000, 240000],
        'Expenses ($)': [300000, 290000, 280000, 270000],
        'Net Income ($)': [100000, 120000, 150000, 160000]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df['Quarter'], df['Revenue ($)'], df['Profit ($)'], df['Expenses ($)'], df['Net Income ($)'], labels=['Revenue', 'Profit', 'Expenses', 'Net Income'], colors=['#8AC6D1', '#F9B1B1', '#FCCDAD', '#9BB7D4'], alpha=0.8)

# Set ticks and ticklabels for x axis
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df['Quarter'])
    plt.setp(ax.get_xticklabels(), ha="right", rotation_mode="anchor", rotation=45)

# Set ticks and ticklabels for y axis
if np.random.choice([True, False], p=[0.7, 0.3]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 1000) * 1000
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.grid(color='grey', linestyle='-', linewidth=0.5)

# Set legend position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Title and labels
ax.set_title('Quarterly Financial Performance')
ax.set_ylabel('Amount ($)')
ax.set_xlabel('Quarter')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-131755_62.png', bbox_inches='tight')

# Clear current image state
plt.clf()