
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

x = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'])
y1 = np.array([100, 120, 140, 180, 160, 200, 220, 190])
y2 = np.array([80, 90, 100, 150, 140, 170, 190, 160])

ax.plot(x, y1, label='Number of Cases Opened', linewidth=2, color='r')
ax.plot(x, y2, label='Number of Cases Closed', linewidth=2, color='b')

plt.title('U.S. Court Cases in 2021', fontsize=18)
ax.set_xlabel('Month', fontsize=16)
ax.set_ylabel('Number of Cases', fontsize=16)

ax.set_xticks(x)
ax.set_xticklabels(x, rotation=45, fontsize=14)

plt.legend(loc='upper left', fontsize=14)
plt.grid(linestyle='--')

plt.tight_layout()
plt.savefig('line chart/png/355.png')
plt.clf()