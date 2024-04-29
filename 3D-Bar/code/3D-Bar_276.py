import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

data = """Year,Website Traffic (Million),Number of Downloads (Million),Online Sales Revenue ($ Million)
2018,35,50,100
2019,50,80,180
2020,70,100,220
2021,90,150,300
2022,120,200,400"""

# Splitting the data
lines = data.split("\n")
header = lines[0].split(',')
lines = lines[1:]

x_values = []
y_values = header[1:]
z_values = []
for line in lines:
    elements = line.split(',')
    x_values.append(elements[0])
    z_values.append(list(map(np.float32, elements[1:])))
    
z_values = np.array(z_values)

# Creating 3D bar chart
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.25, 0.5, z_values[:, i], alpha=0.5, color=colors[i])

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=50)
ax.set_yticklabels(y_values, ha='left')
ax.set_zlabel('Values')
ax.set_title('Internet Usage and Online Business Trends - 2018 to 2022')

plt.gca().invert_xaxis()
ax.view_init(30, -50)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/199_202312302235.png')
plt.clf()
