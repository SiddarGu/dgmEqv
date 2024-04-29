import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Green Energy', 'Conservation', 'Eco Manufacturing', 'Responsible Sourcing', 'Waste Management']
line_labels = ['Carbon Footprint Reduction (%)', 'Renewable Energy Use (%)', 'Water Conservation (%)', 'Sustainable Materials Use (%)', 'Waste Reduction (%)']

data = np.array([[80, 85, 90, 95, 85],
                 [85, 90, 95, 80, 75],
                 [75, 80, 85, 90, 95],
                 [95, 90, 85, 80, 75],
                 [70, 75, 80, 85, 90]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

data = np.concatenate((data, data[:, 0:1]), axis=1)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], 'o-', linewidth=2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper left')
lgd.set_bbox_to_anchor((1.0, 1.0))

plt.title("Environmental and Sustainability Performance")

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/69_202312302350.png')

plt.clf()