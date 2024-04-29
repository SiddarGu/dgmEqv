
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define data dictionary
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], 
        'Expenses ($)': [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500], 
        'Revenue ($)': [6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500], 
        'Profit ($)': [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]}
        
# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10,6))

# Calculate max total value for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y axis limits and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df['Month'], df['Expenses ($)'], df['Revenue ($)'], df['Profit ($)'], labels=['Expenses', 'Revenue', 'Profit'], alpha=0.8)

# Set x axis limits and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Month'])

# Set grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5)

# Set legend 
ax.legend(loc='upper left')

# Set title
plt.title('Monthly Business Financial Report')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_55.png', bbox_inches='tight')

# Clear current image state
plt.clf()