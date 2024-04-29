
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2021, 2022, 2023, 2024, 2025])
y1 = np.array([100, 120, 150, 180, 200])
y2 = np.array([10, 20, 30, 40, 50])

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot()
ax1.plot(x, y1, label='Orders', color='red', linewidth=3)
ax1.plot(x, y2, label='Returns', color='blue', linewidth=3)

ax2 = ax1.twinx()
ax2.plot(x, (y1 - y2), label='Net Orders', color='green', linestyle="--", linewidth=3)

ax1.set_title('Net Orders in the Retail and E-commerce Industry from 2021 to 2025')
ax1.set_xlabel('Year')
ax1.set_ylabel('Orders/Returns')
ax2.set_ylabel('Net Orders')

ax1.grid(linestyle='--', linewidth='0.5', color='gray')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.set_xticks(x)

for i,j in zip(x,(y1-y2)):
    ax2.annotate(str(j), xy=(i,j+2))

plt.tight_layout()
plt.savefig('line chart/png/519.png')
plt.clf()