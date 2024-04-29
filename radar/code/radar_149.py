
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Nuclear']
data = [[90, 85, 80, 75], [60, 65, 70, 75], [75, 80, 85, 90], [70, 75, 80, 85], [85, 90, 95, 100]]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
for i in range(len(data)):
    data[i].append(data[i][0])
    ax.plot(angles, data[i], linewidth=1, label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, 100)

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
legend = ax.legend(handles, labels, loc=(0.9, .95), labelspacing=0.1)
fig.suptitle('Energy and Utilities - Performance Analysis')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/11_202312262150.png')
plt.clf()