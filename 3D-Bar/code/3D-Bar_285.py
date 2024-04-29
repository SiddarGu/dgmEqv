import matplotlib.pyplot as plt
import numpy as np

data_string = "Year,Total Revenue (Million $),Gross Profit (Million $),Net Income (Million $)\n 2018,1892,768,382\n 2019,2100,826,408\n 2020,2245,900,448\n 2021,2425,976,499\n 2022,2690,1083,552"

data_lines = data_string.split("\n")
y_values = data_lines[0].split(",")[1:]
x_values = [line.split(",")[0] for line in data_lines[1:]]
data = np.array([list(map(np.float32, line.split(",")[1:])) for line in data_lines[1:]])

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111, projection='3d')

width = 0.2
colors = ['r', 'g', 'b']

for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i]*len(x_values)
    zpos = np.zeros(len(x_values))
    dx = np.ones(len(x_values)) * width
    dy = np.ones(len(x_values)) * width
    dz = data[:, i]
    color = colors[i]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=color, alpha=0.5)

ax.set_title('Financial Statistics of a Company from 2018 to 2022')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

plt.grid(True)

ax.view_init(elev=30., azim=-45)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/274_202312310050.png")
plt.clf()
