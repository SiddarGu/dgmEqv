
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data dictionary
data_dict = {'Sport': ['Football', 'Basketball', 'Baseball', 'Soccer', 'Hockey', 'Tennis', 'Golf', 'Racing', 'Boxing', 'Other'], 
            'Total Revenue ($)': [100000, 80000, 60000, 40000, 30000, 20000, 10000, 5000, 2000, 1000], 
            'Ticket Sales ($)': [80000, 60000, 50000, 30000, 25000, 15000, 8000, 3000, 1000, 500], 
            'Food and Beverage Sales ($)': [15000, 12000, 10000, 5000, 4000, 3000, 1000, 500, 200, 100], 
            'Merchandise Sales ($)': [3000, 2500, 2000, 1000, 500, 500, 200, 100, 50, 25], 
            'Other Revenue ($)': [5000, 3000, 1500, 500, 500, 500, 200, 100, 50, 25]}

# Convert data dictionary to dataframe
df = pd.DataFrame(data_dict)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value and round up to nearest multiple of 10000
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = int(np.ceil(max_total_value / 10000.0)) * 10000

# Set y ticks
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

# Set y tick labels
yticklabels = ["${:,.0f}".format(i) for i in yticks]

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Ticket Sales', 'Food and Beverage Sales', 'Merchandise Sales', 'Other Revenue'], alpha=0.7)

# Set legend position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, max_total_value)

# Set x and y axis ticks and labels
ax.set_xticks(df.index)
ax.set_xticklabels(df['Sport'])

ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)

# Set axis label
ax.set_xlabel('Sport')
ax.set_ylabel('Total Revenue ($)')

# Set title
ax.set_title('Sports Revenue Breakdown by Category')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-131755_49.png', bbox_inches='tight')

# Clear current image state
plt.close(fig)