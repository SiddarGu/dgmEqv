import numpy as np
import matplotlib.pyplot as plt

data = np.array([[2, 5, 1, 3, 7],
                 [80, 85, 70, 75, 90],
                 [70, 95, 60, 85, 100],
                 [85, 80, 75, 90, 95],
                 [60, 55, 70, 65, 80]])

data_labels = ['Trucks', 'Ships', 'Air Freight', 'Trains', 'Pipelines']
line_labels = ['Delivery Speed (Days)', 'Cost Efficiency (Score)', 'Volume Capacity (%)', 'Reliability (Score)', 'Environmental Impact (Score)']

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for index, row in enumerate(data):
    ax.plot(angles, row, label=line_labels[index])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(1.1, 0.9))

plt.title("Transportation and Logistics Mode Analysis")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/201_202312310100.png")
plt.close(fig)
