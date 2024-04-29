import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [70, 75, 80, 85, 90],
    [80, 85, 90, 95, 92],
    [60, 65, 70, 75, 80],
    [90, 95, 92, 87, 85],
    [75, 80, 85, 90, 88]
])

data_labels = ["Factory A", "Factory B", "Factory C", "Factory D", "Factory E"]
line_labels = ["Production Volume (K Units)", "Production Efficiency (%)", "Waste Management (%)", "Equipment Utilization (%)", "Cost Efficiency (%)"]

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ["b", "g", "r", "c", "m"]
for i in range(len(data)):
    ax.plot(angles, data[i], color=colors[i], linewidth=2, label=line_labels[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels, rotation=45, wrap=True, fontsize=10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

plt.legend(line_labels, loc="upper left")
plt.title("Manufacturing and Production Performance Analysis")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/140_202312302350.png")
plt.clf()