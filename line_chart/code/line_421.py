
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020, 2021, 2022, 2023])
y1 = np.array([200, 220, 230, 240])
y2 = np.array([150, 160, 170, 180])
y3 = np.array([100, 120, 140, 160])
y4 = np.array([250, 270, 280, 290])

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y1, label='Produce', c='b', marker='o')
ax.plot(x, y2, label='Meat', c='r', marker='*')
ax.plot(x, y3, label='Dairy', c='g', marker='s')
ax.plot(x, y4, label='Beverages', c='m', marker='^')
ax.grid(True, linestyle='--')
ax.legend(loc='best')
ax.set_xticks(x)
ax.set_title("Yearly growth of food and beverage consumption in the US", fontsize=14)
plt.tight_layout()
plt.savefig('line chart/png/165.png')
plt.cla()