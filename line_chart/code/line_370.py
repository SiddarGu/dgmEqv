
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2001, 2002, 2003, 2004, 2005])
y1 = np.array([3000, 3500, 3700, 3200, 4000])
y2 = np.array([4500, 5000, 5800, 4700, 5200])
y3 = np.array([1400, 1600, 1400, 1200, 1500])

fig, ax = plt.subplots(figsize=(8,6))

ax.plot(x, y1, '-o', label='Criminal Cases')
ax.plot(x, y2, '-o', label='Civil Cases')
ax.plot(x, y3, '-o', label='Family Cases')

plt.title('Trend of Legal Cases in the US from 2001 to 2005')
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.xticks(x)
ax.legend(bbox_to_anchor=(1.05,1), loc='upper left', borderaxespad=0.)
plt.tight_layout()
plt.savefig('line chart/png/517.png')
plt.clf()