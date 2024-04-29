
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Energy Generation (KGWh)', 'Efficiency (%)', 'Capacity Factor (%)', 'Availability (%)', 'Cost per MWh (USD)']
line_labels = ['Solar', 'Wind', 'Hydro', 'Thermal']
data = np.array([[24, 90, 85, 95, 50], [27, 91, 86, 96, 45], [30, 92, 87, 97, 40], [33, 93, 88, 98, 35]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(data)):
    ax.plot(angles, data[i], color=np.random.rand(3, ), linewidth=2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
ax.legend(loc='upper right', bbox_to_anchor=(1, 1))

plt.title('Energy and Utilities Performance Comparison - 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/47_202312262320.png')
plt.clf()