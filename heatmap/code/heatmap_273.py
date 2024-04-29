
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dataframe from given data
df = pd.DataFrame({'Product':['Widget A', 'Widget B', 'Widget C', 'Widget D', 'Widget E'],
                   'Target Production (Units)':[1000, 1500, 2000, 500, 3000],
                   'Actual Production (Units)':[950, 1475, 1900, 475, 3100],
                   'Production Variance (%)':[-5, -2, -5, -5, 3],
                   'Efficiency (%)':[98, 95, 96, 94, 97],
                   'Downtime (Hours)':[3, 2, 4, 5, 1],
                   'Scrap Rate (%)':[2, 1, 3, 5, 1]})

# Set figure size
fig = plt.figure(figsize=(8,6))

# Plot heatmap
ax = plt.axes()
heatmap = ax.pcolor(df.iloc[:,1:], cmap='Blues', alpha=0.8)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(0.5, len(df.columns)-1, 1))
ax.set_yticks(np.arange(0.5, len(df), 1))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Product'])

# Add colorbar
plt.colorbar(heatmap)

# Set title
ax.set_title('Manufacturing Production Metrics')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-162116_7.png', bbox_inches='tight')

# Clear current image state
plt.clf()