
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Unemployment Rate", "Average Income ($000)", "Poverty Rate (%)"]
data = np.array([[5,45,10], [7,35,15], [4,50,9], [6,40,17]])
x_values = ["North", "South", "East", "West"]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:,i], shade=True, color='b')

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
plt.title("Regional Public Policy and Economic Performance in the US")
ax.view_init(30, -15)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/28_202312251044.png")
plt.clf()