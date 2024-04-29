import matplotlib.pyplot as plt
import numpy as np

data = np.array([[75, 80, 70, 65, 60],
                [90, 85, 95, 80, 75],
                [80, 75, 70, 85, 80],
                [95, 90, 85, 80, 75],
                [5, 10, 15, 8, 6]])

data_labels = ['Truck 1', 'Truck 2', 'Truck 3', 'Truck 4', 'Truck 5']
line_labels = ['Efficiency (%)', 'Fuel Consumption (liters)', 
               'Maintenance Cost ($)', 'Delivery Time (hours)', 'Accident Rate (%)']

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], label=line_labels[i])
    
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower left')

plt.title('Logistics and Transportation Efficiency Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/82_202312302350.png')
plt.clf()