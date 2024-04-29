import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Desktop users', 'Tablet users', 'Mobile users', 'SmartTV users', 'IoT device users']
line_labels = ['Active Users (%)', 'E-commerce Transactions (%)', 'Social Media Engagement (%)', 'Streaming Media Consumption (%)', 'Security Issues Encountered (%)']
data = np.array([[75, 70, 80, 65, 50],
                 [60, 65, 70, 75, 80],
                 [70, 80, 75, 70, 65],
                 [85, 80, 75, 70, 60],
                 [50, 55, 45, 40, 35]])

fig=plt.figure(figsize=(10, 8))
ax = plt.subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], '-o', label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlabel_position(0)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(["20%", "40%", "60%", "80%", "100%"])
ax.set_ylim(0, 100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.grid(True)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.1, 1))
plt.title("Internet Usage Patterns across Different Devices")

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/79_202312302350.png')

plt.clf()