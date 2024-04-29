import matplotlib.pyplot as plt
import numpy as np

data = np.array([[75, 80, 90, 70, 60],
                 [80, 85, 75, 90, 70],
                 [70, 75, 80, 85, 70],
                 [90, 92, 94, 90, 88],
                 [85, 90, 95, 80, 75]])

data_labels = ['Solar Power', 'Wind Power', 'Hydropower', 'Geothermal Energy', 'Biomass Energy']
line_labels = ['Carbon Emission Reduction (%)', 'Energy Conversion Efficiency (%)', 'Cost Efficiency (Score)', 
               'Sustainability (Score)', 'Renewable Energy Potential (Score)']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ['b', 'g', 'r', 'c', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], marker='o', label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
ax.legend(bbox_to_anchor=(1.15, 1), loc='upper right')
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)


plt.title('Renewable Energy Sources Sustainability Analysis')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/177_202312310100.png')
plt.close(fig)