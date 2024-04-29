
import matplotlib.pyplot as plt
import numpy as np

y_values =  ['Hundred Number of Employees', 'Average Salary ($)', 'Number of Job Openings']
data = np.array([[10,15,20], [11,30,25], [12,30,30], [13,34,35], [14,35,40]])
x_values = ['2019', '2020', '2021', '2022', '2023']

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

width = depth = 0.8
colors = ['b', 'g', 'r']

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), width, depth, data[:, i], shade=True, color=colors[i])

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
plt.title('Human Resources Trends - Employee Management and Salary Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/6_202312270030.png')
plt.clf()