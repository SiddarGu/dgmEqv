
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2001, 2002, 2003, 2004])
y1 = np.array([2000, 2200, 2500, 2100])
y2 = np.array([1400, 1600, 2000, 1800])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

ax.plot(x, y1, color='blue', linewidth=2, label="Number of crimes reported")
ax.plot(x, y2, color='red', linewidth=2, label="Number of convictions")

ax.set_title('Crime reports and convictions in the US from 2001 to 2004', fontsize=20)
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('Number', fontsize=16)
ax.set_xticks(x)

ax.grid(True, linestyle='-.', color='gray', alpha=0.4)
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/133.png')
plt.clf()