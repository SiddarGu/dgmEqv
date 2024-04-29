import matplotlib.pyplot as plt
import numpy as np

data = "Parameter,Model A,Model B,Model C,Model D\nEfficiency (%),85,80,75,70\nDurability (Years),\
10,9,8,7\nEnergy Consumption (watts),50,55,60,65\nMaintenance Cost ($),20,25,30,35\nPerformance Index,\
90,85,80,75"
lines = data.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = np.array([list(map(int, line.split(",")[1:])) for line in lines[1:]])
data = np.concatenate((data, data[:, 0:1]), axis=1)
num_vars = len(data_labels)

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
colors = ['b', 'r', 'g', 'm', 'y']
angles = np.linspace(0, 2 * np.pi, num_vars + 1, endpoint=True).tolist()

for i in range(len(data)):
    ax.plot(angles, data[i], color=colors[i], linewidth=3, label=line_labels[i])
    ax.fill(angles, data[i], color=colors[i], alpha=0.25)

ax.set_thetagrids(np.degrees(angles[:-1]), data_labels)
plt.title('Comparison of Engineering Models', size=20, color='blue', y=1.1)

ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, data_labels, loc="upper right", bbox_to_anchor=(0.1, 0.1))

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/175_2023122292141.png')
plt.clf()
