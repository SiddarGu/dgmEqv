import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = """Year,Number of Bachelor's Degrees Awarded,Number of Master's Degrees Awarded,Number of Doctoral Degrees Awarded
2019,2000000,800000,180000
2020,2100000,850000,200000
2021,2150000,900000,220000
2022,2200000,950000,240000
2023,2250000,1000000,260000"""

lines = data.split('\n')
y_values = lines[0].split(",")[1:]
x_values = [line.split(",")[0] for line in lines[1:]]
data = np.array([list(map(np.float32, line.split(",")[1:])) for line in lines[1:]])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

bar_colors = ['b', 'r', 'g']
for c, k in zip(bar_colors, range(data.shape[1])):
    ax.bar3d(np.arange(len(x_values)), [k]*len(x_values), np.zeros_like(data[:, k]), 
              0.2, 0.5, data[:, k], color=c, alpha=0.5)

ax.set_xlabel('Year')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
plt.title('Trends in Higher Education Degrees Awarded - 2019 to 2023')
plt.grid(True)
ax.view_init(elev=20, azim=-35)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/259_202312310050.png")
plt.clf()
