
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Q1", "Q2", "Q3", "Q4"]
line_labels = ["Tax Revenue", "Job Creation", "Social Programs", "Economic Growth", "Infrastructure Investment"]
data = [[60, 65, 70, 75], [70, 75, 80, 85], [50, 55, 60, 65], [80, 85, 90, 95], [65, 70, 75, 80]]

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
max_data = np.max(data)

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='polar')

for i in range(len(data)):
    data[i].append(data[i][0])
    ax.plot(angles, data[i], label=line_labels[i], linewidth=2)
    ax.fill(angles, data[i], alpha=0.25)
    ax.grid(color='grey', linestyle='-', linewidth=0.5)
    grid_angle = np.full_like(angles, (i+1) * max_data/len(data))
    ax.plot(angles, grid_angle, color='grey', linestyle='solid')
    
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, max_data)

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9, 0.95))
ax.set_title('Government and Public Policy Evaluation - 2023')
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/2.png')
plt.close(fig)