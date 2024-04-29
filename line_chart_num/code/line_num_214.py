
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020, 2021, 2022, 2023])
y1 = np.array([800, 900, 1000, 1100])
y2 = np.array([1200, 1100, 1300, 1400])
y3 = np.array([2000, 2000, 2300, 2500])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.set_title('Online and Store Sales in the Retail Industry from 2020 to 2023')
ax.set_xlabel('Year')
ax.set_ylabel('Sales (billion dollars)')
ax.plot(x, y1, color='r', label='Online Sales')
ax.plot(x, y2, color='b', label='Store Sales')
ax.plot(x, y3, color='g', label='Total Sales')
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.02))
ax.grid(True, linestyle='--', color='grey', linewidth=0.3)

for a, b, c, d in zip(x, y1, y2, y3):
    ax.annotate('%.0f' % d, xy=(a, d), xytext=(a-0.2, d-150), size=10)
ax.set_xticks(x)
plt.tight_layout()
plt.savefig('line chart/png/176.png')
plt.clf()