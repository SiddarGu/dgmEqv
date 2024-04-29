
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Painting', 'Photography', 'Sculpture', 'Music']
data = np.array([[50, 20, 30, 20], [40, 15, 25, 15], [45, 25, 35, 20], [30, 20, 10, 30]])
x_values = ['Art Galleries', 'Museums', 'Art Festivals', 'Concerts']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.4, 0.8, data[:, i], alpha=0.7, color='b')

ax.set_title('Arts and Culture in the Community - A Comparison')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.view_init(135, -15)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/43_202312251044.png')

plt.clf()