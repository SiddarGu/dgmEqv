
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 8))
plt.title('Energy consumption in the US from 2020 to 2024')

x = np.arange(2020, 2025)
y1 = np.array([1000, 1200, 1400, 1600, 1800])
y2 = np.array([3000, 2800, 2600, 2400, 2200])

ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y1, color='#FF1493', label='Renewable Energy(GWh)',linestyle='-')
ax.plot(x, y2, color='#87CEFA', label='Non-Renewable Energy(GWh)',linestyle='-')
ax.legend(loc='best')

for a, b in zip(x, y1):
    plt.text(a, b + 0.2, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y2):
    plt.text(a, b + 0.2, b, ha='center', va='bottom', fontsize=10)

plt.xticks(x) 
plt.tight_layout()
plt.savefig('line chart/png/496.png')
plt.clf()