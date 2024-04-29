
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

x = np.array([2015, 2016, 2017, 2018])
y1 = np.array([20, 30, 25, 35])
y2 = np.array([18, 20, 25, 30])
y3 = np.array([15, 20, 25, 30])
y4 = np.array([30, 35, 30, 40])

ax.plot(x, y1, '-', label='Football Team A')
ax.plot(x, y2, '--', label='Football Team B')
ax.plot(x, y3, '-.', label='Baseball Team A')
ax.plot(x, y4, ':', label='Baseball Team B')

plt.title('Performance comparison between Football and Baseball teams in 2015-2018')
plt.xlabel('Year')
plt.ylabel('Performance')
plt.xticks(x)

for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y3):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y4):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

ax.legend(loc='best')
plt.tight_layout()

plt.savefig('line chart/png/64.png')
plt.clf()