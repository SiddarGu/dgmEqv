

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

data = {'Category': [1, 2, 3, 4, 5],
        'Painting': [20, 30, 40, 25, 15],
        'Sculpture': [10, 15, 20, 15, 10],
        'Dance': [5, 5, 10, 10, 5],
        'Film': [30, 25, 15, 20, 15],
        'Music': [15, 20, 20, 30, 20],
        'Theatre': [20, 15, 15, 25, 30]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 6))

sns.heatmap(df.set_index('Category'),
            annot=True,
            fmt='g',
            cmap='YlGnBu',
            linewidths=0.5,
            ax=ax)

ax.set_title('Popularity of Arts and Culture by Category')

plt.yticks(rotation=0)
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')

plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_96.png', bbox_inches='tight')

plt.clf()