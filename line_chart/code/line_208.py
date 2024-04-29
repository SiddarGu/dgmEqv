

import matplotlib.pyplot as plt
import numpy as np

Year = np.array([ 2021, 2022, 2023, 2024])
Sports_Revenue = np.array([1000, 1100, 1300, 1500])
Entertainment_Revenue = np.array([1200, 1300, 1400, 1600])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(Year, Sports_Revenue, color='r', marker='o', markersize=7, linewidth=2, label='Sports Revenue')
ax.plot(Year, Entertainment_Revenue, color='b', marker='^', markersize=7, linewidth=2, label='Entertainment Revenue')
ax.set_title('Annual Revenue Growth of Sports and Entertainment')
ax.set_xlabel('Year')
ax.set_ylabel('Revenue')
ax.legend(loc='upper left')
ax.grid(True)
ax.set_xticks(Year)
plt.tight_layout()
plt.savefig('line chart/png/110.png')
plt.clf()