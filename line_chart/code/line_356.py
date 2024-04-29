
import matplotlib.pyplot as plt
import numpy as np

Year = np.array([2020, 2021, 2022, 2023])
YieldA = np.array([1000, 1200, 800, 1500])
YieldB = np.array([800, 900, 1100, 1200])
YieldC = np.array([1200, 1100, 1300, 1400])
YieldD = np.array([1500, 1600, 1200, 800])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

ax.plot(Year, YieldA, 'r--', label='Yield A')
ax.plot(Year, YieldB, 'b-.', label='Yield B')
ax.plot(Year, YieldC, 'g-', label='Yield C')
ax.plot(Year, YieldD, 'y:', label='Yield D')

ax.set_xlabel('Year')
ax.set_ylabel('Yield (ton)')
ax.set_title('Crop Yields in Four Different Regions in the U.S.')
ax.legend(loc='lower right', fontsize='large')
ax.set_xticks(Year)

plt.tight_layout()
plt.savefig('line chart/png/528.png')
plt.clf()