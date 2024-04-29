
import matplotlib.pyplot as plt
import numpy as np

data = [['USA',100,120],['UK',90,110],['Germany',80,95],['France',85,105]]

fig, ax = plt.subplots(figsize=(8,6))
ax.set_title('Number of sports and entertainment activities in four countries in 2021')

p1 = ax.bar(np.arange(4), [item[1] for item in data], width=0.3, label='Sports')
p2 = ax.bar(np.arange(4)+0.3, [item[2] for item in data], width=0.3, label='Entertainment')

ax.set_xticks(np.arange(4)+0.15)
ax.set_xticklabels([item[0] for item in data])
ax.legend(loc='best')

for i, v in enumerate(zip([item[1] for item in data], [item[2] for item in data])):
    ax.text(i-0.15, v[0]+20, str(v[0]), color='black', fontsize=10, rotation=90,
            ha='center', va='bottom', fontweight='bold')
    ax.text(i+0.15, v[1]+20, str(v[1]), color='black', fontsize=10, rotation=90,
            ha='center', va='bottom', fontweight='bold')

fig.tight_layout()
fig.savefig('Bar Chart/png/324.png')
plt.close()