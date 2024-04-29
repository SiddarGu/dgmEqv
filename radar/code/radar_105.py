import numpy as np
import matplotlib.pyplot as plt

data_labels = ['General Hospital', "Children's Hospital", 'Dental Clinic', 'Physiotherapy Center', 'Eye Care Center']
line_labels = ['Patient Satisfaction', 'Treatment Effectiveness', 'Staff Efficiency', 'Facility Quality', 'Cost Efficiency']
data = np.array([[80, 85, 75, 90, 70],
                 [80, 75, 95, 85, 80],
                 [90, 85, 70, 80, 95],
                 [75, 90, 80, 85, 95],
                 [75, 70, 65, 80, 85]])

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
plt.xticks(angles[:-1], data_labels)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], label=line_labels[i])
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

plt.legend(loc='upper right')

plt.title('Health Facility Performance Comparison')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/187_202312310100.png')
plt.close()