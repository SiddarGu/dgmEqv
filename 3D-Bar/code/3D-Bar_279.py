import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# parsing the given data
data_str = """Year,Concert Attendance (Millions),Movie Box Office Revenue ($ Billion),Sporting Event Attendance (Millions)
2019,30,45,35
2020,15,25,20
2021,20,35,25
2022,25,40,30
2023,30,45,35 """

lines = data_str.split("\n")
y_values = lines[0].split(",")[1:]
x_values = [line.split(",")[0] for line in lines[1:]]
data = np.array([list(map(float, line.split(",")[1:])) for line in lines[1:]], dtype=np.float32)

# figure creation
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

# bar attributes
width = 0.5
depth = 0.5
colors = ['r', 'g', 'b']
alpha = 0.7

# plotting each column
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
              width, depth, data[:, i], color=colors[i], alpha=alpha)

# setting x, y labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation = 15)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# setting chart title and viewing angle
plt.title('Sports and Entertainment Industry Overview - 2019 to 2023') 
ax.view_init(elev=20, azim=-70)

# grid
ax.grid(True)

# save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/105_202312302126.png')
plt.clf()
