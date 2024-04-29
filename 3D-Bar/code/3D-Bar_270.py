
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Social Media Usage (%)', 'Web Usage (%)', 'Time Spent (Hours)']
data = np.array([[80, 90, 4.2], [82, 92, 4.3], [75, 85, 3.9], [77, 87, 4.0]])
x_values = ['North', 'South', 'East', 'West']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for i, y in enumerate(y_values):
    X = np.arange(len(x_values))
    Y = np.ones(len(x_values)) * i
    dx = 0.5
    dy = 0.5
    dz = data[:,i]
    ax.bar3d(X, Y, np.zeros(len(x_values)), dx, dy, dz, alpha=0.5, color=plt.cm.tab10(i))

ax.set_xlabel('Region')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_title('Social Media and Web Usage by Region')
ax.grid(b=True, which='major', color='k', linestyle='-')
ax.view_init(30, -15)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/32.png')
plt.cla()