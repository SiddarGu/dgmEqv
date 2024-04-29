import numpy as np
import matplotlib.pyplot as plt

data = np.array([[80, 85, 90, 80, 75],
                [70, 75, 70, 65, 70],
                [90, 95, 90, 85, 80],
                [80, 85, 80, 75, 70],
                [75, 80, 85, 80, 75],
                [85, 90, 95, 90, 85]])

data_labels = ["Environmental Impact (Score)", "Sustainability Initiatives (Score)", "Conservation Efforts (Score)",
               "Pollution Management (Score)", "Waste Management (Score)"]
line_labels = ["Forest Conservation", "Energy Usage", "Water Conservation", "Wildlife Protection",
               "Green Building Initiatives", "Eco-friendly Practices"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ['r', 'g', 'b', 'c', 'm', 'y']
for i in range(len(data)):
    ax.plot(angles, data[i], color=colors[i], label=line_labels[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels)
ax.set_yticklabels([])

max_val = np.max(data)
ax.set_ylim(0, max_val)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

ax.set_title("Environmental and Sustainability Performance Index", fontsize=16)

plt.grid(True)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/109_202312302350.png')
plt.clf()