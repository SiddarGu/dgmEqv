import numpy as np
import matplotlib.pyplot as plt

data = np.array([[70, 75, 80, 85, 90],
                 [60, 65, 70, 75, 80],
                 [80, 85, 90, 95, 100],
                 [75, 80, 85, 90, 95],
                 [65, 70, 75, 80, 85]])

data_labels = ['Banking', 'Insurance', 'Real Estate', 'IT', 'Manufacturing']
line_labels = ['Revenue (%)', 'Operating Cost (%)',
               'Gross Profit (%)', 'Market Share (%)', 'Capital Investment (%)']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ['r', 'g', 'b', 'c', 'm']

for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], label=line_labels[i])
    
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, max(data.flatten()))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.3, 1))

plt.title('Sector-wise Business Performance Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/128_202312302350.png')
plt.close()