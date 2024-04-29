import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

content = '''Year,Soccer Matches Attendance (Million),Movie Box Office Revenue ($ Billion),Concerts Attendance (Million),Video Game Sales ($ Billion)
2018,40,40.4,30,135
2019,42,42.5,32,140
2020,20,20.3,15,158
2021,25,24.6,20,170'''

# processing data for plotting
lines = content.split('\n')
x_values = [line.split(',')[0] for line in lines[1:]]
y_values = lines[0].split(',')[1:]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines[1:]])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
for c, z, i in zip(colors, [30, 20, 10, 0], range(4)):
    xs = np.arange(len(x_values))
    ys = data[:, i]
    ax.bar(xs, ys, zs=z, zdir='y', color=c, alpha=0.8)

ax.set_xlabel('Year')
ax.set_ylabel('Metrics')
ax.set_zlabel('Values')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation = 45)
ax.set_yticklabels(y_values, ha='left')

ax.view_init(30, -35)

plt.title("Sports and Entertainment Industry Trends - 2018 to 2021")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/240_202312310050.png')
plt.clf()
