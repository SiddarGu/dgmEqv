
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process data
data = {'Factory': ['Factory A', 'Factory B', 'Factory C'],
        'Production Line Efficiency (%)': [85, 90, 80],
        'Maintenance Costs ($)': [50000, 70000, 60000],
        'Downtime (hours)': [200, 150, 300],
        'Labor Costs ($)': [100000, 110000, 90000],
        'Energy Costs ($)': [5000, 6000, 5500],
        'Waste Reduction (%)': [30, 25, 35]}

df = pd.DataFrame(data)
df = df.set_index('Factory')

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot heatmap
heat_map = sns.heatmap(df, annot=True, cmap='coolwarm', linewidths=1, linecolor='white', cbar=False)

# Set ticks and tick labels
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, fontsize=10, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, fontsize=10, rotation=0)

# Set title
ax.set_title('Manufacturing Cost Efficiency')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-134212_80.png', bbox_inches='tight')

# Clear current image state
plt.clf()