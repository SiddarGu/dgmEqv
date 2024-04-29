
# Import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dataframe
data = {'Category': ['Clothing', 'Electronics', 'Beauty', 'Home Goods', 'Toys'],
        'Revenue (in millions)': [500, 800, 300, 400, 200],
        'Sales Growth (%)': [5, 3, 8, 4, 2],
        'Market Share (%)': [20, 25, 15, 10, 5]}
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Create heatmap
heatmap = ax.imshow(df[['Revenue (in millions)', 'Sales Growth (%)', 'Market Share (%)']], cmap='Blues')

# Add colorbar
plt.colorbar(heatmap)

# Set x and y tick labels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df['Category'])))
ax.set_yticklabels(df['Category'])

# Set tick labels in the center of each cell
ax.set_xticks(np.arange(len(df.columns) + 1) - 0.5, minor=True)
ax.set_yticks(np.arange(len(df['Category']) + 1) - 0.5, minor=True)
ax.grid(which='minor', color='white', linestyle='-', linewidth=2)

# Add labels to each cell
for i in range(len(df['Category'])):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha='center', va='center')

# Set title
ax.set_title('Revenue and Market Share by Product Category')

# Automatically resize and save image
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_3.png', bbox_inches='tight')

# Clear current image state
plt.clf()