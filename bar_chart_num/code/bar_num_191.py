
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
data = [[200,250],[180,220],[210,260],[190,230]]
stores = ['Store A', 'Store B', 'Store C', 'Store D']
online = [x[0] for x in data]
store = [x[1] for x in data]
width = 0.3
ax.bar(np.arange(len(data)), online, width, label='Online Sales(million)')
ax.bar(np.arange(len(data)) + width, store, width, label='Store Sales(million)')
ax.set_title('Online and Store Sales of Four Stores in 2021')
ax.set_xticks(np.arange(len(data)) + width / 2)
ax.set_xticklabels(stores)
ax.legend(loc='best')
for i, v in enumerate(data):
    ax.text(i - .2, v[0] + 10, str(v[0]), color='blue')
    ax.text(i + .15, v[1] + 10, str(v[1]), color='orange')
fig.tight_layout()
fig.savefig('Bar Chart/png/568.png')
plt.cla()