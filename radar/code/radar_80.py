import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Truck', 'Ship', 'Train', 'Plane', 'Cargo Van']
line_labels = ['On-Time Delivery (%)', 'Fuel Efficiency (MPG)', 'Load Capacity (Tons)', 'Maintenance Cost ($k/year)', 'Average Speed (MPH)']
data = np.array([[90, 85, 95, 92, 88],
                 [10, 30, 80, 300, 15],
                 [20, 1000, 100, 50, 1],
                 [10, 100, 50, 500, 5],
                 [60, 20, 70, 600, 80]])

# Append the first element of each row to create closed loops
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

for i in range(data.shape[0]):
    ax.plot(angles, data[i], linewidth=2, label=line_labels[i])

ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Transportation and Logistics Efficiency Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/135_202312302350.png')
plt.close()
