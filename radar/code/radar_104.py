import numpy as np
import matplotlib.pyplot as plt


data_labels = ['Utilities', 'Renewable Energy', 'Non-renewable Energy', 'Nuclear Energy', 'Hydropower']
line_labels = ['Production (GWh)', 'Efficiency (%)', 'Cost per unit ($)', 'Reliability Score', 'Safety Score', 'Carbon Emissions (tons)']

data = np.array([
    [50, 55, 60, 65, 70],
    [70, 75, 80, 85, 90],
    [60, 62, 64, 66, 68],
    [80, 85, 90, 95, 95],
    [85, 90, 95, 100, 105],
    [120, 110, 100, 90, 80]
])

data = np.concatenate((data, data[:, :1]), axis=1)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, row in enumerate(data):
    ax.plot(angles, row, marker='.', label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, max(data.flatten()))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

plt.title('Energy and Utilities: Comparative Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/149_202312310100.png')
plt.clf()
