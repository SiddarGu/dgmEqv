

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({'Year': [2018, 2019, 2020, 2021, 2022], 'Number of Laws Passed': [150, 200, 250, 300, 350], 'Number of Legal Cases Filed': [100, 150, 200, 250, 300], 'Number of Lawyers Employed': [200, 250, 300, 350, 400]})

df.iloc[:, 0] = df.iloc[:, 0].astype(str)

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], colors=['#fbb4ae', '#b3cde3', '#ccebc5'], alpha=0.8)
ax.grid(linestyle='dotted', color='#cbcbcb')

max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100

ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_ylim(0, max_total_value)

ax.set_ylabel('Number of Laws/Legal Cases/Lawyers Employed')

ax.set_xticks(np.arange(len(df.iloc[:, 0])))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

ax.legend(labels=['Laws Passed', 'Legal Cases Filed', 'Lawyers Employed'], loc='upper left')
ax.set_title('Legal Activity Trends')

fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-103019_13.png', bbox_inches='tight')