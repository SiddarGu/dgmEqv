
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Attendance (Millions)', 'Tickets Sold (Millions)', 'Revenue ($Billion)']
x_values = ['Soccer Stadium', 'Baseball Stadium', 'Basketball Stadium', 'Hockey Stadium']
data = np.array([[2.5, 10, 3.5], [3, 8, 3.2], [4.5, 7, 3.7], [2.7, 9, 3.6]])

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:, i], shade=True, alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_xlabel('Sports and Entertainment Industry')
ax.view_init(elev=15, azim=20)
plt.tight_layout()
plt.title('Sports and Entertainment Industry Performance Overview')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/37_202312251044.png')
plt.clf()