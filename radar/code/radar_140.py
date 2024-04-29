
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Region A', 'Region B', 'Region C', 'Region D']
line_labels = ['Tourist Arrival (million)', 'Hotel Occupancy Rate (%)', 'Flight Booking (thousand/day)', 'Local Attraction (number)', 'Tourist Spending (billion)']
data = [[85, 90, 95, 100], [70, 75, 80, 85], [90, 95, 100, 105], [40, 45, 50, 55], [35, 40, 45, 50]]

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, d in enumerate(data):
    d.append(d[0])
    ax.plot(angles, d, label=line_labels[i], linewidth=1.5, color=f'#{2 * i + 1}{2 * i + 1}{2 * i + 1}{2 * i + 1}{2 * i + 1}{2 * i + 1}')

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, max([max(data[i]) for i in range(len(data))]))

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.legend(loc='best')
ax.set_title('Tourism and Hospitality in 2023 - Global Overview', fontsize=14, y=1.08)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/3_202312262150.png')
plt.clf()