
import matplotlib.pyplot as plt
import numpy as np

y_values = ["Participants (Millions)", "Revenue ($ Billion)", "Growth Rate (%)"]
x_values = ["Live Sports", "Online Gaming", "Movies and TV", "Music", "Theme Parks"]
data = np.array([[2.7, 7, 3.2], [1.5, 5, 8.6], [2.2, 1, 2.4], [1.1, 2, 6.2], [0.7, 3, 4.8]])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(xs)), 0.4, 0.4, data[:,i], shade=True, alpha=.6)

ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_title('Sports and Entertainment: An Overview of Participants, Revenues, and Growth Rates')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/38_202312251044.png')
plt.clf()