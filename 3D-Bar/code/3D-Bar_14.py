
import numpy as np
import matplotlib.pyplot as plt

y_values = ['CO2 Emission (MtCO2e)', 'Renewable Energy Production (TWh)', 'Energy Efficiency (MtCO2e/GDP)', 'Water Usage (billion cubic meters)']
data = np.array([[9700, 3000, 900, 800],
                [5100, 2000, 600, 400],
                [3900, 1000, 400, 200],
                [2600, 3000, 500, 100]])
x_values = ['China', 'USA', 'India', 'Russia']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Environmental Sustainability Comparison Across Countries')
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:, i], shade=True, color='orange')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
ax.tick_params(axis='x', rotation=45)
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/9.png')
plt.clf()