
import matplotlib.pyplot as plt
import numpy as np

data = {'Country': ['USA', 'UK', 'Germany', 'France'],
        'Manufacturing': [1000, 900, 1100, 800],
        'Agriculture': [1200, 1300, 1400, 1500],
        'Services': [800, 1100, 1200, 1400]}

fig, ax = plt.subplots(figsize=(10,6))
x_pos = np.arange(len(data['Country']))
width = 0.2

ax.bar(x_pos, data['Manufacturing'], width, label='Manufacturing', color='blue')
ax.bar(x_pos + width, data['Agriculture'], width, label='Agriculture', color='green')
ax.bar(x_pos + 2 * width, data['Services'], width, label='Services', color='red')

for i, v in enumerate(data['Manufacturing']):
    ax.text(i-0.1, v+20, str(v), color='black', fontweight='bold')

for i, v in enumerate(data['Agriculture']):
    ax.text(i-0.1 + width, v+20, str(v), color='black', fontweight='bold')

for i, v in enumerate(data['Services']):
    ax.text(i-0.1 + 2 * width, v+20, str(v), color='black', fontweight='bold')

plt.title('Economic contributions of Manufacturing, Agriculture and Services in four countries in 2021')
ax.set_xticks(x_pos + width)
ax.set_xticklabels(data['Country'])
ax.legend()
ax.grid()
plt.tight_layout()
plt.savefig('Bar Chart/png/107.png')
plt.clf()