
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = [['USA', 200, 450], ['UK', 300, 500], ['Germany', 220, 400], ['France', 230, 470]]
df = pd.DataFrame(data, columns = ['Country', 'Law Enforcement Expenditure', 'Education Expenditure'])

fig, ax = plt.subplots(figsize=(10,6))
bar_width = 0.35
x = np.arange(len(df))
ax.bar(x - bar_width/2, df['Law Enforcement Expenditure'], bar_width, label='Law Enforcement')
ax.bar(x + bar_width/2, df['Education Expenditure'], bar_width, label='Education')

ax.set_title('Government Expenditure on Law Enforcement and Education in Four Countries 2021')
ax.set_xticks(x)
ax.set_xticklabels(df['Country'], rotation=45)
ax.legend(loc='upper left')

for i, v in enumerate(df['Law Enforcement Expenditure']):
    ax.text(i-.25, v-10, str(v), color='white', fontweight='bold')

for i, v in enumerate(df['Education Expenditure']):
    ax.text(i+.15, v-10, str(v), color='white', fontweight='bold')

plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('Bar Chart/png/618.png')
plt.clf()