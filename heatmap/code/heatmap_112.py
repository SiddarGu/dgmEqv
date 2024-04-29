
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {'League': ['NFL', 'NBA', 'MLB', 'NHL', 'MLS'],
        'Viewership (Millions)': [120, 100, 80, 50, 30],
        'Tickets Sold (Millions)': [5, 10, 7, 3, 2],
        'Merchandise Sales (Millions)': [200, 150, 100, 80, 50],
        'TV Rights Revenue (Millions)': [300, 200, 150, 100, 80],
        'Sponsorship Revenue (Millions)': [400, 300, 200, 100, 50]}

df = pd.DataFrame(data)
df.set_index('League', inplace=True)

fig, ax = plt.subplots(figsize=(10, 6))

cmap = plt.get_cmap('Reds')
im = ax.imshow(df, cmap=cmap)

ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

ax.xaxis.tick_top()
plt.setp(ax.get_xticklabels(), rotation=45, ha='left', rotation_mode='anchor')
plt.setp(ax.get_yticklabels(), rotation=0, ha='right', rotation_mode='anchor')

for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j],
                       ha='center', va='center', color='black')

cbar = ax.figure.colorbar(im, ax=ax, shrink=0.5)
cbar.ax.set_ylabel('Revenue (Millions)', rotation=-90, va='bottom')

ax.set_title('Revenue Breakdown by League in Sports')

fig.tight_layout()

plt.savefig('output/final/heatmap/png/20231228-131639_13.png', bbox_inches='tight')

plt.clf()