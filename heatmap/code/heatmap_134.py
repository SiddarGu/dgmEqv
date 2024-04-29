
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
    'Category': ['Visual Arts', 'Music', 'Theatre', 'Dance', 'Film', 'Literature', 'Architecture', 'Photography', 'Design', 'Fashion'],
    'Exhibitions': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Performances': [15, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Concerts': [10, 35, 40, 45, 50, 55, 60, 65, 70, 75],
    'Museums': [25, 40, 45, 50, 55, 60, 65, 70, 75, 80],
    'Theatres': [30, 45, 50, 55, 60, 65, 70, 75, 80, 85],
    'Galleries': [20, 50, 55, 60, 65, 70, 75, 80, 85, 90]
}


df = pd.DataFrame(data)
df = df.set_index('Category')

fig, ax = plt.subplots(figsize=(10,10))
heatmap = ax.pcolor(df, cmap='YlGn')
ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=False)
ax.invert_yaxis()

ax.set_xticklabels(df.columns, rotation=45, ha='right')
ax.set_yticklabels(df.index, rotation=0)
ax.set_xlabel('Events', labelpad=20)
ax.set_ylabel('Category', labelpad=20)

cbar = fig.colorbar(heatmap)
cbar.set_label('Number of Events', labelpad=20)

plt.title('Arts and Culture Events by Category')

plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_40.png', bbox_inches='tight')

plt.clf()