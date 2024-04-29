
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Number of Cases Filed (Thousands)', 'Number of Cases Settled (Thousands)', 'Number of Cases in Process (Thousands)']
data = np.array([[400, 300, 100], [350, 250, 150], [450, 300, 150], [500, 350, 100]])
x_values = ['North', 'South', 'East', 'West']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(3):
    xpos = np.arange(len(x_values))
    ypos = [i] * len(x_values)
    dx = 0.5
    dy = 0.5
    dz = data[:, i]
    ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, dy, dz, color=['red','blue', 'green', 'purple'], alpha=0.5)
    ax.set_xticks(xpos)
    ax.set_xticklabels(x_values, rotation=15)
    ax.set_yticklabels(y_values)

plt.tight_layout()
plt.title('Regional Analysis of Law and Legal Affairs Cases - 2019')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/37.png')
plt.clf()