
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create dictionary for data
data = {'Area': ['Q1', 'Q2', 'Q3', 'Q4'], 
        'Online Sales (in thousands)': [500, 520, 480, 510],
        'In-Store Sales (in thousands)': [400, 410, 450, 420]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set up plot
fig, ax = plt.subplots(figsize=(10, 6))
plt.tight_layout()

# Set background grid lines
ax.grid(color='lightgrey', linestyle='-', linewidth=0.5, alpha=0.5)

# Plot area chart
ax.stackplot(df['Area'], df['Online Sales (in thousands)'], df['In-Store Sales (in thousands)'], labels=['Online Sales', 'In-Store Sales'], colors=['#FFA07A', '#ADD8E6'], alpha=0.7)

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df['Area'])))
ax.set_xticklabels(df['Area'])

# Calculate max total value and set y axis ticks and ticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend and labels
ax.legend(loc='upper left')
plt.ylabel('Sales (in thousands)', labelpad=10)
plt.xlabel('Quarter')

# Set title
plt.title('Retail and E-commerce Sales Comparison by Quarter')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_40.png', bbox_inches='tight')

# Clear current image state
plt.clf()