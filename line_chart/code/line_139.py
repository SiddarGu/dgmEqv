
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[323.1, 19.39],
                [1409.4, 12.24],
                [1379.3, 2.72],
                [126.8, 4.98],
                [65.3, 2.83],
                [66.99, 2.77],
                [82.8, 3.69]])

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(1, 1, 1)

ax.plot(data[:, 0], data[:, 1], color='red', marker='o', linewidth=2, label='GDP')

ax.set_xlabel('Population (million people)', fontsize=12, fontweight='bold')
ax.set_ylabel('GDP (billion dollars)', fontsize=12, fontweight='bold')
ax.set_title('Population and GDP of Major Countries in 2019', fontsize=14)
ax.legend(loc='best')
ax.set_xticks(data[:, 0])
ax.tick_params(axis='both', labelsize=10)
ax.xaxis.set_tick_params(rotation=30)

plt.tight_layout()
plt.savefig('line chart/png/264.png')
plt.clf()