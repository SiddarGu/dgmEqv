


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data Processing
data = {'Crop': ['Wheat', 'Corn', 'Rice', 'Soybeans', 'Barley', 'Potatoes'],
        'Harvested Area (Million Hectares)': [30, 35, 20, 25, 15, 10],
        'Production (Million Tonnes)': [80, 100, 50, 70, 40, 30],
        'Yield (Tonnes per Hectare)': [2.67, 2.86, 2.50, 2.80, 2.67, 3.00],
        'Exports (Million Tonnes)': [20, 25, 15, 18, 10, 8],
        'Imports (Million Tonnes)': [10, 12, 8, 9, 5, 3]}

df = pd.DataFrame(data)
df.set_index('Crop', inplace=True)

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))

# 70% probability using imshow() or pcolor()
if np.random.rand() < 0.7:
    im = ax.imshow(df, cmap='YlGn')

    # 40% probability for adding colorbar
    if np.random.rand() < 0.4:
        cbar = fig.colorbar(im, ax=ax)

# 30% probability using sns.heatmap()
else:
    import seaborn as sns
    sns.heatmap(df, cmap='YlGn', ax=ax)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df.index)))
ax.set_yticklabels(df.index, rotation=0, ha='right')

# Set ticks and ticklabels in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=True)
ax.set_yticks(np.arange(len(df.index)) + 0.5, minor=True)
ax.tick_params(which='minor', bottom=False, left=False)

# Set title and labels
ax.set_title('Crop Production and Trade Statistics')
ax.set_xlabel('Metrics')
ax.set_ylabel('Crop')

# Automatically resize the image
fig.tight_layout()

# Save image
fig.savefig('output/final/heatmap/png/20231228-134212_41.png', bbox_inches='tight')

# Clear current image state
plt.clf() 