
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 5))

x = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008])
y1 = np.array([5000, 6000, 7000, 8000, 9000, 10000, 11000, 9500])
y2 = np.array([200, 220, 250, 280, 300, 330, 360, 320])

plt.plot(x, y1, color='#2A6EA6', linestyle='-', marker='o', label='Number of Houses Sold')
plt.plot(x, y2, color='#FFA933', linestyle='-', marker='o', label='Median Prices(thousand dollars)')

plt.title('Evolution of the Real Estate Market in the US from 2001 to 2008', fontsize=12, fontweight='bold')
plt.xlabel('Year', fontsize=10)
plt.ylabel('Number of Houses Sold/Median Prices(thousand dollars)', fontsize=10)
plt.xticks(x, fontsize=10, rotation=45)
plt.legend(frameon=False, loc='upper left')
plt.tight_layout()

plt.savefig('line chart/png/544.png', dpi=300)
plt.clf()