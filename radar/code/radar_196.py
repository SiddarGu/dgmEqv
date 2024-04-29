import numpy as np
import matplotlib.pyplot as plt

data = [
    [50,55,58,52],
    [70,75,78,74],
    [85,87,89,88],
    [45,48,46,47],
    [65,67,70,72]
]
data_labels = ['January', 'February', 'March', 'April']
line_labels = ['Raw Material Costs', 'Production Volume', 'Quality Control Score', 'Maintenance Costs', 'Return on Investment']

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, data_item in enumerate(data):
    data_item.append(data_item[0])
    ax.plot(angles, data_item, label=line_labels[i])

    radius = np.full_like(angles, (i+1) * max(l for sublist in data for l in sublist) / len(data))
    ax.plot(angles, radius, color='grey', linestyle='dashed')

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
ax.xaxis.label.set_size(15)
ax.set_ylim(0, max(l for sublist in data for l in sublist))

plt.title('Manufacturing and Production Performance Review', size=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/129_2023122292141.png', format='png')
plt.clf()
