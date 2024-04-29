
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Freight Carried (Million Tonnes)", "Total Revenue ($ Billion)", "Passengers Carried (Million)"]
data = np.array([[72.5,100,20.6], [19.2,90,10.5], [90,85,7.8], [45,12,19.2]])
x_values = ["Road", "Rail", "Air", "Sea"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros_like(data[:, i]), 1, 1, data[:, i], shade=True, color='b', alpha=0.5)

ax.set_xticks(xs)
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')
ax.tick_params(axis='x', rotation=45)
ax.view_init(30, -15)

ax.set_title('Transportation and Logistics - A Comprehensive Analysis')
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/27_202312251044.png")
plt.clf()