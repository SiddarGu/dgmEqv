
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Donations Received (K USD)', 'Number of Donations', 'Number of Volunteers']
x_values = ['2019', '2020', '2021', '2022', '2023']
data = np.array([[100000, 100000, 200000],
                 [125000, 125000, 300000],
                 [150000, 150000, 400000],
                 [175000, 175000, 500000],
                 [200000, 200000, 600000]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x_pos = np.arange(len(x_values))

for i in range(len(y_values)):
    y_pos = [i] * len(x_values)
    ax.bar3d(x_pos, y_pos, np.zeros(len(x_values)), 1, 1, data[:, i], alpha=0.5)

ax.set_xticks(x_pos)
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=-30, ha='left')
ax.set_yticklabels(y_values)

plt.title('Financial and Volunteer Support for Nonprofit Organizations - 2019 to 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/7_202312251000.png')
plt.clf()