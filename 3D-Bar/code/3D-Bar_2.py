import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') 

y_values = ['Football Attendance (Millions)','Cinema Attendance (Millions)','Music Concert Attendance (Millions)']
x_values = ['2019', '2020', '2021', '2022', '2023']
data = np.array([[4.2, 3.6, 2.5], [1.6, 2.8, 2.1], [2.2, 3.4, 2.3], [3.7, 3.9, 2.7], [4.3, 4.2, 3.2]])

for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i] * len(x_values)
    zpos = np.zeros(len(x_values))
    dx = np.ones(len(x_values))
    dy = np.ones(len(x_values))
    dz = data[:, i]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa', alpha=0.5)
    
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_zlabel('Attendance (Millions)')

plt.title('Sports and Entertainment Attendance Trends - 2019 to 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/13_202312251036.png')
plt.clf()