
import numpy as np
import matplotlib.pyplot as plt

data_labels = np.array(['Tourist Arrivals (in Millions)', 'Hotel Room Occupancy (%)', 'Retail Sales (in Billions)', 'Cultural Attractions (Score)', 'Hospitality Services (Score)'])
line_labels = np.array(['Beijing', 'Shanghai', 'Guangzhou', 'Chengdu', 'Shenzhen'])
data = np.array([[20, 70, 30, 90, 80],
                 [25, 75, 40, 85, 85],
                 [30, 80, 50, 80, 90],
                 [35, 85, 60, 75, 95],
                 [40, 90, 76, 70, 99]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=15)
ax.set_rlim(0, np.max(data))

for i in range(len(data)):
    ax.plot(angles, data[i], label=line_labels[i], linewidth=2, color=plt.cm.jet(i/len(data)))
    ax.fill(angles, data[i], alpha=0.1, color=plt.cm.jet(i/len(data)))

handles, labels = ax.get_legend_handles_labels()
legend = plt.legend(handles[::-1], labels[::-1], loc='upper left', bbox_to_anchor=(1.1, 1))

plt.title('Tourism and Hospitality Trends in China', fontsize=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/6_202312262320.png')

plt.clf()