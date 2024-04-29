
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {'Field': ['Energy', 'Materials', 'Robotics', 'Nanotechnology', 'Biomedical'],
        'Physics': [12, 8, 5, 10, 6],
        'Biology': [6, 15, 8, 12, 20],
        'Chemistry': [10, 10, 10, 5, 15],
        'Computer Science': [8, 5, 15, 8, 10],
        'Engineering': [15, 12, 20, 10, 8]}

df = pd.DataFrame(data)
df = df.set_index('Field')

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(df, annot=True, cmap='YlGnBu', linewidths=0.5, ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
ax.tick_params(axis='both', which='both', length=0, labelsize=12)
ax.set_title('Interdisciplinary Research in STEM Fields', fontsize=16)
ax.set_xlabel('Fields', fontsize=14)
ax.set_ylabel('Research Areas', fontsize=14)
fig.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-163105_25.png', bbox_inches='tight')
plt.clf()