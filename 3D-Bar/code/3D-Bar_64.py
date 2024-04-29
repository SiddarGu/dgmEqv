
import numpy as np
import matplotlib.pyplot as plt

y_values = np.array(['CO2 Emission (Million Tonnes)', 'Energy Consumption (Million kWh)', 'Renewable Energy (%)'])
data = np.array([[50, 30, 20], [30, 20, 30], [20, 15, 25], [40, 30, 35]])
x_values = np.array(['North', 'South', 'East', 'West'])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.8, 0.6, data[:, i], color=[0.5, 0.3, 0.5, 0.8], shade=True, alpha=0.8)
ax.set_title("Environmental Sustainability - Regional Analysis")
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=-20)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/34_202312270030.png")
plt.clf()