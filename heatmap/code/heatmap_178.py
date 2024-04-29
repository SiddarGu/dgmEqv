
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {'Product': ['Laptops', 'Smartphones', 'Tablets', 'Desktops'],
        'Revenue ($)': [500, 750, 400, 600],
        'Profit Margin (%)': [15, 20, 18, 17],
        'Market Share (%)': [25, 30, 20, 35],
        'Production Costs ($)': [400, 600, 350, 500],
        'Sales Growth (%)': [10, 12, 8, 15],
        'Units Sold': [200, 300, 150, 250]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 8))

ax = sns.heatmap(df.iloc[:, 1:], annot=True, fmt='.0f', cmap='Blues', cbar=False, linewidths=1, linecolor='white')

ax.set_xticks(np.arange(0.5, 6, 1))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')

ax.set_yticks(np.arange(0.5, 4, 1))
ax.set_yticklabels(df['Product'], rotation=0, ha='center')

ax.set_title('Manufacturing and Production Metrics')

plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_32.png', bbox_inches='tight')

plt.clf()
plt.close()