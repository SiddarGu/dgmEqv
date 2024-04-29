
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Crop Production (Tons)': [350, 320, 400, 500, 280, 350],
        'Livestock Production (Tons)': [450, 400, 500, 600, 350, 450],
        'Fish Production (Tons)': [150, 100, 200, 250, 100, 150],
        'Vegetable Production (Tons)': [200, 180, 250, 300, 150, 200],
        'Fruit Production (Tons)': [100, 80, 120, 150, 70, 100],
        'Dairy Production (Tons)': [300, 250, 350, 400, 200, 300]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 7))
im = ax.imshow(df.iloc[:, 1:].values, cmap='Blues')

ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['Region'])))
ax.set_xticklabels(df.columns[1:])
ax.set_yticklabels(df['Region'])

plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
plt.setp(ax.get_yticklabels(), rotation=0)

plt.xlabel('Production Type')
plt.ylabel('Region')
ax.set_title('Agricultural Production by Region')

for i in range(len(df['Region'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j+1], ha='center', va='center', color='black', size=10)

plt.colorbar(im)
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_38.png', bbox_inches='tight')
plt.show()
plt.clf()