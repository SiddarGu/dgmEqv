import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Hydro Power', 'Coal Power', 'Nuclear Power', 'Gas Power', 'Wind Power/Solar Power']
line_labels = ['Energy Production (GWH)', 'Maintenance Costs (Million $)', 'Sustainability Index (%)', 'Efficiency (%)', 'Carbon Emission (1000 Tonnes)']

data = np.array([[80, 85, 90, 95, 100],
                 [45, 50, 55, 60, 65],
                 [35, 40, 45, 50, 55],
                 [70, 75, 80, 85, 90],
                 [85, 80, 75, 70, 65]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])
    
ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels)

ax.set_yticklabels([])

ax.set_ylim([0, np.max(data)])
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

ax.grid(True)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

plt.title('Energy and Utilities Sector Performance Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/163_202312310100.png')
plt.close()