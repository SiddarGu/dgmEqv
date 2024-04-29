import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
raw_data = "Year,Science Graduates (000s),Arts Graduates (000s),Commerce Graduates (000s),Engineering Graduates (000s)\n 2019,200,180,230,300\n 2020,210,190,240,320\n 2021,220,200,250,340\n 2022,235,210,265,360\n 2023,245,225,280,380"
lines = raw_data.split("\n")
header = lines[0].split(",")
data = np.array([list(map(np.float32, line.split(","))) for line in lines[1:]])
x_values = data[:, 0]
y_values = header[1:]
data = data[:, 1:]

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
colors = ['r', 'g', 'b', 'y']

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.8, data[:, i], color=colors[i])

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.view_init(elev=30., azim=-135)

plt.tight_layout()
plt.title('Graduation Trends in Different Academic Fields - 2019 to 2023')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/103_202312302126.png')
plt.clf()
