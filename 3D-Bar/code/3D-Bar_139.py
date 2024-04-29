
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Number of Students (K)','Average Grade','Average Tuition (k $)']
data = np.array([[3,3.5,2],[1,3.7,2.8],[5,3.9,3.5],[2,4.0,4]])
x_values = ['Undergraduate','Graduate','Doctorate','Post-Doctorate']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_pos = np.arange(len(x_values))
y_pos = np.arange(len(y_values))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)

for i in range(len(y_values)):
    xs = x_pos[i]
    ys = y_pos[i]
    zs = data[:,i]
    ax.bar3d(xs, ys, np.zeros_like(zs), 1, 1, zs, alpha = 0.5, color = '#FFC222')

ax.set_title("Education Level Comparison - Student Numbers, Average Grade, and Tuition")
ax.set_xlabel('Level of Education')
ax.w_xaxis.set_ticklabels(x_values, rotation = 30)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.set_ylabel('Metric')
ax.set_zlabel('Value')

ax.grid(b = True, which = 'major', axis = 'both', linestyle = '--', color = '#777777')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/34.png')
plt.clf()