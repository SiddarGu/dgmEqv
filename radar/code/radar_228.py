import numpy as np
import matplotlib.pyplot as plt

# Prepare Data
data_str = "Air, 65,70,75,80; Sea, 55,60,65,70; Rail, 70, 75,80,85; Road, 60,65,70,75; Pipeline, 50, 55,60,65"
data_str_list = [item.split(',') for item in data_str.split(';')]
data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = [item[0] for item in data_str_list]
data = [list(map(int, item[1:])) for item in data_str_list]

# Begin Drawing
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

colors = ['b', 'g', 'r', 'c', 'm']
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(data)):
    data[i].append(data[i][0])
    ax.plot(angles, np.full_like(angles, (i+1)*max(max(data))/len(data)), color=colors[i], alpha=0.1)
    ax.plot(angles, data[i], color=colors[i], label=line_labels[i], linewidth=2)
    
ax.fill(angles, data[i], facecolor=colors[i], alpha=0.25)

ax.set_thetagrids(angles[:-1]*180/np.pi, data_labels)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.set_title("Transportation Modal Split - 2023", size=20, color='black', y=1.1)

ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right', bbox_transform=plt.gcf().transFigure)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/192_2023122292141.png", dpi=300)
plt.close(fig)
