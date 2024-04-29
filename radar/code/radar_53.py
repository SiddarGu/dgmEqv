import numpy as np
import matplotlib.pyplot as plt

data = np.array([[85, 80, 75, 80, 70],
                 [25, 20, 15, 20, 10],
                 [80, 85, 90, 95, 70],
                 [90, 85, 80, 75, 70],
                 [70, 75, 80, 85, 90]])

data_labels = ['NBA', 'FIFA', 'GRAMMYs', 'NETFLIX', 'CNN']
line_labels = ['Popularity (%)', 'Revenue (in billion $)', 'Social Impact (Score)', 'Fan Engagement (Score)', 'Innovation Score']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(data)):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])
    
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

legend_handles, legend_labels = ax.get_legend_handles_labels()
ax.legend(legend_handles, line_labels, loc='best')

ax.set_title('Sports and Entertainment Industry Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/156_202312310100.png')
plt.clf()