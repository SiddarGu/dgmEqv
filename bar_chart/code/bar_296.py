
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8,6))
x = np.arange(4)
y1 = [1500, 1700, 2000, 1800]
y2 = [100000, 120000, 150000, 130000]
bar_width = 0.3
ax.bar(x, y1, width=bar_width, label='Tickets Sold')
ax.bar(x+bar_width, y2, width=bar_width, label='Total Revenue')
ax.set_xticks(x+bar_width/2)
ax.set_xticklabels(['Football Match', 'Basketball Game', 'Concert', 'Movie Premiere'], rotation=45, ha='right', wrap=True)
ax.set_title('Ticket sales and total revenue of four events in 2021')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('bar chart/png/342.png')
plt.clf()