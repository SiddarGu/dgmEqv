
# Code:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Process the data
data = {'Route': ['Seattle to Portland', 'Los Angeles to San Francisco', 'New York to Chicago', 'Miami to Atlanta', 'Houston to Dallas'],
        'On-time Performance (%)': [90, 95, 85, 92, 88],
        'Delivery Time (Minutes)': [120, 180, 240, 150, 130],
        'Distance (Miles)': [173, 350, 800, 660, 225],
        'Cargo Weight (Tons)': [5.5, 8.2, 12.5, 10, 6],
        'Fuel Efficiency (Miles per Gallon)': [28, 25, 20, 23, 26],
        'Cost (Dollars)': [350, 500, 800, 600, 400]}

df = pd.DataFrame(data)
df.set_index('Route', inplace=True)

# Plot the heatmap chart
fig, ax = plt.subplots(figsize=(10, 7))
heatmap = ax.pcolor(df, cmap='YlGnBu')

# Set x and y ticks and ticklabels
ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=False)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df.index, rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# Add colorbar
cbar = fig.colorbar(heatmap)

# Show cell values
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        if df.iloc[i, j] > 600 or df.iloc[i, j] < 100:
            ax.text(j + 0.5, i + 0.5, df.iloc[i, j], ha='center', va='center', color='w', size='large')
        else:
            ax.text(j + 0.5, i + 0.5, df.iloc[i, j], ha='center', va='center', color='black', size='large')

# Set title
ax.set_title('Logistics Efficiency by Route')

# Automatically resize and save the image
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_1.png', bbox_inches='tight')

# Clear the current image state
plt.clf()