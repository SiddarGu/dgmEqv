
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data processing
data = pd.DataFrame({'Crop Type': ['Wheat', 'Corn', 'Soybeans', 'Rice'],
                     'Yield per Hectare (Bushels)': [70, 120, 80, 50],
                     'Percentage of Total Production': [25, 40, 20, 10]})
# Setting figure size and title
plt.figure(figsize=(12, 8))
plt.title('Crop Production and Trade in Agriculture')

# Plotting heatmap
ax = sns.heatmap(data[['Yield per Hectare (Bushels)', 'Percentage of Total Production']].transpose(),
                 cmap='YlGnBu',
                 annot=True,
                 fmt='g')

# Setting ticks and tick labels
ax.set_xticks(np.arange(0.5, 4.5, 1))
ax.set_yticks(np.arange(0.5, 2.5, 1))
ax.set_xticklabels(data['Crop Type'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(['Yield per Hectare (Bushels)', 'Percentage of Total Production'])

# Adding colorbar
# plt.colorbar(ax.collections[0])

# Automatically resizing image
plt.tight_layout()

# Saving image
plt.savefig('output/final/heatmap/png/20231228-134212_58.png', bbox_inches='tight')

# Clearing current image state
plt.clf()