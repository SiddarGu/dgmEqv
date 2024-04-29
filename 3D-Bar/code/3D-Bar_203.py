
import numpy as np
import matplotlib.pyplot as plt

y_values = ['New Employees (Number)', 'Retention Rate (%)', 'Training Hours (Hours)']
x_values = ['HR', 'IT', 'Accounting', 'Sales', 'Marketing']
data = np.array([[50, 75, 250], 
                [60, 80, 300],
                [40, 90, 200],
                [80, 85, 350],
                [90, 70, 400]])

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, [0]*len(x_values), 0.9, 0.9, data[:, i], 
            shade=True, color=['#00BFFF', '#FA8072', '#FFD700', '#2E8B57', '#FF1493'],
            alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_title('Human Resources and Employee Management Overview')
# plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/26_202312270030.png')
plt.clf()