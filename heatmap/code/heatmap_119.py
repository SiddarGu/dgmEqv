


# Retail and E-commerce Performance

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data processing
data = {'Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Sports'],
        'Online Sales (in millions)': [250, 350, 200, 150, 100],
        'In-Store Sales (in millions)': [300, 400, 250, 200, 150],
        'Online Traffic (in millions)': [350, 300, 200, 150, 100],
        'In-Store Traffic (in millions)': [400, 350, 250, 200, 150],
        'Average Order Value (in dollars)': [50, 75, 100, 35, 40],
        'Conversion Rate (%)': [25, 30, 20, 15, 10]}

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Plotting the heatmap
fig, ax = plt.subplots(figsize=(8, 6))
heatmap = ax.pcolor(df, cmap='Blues')

# Setting ticks and labels
ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=False)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Adding colorbar
cbar = plt.colorbar(heatmap)

# Setting title and labels
ax.set_title('Retail and E-commerce Performance')
ax.set_xlabel('Metrics')
ax.set_ylabel('Categories')

# Show values in each cell
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        text = ax.text(j + 0.5, i + 0.5, df.iloc[i, j], ha='center', va='center', color='black')

# Resizing and saving the image
plt.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-131639_23.png', bbox_inches='tight')

# Removing current image state
plt.clf()