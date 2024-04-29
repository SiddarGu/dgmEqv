import numpy as np
import matplotlib.pyplot as plt

data = np.array([[26, 33, 10, 20, 74, 45],
                 [35, 10, 27, 40, 10, 14],
                 [86, 115, 20, 15, 80, 11],
                 [60, 70, 85, 90, 50, 30],
                 [70, 65, 80, 85, 60, 50]])

data_labels = ['Facebook', 'Twitter', 'Instagram', 'YouTube', 'LinkedIn', 'Pinterest']
line_labels = ['Active Users (Millions)', 'Avg. Time Spent (Minutes)', 'Ad Revenue (Billions)', 'Global Reach (%)', 'User Engagement (%)']

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])
    
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

ax.legend(line_labels, loc='lower right')

plt.title('Social Media Platform Performance and Reach')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/165_202312310100.png')
plt.show()
plt.clf()
