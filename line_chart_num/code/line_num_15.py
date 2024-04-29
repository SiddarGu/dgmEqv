
import matplotlib.pyplot as plt
import numpy as np

country = ['China', 'Japan', 'Thailand', 'Malaysia', 'Singapore']
visitor = [100, 80, 50, 30, 20]
revenue = [500, 350, 200, 150, 100]

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(1, 1, 1)
ax.plot(country, visitor, marker='o', label='Number of Visitor (millions)', color='green')
ax.plot(country, revenue, marker='*', label='Tourism Revenue (billion dollars)', color='red')
ax.legend(loc='upper left', fontsize='large')
ax.set_title('Visitor and Revenue of Popular Tourist Destinations in Asia in 2021', fontsize='xx-large')
ax.set_xticks(np.arange(len(country)))
ax.set_xticklabels(country, fontsize='large', rotation=30, ha='right', wrap=True)
ax.grid(True, linestyle='--', linewidth=1, alpha=0.3)
for x, y, z in zip(country, visitor, revenue):
    ax.annotate(f'{y}/{z}', (x, y), xytext=(-15, 10), textcoords='offset points', fontsize='large', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))
for x, y, z in zip(country, visitor, revenue):
    ax.annotate(f'{y}/{z}', (x, z), xytext=(-15, 10), textcoords='offset points', fontsize='large', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))

plt.tight_layout()
plt.savefig('line chart/png/600.png')
plt.clf()