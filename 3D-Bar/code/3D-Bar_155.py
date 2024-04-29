import numpy as np
import matplotlib.pyplot as plt

data = """Department,Number of Employees,Training Hours,Average Annual Salary($)
Sales,150,120,700
Production,220,100,650
IT,110,140,850
HR,50,150,750
Marketing,90,130,720"""

lines = data.split("\n")
y_values = lines[0].split(",")
x_values = [line.split(",")[0] for line in lines[1:]]
data = np.array([[np.float32(value) for value in line.split(",")[1:]] for line in lines[1:]])

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(projection='3d')

colors = ['red', 'green', 'blue']
width_depth = [0.3, 0.4, 0.5]

for i in range(data.shape[1]):
    x = np.arange(len(x_values))
    y = [i]*len(x_values)
    z = np.zeros(len(x_values))
    dx = np.ones(len(x_values))*width_depth[i]
    dy = np.ones(len(x_values))*0.2
    dz = data[:, i]
    ax.bar3d(x, y, z, dx, dy, dz, color=colors[i])

ax.set_xlabel('Departments')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values[1:])))
ax.set_yticklabels(y_values[1:], ha='left')

plt.title('Analysis of Employee Management in Different Departments')
plt.grid(True)
ax.view_init(elev=20, azim=-45)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/250_202312310050.png')
plt.clf()
