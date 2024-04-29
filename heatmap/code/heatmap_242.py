
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {'Property': ['House 1', 'House 2', 'House 3', 'House 4', 'House 5'],
        'Sale Price (USD)': [500, 650, 800, 450, 700],
        'Rental Price (USD)': [1500, 1800, 2000, 1300, 1900],
        'Square Footage': [2000, 2100, 2400, 1500, 2200],
        'Number of Bedrooms': [4, 3, 5, 2, 4],
        'Number of Bathrooms': [3, 2, 4, 1, 3],
        'Year Built': [2015, 2010, 2018, 1995, 2005]
        }

df = pd.DataFrame(data)
df = df.set_index('Property')

fig, ax = plt.subplots(figsize=(10, 8))

heatmap = ax.imshow(df, cmap='coolwarm')

ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))

ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index)

ax.set_xticklabels(ax.get_xticklabels(), wrap=True)
ax.set_yticklabels(ax.get_yticklabels(), wrap=True)

ax.set_xticks(np.arange(len(df.columns))+0.5, minor=True)
ax.set_yticks(np.arange(len(df.index))+0.5, minor=True)

ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

ax.tick_params(which='minor', bottom=False, left=False)

cbar = plt.colorbar(heatmap)

plt.title('Real Estate Prices and Features')

plt.tight_layout()

plt.savefig('output/final/heatmap/png/20231228-155147_38.png', bbox_inches='tight')

plt.clf()