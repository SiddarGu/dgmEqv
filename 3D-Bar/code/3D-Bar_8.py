
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Headcount', 'Average Salary ($)', 'Average Vacation Days']
x_values = ['Interns', 'Full-Time', 'Part-Time', 'Contractors', 'Remote']

data = np.array([[45,22,27],
                 [40,50,14],
                 [15,20,37],
                 [25,40,45],
                 [20,45,14]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], alpha=0.6, color='#2196F3')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
ax.set_title('HR and Employee Management Insights by Type')

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/18_202312251044.png')
plt.clf()