import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = "Year,Theatre Attendance (Million),Museum Visitors (Million),Music Festival Attendees (Million),Art Exhibition Visitors (Million)/n 2018,15,18,20,25/n 2019,14,19,21,28/n 2020,5,7,8,10/n 2021,6,9,11,15/n 2022,14,17,20,26"
data = [item.split(',') for item in data.split('/n')]
data_array = np.array(data)

x_values = data_array[1:, 0]
y_values = data_array[0, 1:]
data = np.float32(data_array[1:, 1:])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
yticks = np.arange(len(y_values))

for c, k in zip(colors, yticks):
    xs = np.arange(len(x_values))
    ys = data[:, k]
    # Plot bars
    ax.bar3d(xs, np.full_like(xs, k), np.zeros_like(ys), 0.4, 0.8, ys, color=c, alpha=0.7)

ax.set_xlabel('Year')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(yticks)
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Arts and Culture Attendance Trends - 2018 to 2022')

plt.grid(True)
ax.view_init(30, -60)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/57_202312302126.png')
plt.clf()
