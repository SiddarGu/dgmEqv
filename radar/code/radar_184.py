import numpy as np
import matplotlib.pyplot as plt

data = np.array([[80, 60, 50, 20, 15],
                 [75, 55, 45, 18, 20],
                 [50, 40, 35, 12, 30],
                 [40, 35, 30, 10, 25],
                 [45, 37, 32, 11, 20]])

data_labels = ['Detached House Price', 'Townhouse Price', 'Apartment Price', 'Rental Price', 'New Developments']
line_labels = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide', 'Perth']

data = np.concatenate((data, data[:, 0:1]), axis=1)

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker='o', linewidth=2, label=line_labels[i])

plt.xticks(angles[:-1], data_labels)
plt.ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left')

ax.set_title('Real Estate and Housing Market Overview in Australia')

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/73_202312302350.png')

plt.clf()