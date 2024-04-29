
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Museums Visited (Million)', 'Theaters Visited (Million)', 'Galleries Visited (Million)', 'Live Music Events (Million)']
data = np.array([[30, 40, 25, 20], 
                 [20, 25, 15, 10], 
                 [15, 20, 10, 5], 
                 [25, 35, 20, 15], 
                 [10, 15, 10, 5]])
x_values = ['USA', 'UK', 'France', 'Germany', 'Japan']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:, i], shade=True, color='lightsteelblue')

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_zlabel('Number of people (Million)')

plt.title('Arts and Culture Participation by Country - A Global Perspective')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/39_202312270030.png')

plt.clf()