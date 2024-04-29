import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Preparing data
data = np.array([
    [2019, 3000, 2200, 40, 60],
    [2020, 2900, 2300, 39.5, 62],
    [2021, 2800, 2500, 39, 64],
    [2022, 2700, 2700, 38.5, 66],
    [2023, 2600, 2800, 38, 68]
], dtype=np.float32)

x_values = data[:, 0]
y_values = ['Greenhouse Gas Emissions (Million Tons)', 'Renewable Energy Consumption (Billion kWh)', 'Forest Area (Million sq. km)', 'Recycling Rate (%)']
data = data[:, 1:].T

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
for i in range(len(y_values)):
    ax.bar3d(x = np.arange(len(x_values)), y = [i]*len(x_values), z = np.zeros(len(x_values)), 
             dz = data[i], dx = 0.5, dy = 0.1, color = colors[i])

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticklabels(y_values, ha='left')

ax.set_xlabel('Year')
ax.set_title('Trends in Environment and Sustainability Metrics - 2019 to 2023', pad=30)

plt.grid(True)
ax.view_init(azim=-60, elev=30)
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/211_202312302235.png', dpi=300)
plt.clf()
