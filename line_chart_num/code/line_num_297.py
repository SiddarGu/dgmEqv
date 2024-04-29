
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,9)
y1 = [125.0, 150.5, 145.4, 135.2, 140.3, 146.8, 155.7, 145.3]
y2 = [87.5, 95.2, 95.3, 89.4, 95.2, 97.4, 105.1, 92.3]
y3 = [78.6, 83.1, 79.2, 73.5, 78.4, 82.1, 87.2, 79.4]

fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(111)

plt.plot(x, y1, label='Movie A(million dollars)', color='b', marker='o', markersize=8, linestyle='-')
plt.plot(x, y2, label='Movie B(million dollars)', color='r', marker='o', markersize=8, linestyle='-')
plt.plot(x, y3, label='Movie C(million dollars)', color='g', marker='o', markersize=8, linestyle='-')

plt.xticks(x, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'))
plt.title('Box office performance of three movies in the US from January to August 2020')
plt.xlabel('Month')
plt.ylabel('Box office performance (million dollars)')
plt.legend(loc='upper left')

for xy in zip(x, y1):
    ax.annotate('%s' % xy[1], xy=xy, textcoords='data')
for xy in zip(x, y2):
    ax.annotate('%s' % xy[1], xy=xy, textcoords='data')
for xy in zip(x, y3):
    ax.annotate('%s' % xy[1], xy=xy, textcoords='data')

ax.grid()
fig.tight_layout()

plt.savefig('line chart/png/345.png')
plt.clf()