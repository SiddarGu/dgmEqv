import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Solar Power', 'Wind Power', 'Hydropower', 'Bioenergy', 'Geothermal']
line_labels = ['Carbon Emissions (%)', 'Renewable Energy Production (GWh)', 'Energy Efficiency (%)', 'Cost Effectiveness (%)', 'Environmental Impact (Score)']
data = np.array([[20, 15, 25, 10, 5],
                 [400, 380, 520, 300, 250],
                 [60, 70, 85, 55, 80],
                 [70, 80, 90, 65, 75],
                 [85, 90, 80, 75, 70]])

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(data)):
    ax.plot(angles, data[i], color=colors[i], label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right', bbox_to_anchor=(1.3, 1))

ax.set_title('Comparative Analysis of Renewable Energy Sources')

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/127_202312302350.png')

plt.close(fig)