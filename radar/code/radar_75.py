import numpy as np
import matplotlib.pyplot as plt

data = np.array([[4.1, 2.8, 5.6, 2.1, 25, 3],
                 [9, 6, 15, 5, 25, 10],
                 [10, 9, 12, 8, 15, 7],
                 [15, 10, 20, 8, 30, 12],
                 [21, 18, 23, 15, 31, 17]])

data_labels = ['Rice', 'Wheat', 'Corn', 'Soybean', 'Potato', 'Barley']
line_labels = ['Yield (tons per hectare)', 'Water Requirement (million liters per hectare)', 
               'Fertilizer Need (kg per hectare)', 'Pesticide Use (kg per hectare)', 'Profit ($ per hectare)']

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, row in enumerate(data):
    ax.plot(angles, row, linewidth=2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12, rotation=0, wrap=True)
ax.set_rlim(0, data.max())
ax.grid(True)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
plt.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.2, 1))

plt.title('Agriculture and Food Production Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/49_202312302350.png')
plt.close()