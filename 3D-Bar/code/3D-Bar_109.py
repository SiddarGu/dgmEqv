

import numpy as np
import matplotlib.pyplot as plt

y_values = ['Donations (USD million)', 'Volunteer Hours (million hours)', 'Number of Charities']
data = np.array([[2000, 1500, 3000], [2200, 1200, 2750], [2400, 1700, 3200], [2500, 1800, 3500], [2700, 1600, 3300]])
x_values = ['2019', '2020', '2021', '2022', '2023']

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.2, 0.2, data[:, i], shade=True, color='b', alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
ax.view_init(30, -15)
ax.set_title('Charitable Contributions and Volunteerism - 2019 to 2023')
ax.autoscale_view()
fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/30_202312270030.png')
plt.clf()