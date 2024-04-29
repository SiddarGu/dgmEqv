

import matplotlib.pyplot as plt
import numpy as np

data = [['North America', 20000, 30000, 25000],
        ['South America', 21000, 32000, 27000],
        ['Europe', 22000, 33000, 28000],
        ['Asia', 23000, 34000, 29000]]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

x_labels = [i[0] for i in data]
x_pos = np.arange(len(x_labels))

ax.bar(x_pos, [i[1] for i in data], label='Wind Energy', color='#FFC222')
ax.bar(x_pos, [i[2] for i in data], bottom=[i[1] for i in data], label='Solar Energy', color='#F07818')
ax.bar(x_pos, [i[3] for i in data], bottom=[i[1] + i[2] for i in data], label='Hydro Energy', color='#43C6DB')

ax.set_title('Renewable energy output in four regions in 2021')
ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels, rotation=30)
ax.legend(loc='upper left')

for i in range(len(data)):
    ax.annotate('{:.0f}'.format(data[i][1]), xy=(x_pos[i], data[i][1] + 500), ha='center')
    ax.annotate('{:.0f}'.format(data[i][2]), xy=(x_pos[i], data[i][1] + data[i][2] + 500), ha='center')
    ax.annotate('{:.0f}'.format(data[i][3]), xy=(x_pos[i], data[i][1] + data[i][2] + data[i][3] + 500), ha='center')

plt.tight_layout()
plt.savefig('Bar Chart/png/158.png')
plt.clf()