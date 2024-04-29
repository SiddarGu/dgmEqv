
import matplotlib.pyplot as plt
import numpy as np

data = [[1000, 1200], [900, 1300], [1100, 1400], [800, 1500]]
states = ['New York','California','Texas','Florida']

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)
width = 0.35

x = np.arange(len(states))
rects1 = ax.bar(x, [row[0] for row in data], width, color='b')
rects2 = ax.bar(x + width, [row[1] for row in data], width, color='r')

ax.set_title('Retail and E-commerce sales in four states in 2021')
ax.set_ylabel('Sales (million)')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(states,rotation=90, wrap=True)
ax.legend((rects1[0], rects2[0]), ('Retail Sales', 'E-commerce Sales'))
plt.tight_layout()
plt.savefig('bar chart/png/336.png')
plt.clf()