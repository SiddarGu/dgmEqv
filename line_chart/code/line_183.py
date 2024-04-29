
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 6))

x = np.array([2011, 2012, 2013, 2014, 2015, 2016])
y1 = np.array([30, 20, 15, 10, 8, 5])
y2 = np.array([5, 15, 25, 35, 45, 50])

plt.plot(x, y1, label='Desktop Usage', linewidth=2)
plt.plot(x, y2, label='Mobile Usage', linewidth=2)

plt.xticks(x)
plt.title('Computer and Mobile Usage from 2011-2016')
plt.xlabel('Year')
plt.ylabel('Usage')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/50.png')

plt.clf()