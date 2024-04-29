import numpy as np
import matplotlib.pyplot as plt

data_labels = ('Hydropower', 'Nuclear Power', 'Wind Power', 'Solar Power', 'Geothermal Power')
data = np.array([[100, 120, 80, 90, 75],
                 [85, 90, 75, 80, 70],
                 [80, 100, 70, 60, 55],
                 [90, 65, 95, 100, 95],
                 [85, 50, 95, 100, 95]])

line_labels = ('Production (in GWh)', 'Efficiency (%)', 'Cost (in USD Million)', 'Environmental Impact (Score)', 'Sustainability (Score)')

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels)

ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

colors = ['blue', 'green', 'red', 'orange', 'purple']

for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], label=line_labels[i])
    
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))

ax.set_title('Energy and Utilities Comparison Analysis')

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/184_202312310100.png')
plt.clf()