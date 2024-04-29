

import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 20000, 50000, 100000],
        ['Canada', 15000, 45000, 80000],
        ['Mexico', 18000, 48000, 95000],
        ['Brazil', 30000, 60000, 110000]]

x = np.arange(len(data))

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1, 1, 1)
ax.bar(x, [i[1] for i in data], color='#ff0090', label='Crops')
ax.bar(x, [i[2] for i in data], bottom=[i[1] for i in data], color='#0090ff', label='Fruits')
ax.bar(x, [i[3] for i in data], bottom=[i[1]+i[2] for i in data], color='#90ff00', label='Vegetables')
ax.set_xticks(x)
ax.set_xticklabels([i[0] for i in data])
ax.set_title("Total Production of Crops, Fruits and Vegetables in Four Countries in 2021")
ax.legend(loc='upper left')
for i, v in enumerate(data):
    ax.text(i - 0.2, v[1]/2, str(v[1]), color='#ff0090', fontweight='bold')
    ax.text(i - 0.2, v[1] + v[2]/2, str(v[2]), color='#0090ff', fontweight='bold')
    ax.text(i - 0.2, v[1] + v[2] + v[3]/2, str(v[3]), color='#90ff00', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/163.png')
plt.clf()