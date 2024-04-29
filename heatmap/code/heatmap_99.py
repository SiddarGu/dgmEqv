

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import seaborn as sns

data = {'Category': ['Energy Research', 'Space Exploration', 'Biomedical Engineering', 'Nanotechnology', 'Materials Science'], '2010 (billion)': [10.5, 8, 6, 4, 3], '2011 (billion)': [12, 9, 7, 5, 4], '2012 (billion)': [13.2, 10, 8, 6, 5], '2013 (billion)': [14.5, 11, 9, 7, 6], '2014 (billion)': [16, 12, 10, 8, 7], '2015 (billion)': [18, 14, 11, 9, 8]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 8))

plt.imshow(df.iloc[:, 1:], cmap='YlOrRd', aspect='auto')

ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Category'])))

ax.set_xticklabels(df.columns[1:], ha='right', rotation=45, rotation_mode='anchor')
ax.set_yticklabels(df['Category'], wrap=True, ha='right', rotation=0, rotation_mode='anchor')

ax.set_xlabel('Fiscal Year')
ax.set_ylabel('Category')

ax.tick_params(axis='x', which='major', pad=10)
ax.tick_params(axis='y', which='major', pad=10)

ax.set_title('Funding for Science and Engineering Research')

for i in range(len(df['Category'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j+1], ha='center', va='center', color='w')

# sns.heatmap(df.iloc[:, 1:], cmap='YlOrRd', annot=True, fmt='.1f', cbar=False)

fig.colorbar(plt.imshow(df.iloc[:, 1:], cmap='YlOrRd', aspect='auto'))

# plt.savefig('output/final/heatmap/png/20231228-130949_0.png', bbox_inches='tight')
# plt.tight_layout()
# plt.savefig('output/final/heatmap/png/20231228-130949_0.png', bbox_inches='tight')
plt.savefig('output/final/heatmap/png/20231228-130949_0.png', bbox_inches='tight')

plt.clf()