


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Category': ['Sociology', 'Psychology', 'History', 'Literature', 'Political Science'],
        '2015': [500, 400, 300, 200, 100],
        '2016': [600, 500, 400, 300, 200],
        '2017': [700, 600, 500, 400, 300],
        '2018': [800, 700, 600, 500, 400],
        '2019': [900, 800, 700, 600, 500]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up to nearest multiple of 10, 100, or 1000
if max_total_value > 1000:
    max_total_value = np.ceil(max_total_value / 1000) * 1000
elif max_total_value > 100:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 10) * 10

# Plot area chart
ax.stackplot(df['Category'], df['2015'], df['2016'], df['2017'], df['2018'], df['2019'], labels=['2015', '2016', '2017', '2018', '2019'],
             colors=['#4b86b4', '#69b1c5', '#b1e1e2', '#fde8c8', '#f3b89b'], alpha=0.8)

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, max_total_value)

# Set y ticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Add grid lines
ax.grid(axis='y', linestyle='--')
ax.grid(axis='x', linestyle='-', color='gray', alpha=0.3)

# Set tick labels
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticks(), rotation=0, ha='right', rotation_mode='anchor')

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)

# Set title
plt.title('Publication Trends in Social Sciences and Humanities from 2015 to 2019')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_13.png', bbox_inches='tight')

# Clear current image state
plt.clf()