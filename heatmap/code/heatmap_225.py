
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process the data using dict and pandas
data = {'Factory': ['Factory A', 'Factory B', 'Factory C', 'Factory D', 'Factory E', 'Factory F', 'Factory G', 'Factory H', 'Factory I'],
        'Production (Units)': [100, 120, 140, 160, 180, 200, 220, 240, 260],
        'Efficiency (%)': [90, 85, 80, 75, 70, 65, 60, 55, 50],
        'Defect Rate (%)': [2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Downtime (Hours)': [5, 7, 10, 12, 15, 17, 20, 22, 25],
        'Maintenance Cost ($)': [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600],
        'Energy Cost ($)': [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]}
df = pd.DataFrame(data)

# Set figure size and title
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Manufacturing Metrics Comparison')

# Plot the heatmap chart using imshow()
im = ax.imshow(df.iloc[:, 1:].values, cmap='YlGn')

# Set x and y tick labels
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Factory'])))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Factory'])

# Add the value of each cell
for i in range(len(df['Factory'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j+1], ha='center', va='center', color='black')

# Add colorbar
cbar = fig.colorbar(im, ax=ax)

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_13.png', bbox_inches='tight')

# Clear the current image state
plt.clf()