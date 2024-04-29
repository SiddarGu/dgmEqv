
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2001, 2002, 2003, 2004])
y1 = np.array([14000, 15500, 13000, 14500])
y2 = np.array([2.2, 3.3, 2.4, 1.6])

plt.figure(figsize=(10, 5))
plt.subplot()

plt.plot(x, y1, label='GDP')
plt.plot(x, y2, label='Inflation Rate')

plt.xticks(x)
plt.title('GDP and Inflation Rate of the US from 2001 to 2004')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend(loc='upper right')
plt.grid(axis='y')
for x, y1, y2 in zip(x, y1, y2):
    plt.annotate('GDP=%.1fB$\nInflation Rate=%.1f%%' % (y1, y2),xy=(x, y1), xytext=(-25, 10),
        textcoords='offset points',
        wrap=True,
        horizontalalignment='right',
        fontsize=10)

plt.tight_layout()
plt.savefig('line chart/png/475.png')
plt.clf()