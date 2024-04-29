
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame({'Category': ['Personal Injury', 'Employment', 'Intellectual Property', 'Corporate', 'Real Estate', 'Criminal Defense', 'Family Law', 'Immigration', 'Environmental', 'Tax', 'Civil Rights', 'Bankruptcy'],
                   'Legal Cases Filed': [100, 150, 200, 250, 100, 150, 180, 200, 100, 250, 150, 100],
                   'Legal Cases Won': [50, 100, 180, 200, 80, 100, 150, 180, 50, 200, 120, 80],
                   'Legal Cases Settled': [30, 50, 100, 150, 50, 80, 100, 100, 30, 100, 70, 50],
                   'Legal Cases Lost': [20, 20, 20, 50, 20, 20, 30, 20, 20, 50, 20, 20]})
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10) * 10
y_ticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

fig, ax = plt.subplots(figsize=(12, 6))

ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.iloc[:, 0], colors=['#0f4c75', '#3282b8', '#bbe1fa', '#fcbf1e'], alpha=0.8)

ax.set_xlabel('Categories', fontsize=12)
ax.set_ylabel('Legal Cases', fontsize=12)
ax.set_title('Legal Cases Analysis by Category', fontsize=14)

ax.set_xticks(df.index)
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticks)

ax.set_xlim(0, len(df.index)-1)
ax.set_ylim(0, max_total_value)

ax.grid(color='#dfe6e9', alpha=0.5)

ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Categories')

fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-155112_1.png', bbox_inches='tight')

plt.close(fig)