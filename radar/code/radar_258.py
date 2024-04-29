import numpy as np
import matplotlib.pyplot as plt

# Data
data_str = 'Crop Type,Spring,Summer,Autumn,Winter/n Wheat,85,80,90,85/n Corn,75,85,95,80/n Rice,60,70,80,65/n Soybeans,70,80,90,75/n Potatoes,65,70,75,70 '

def parse_data(data_str):
    data_lines = data_str.split('/n')
    data_labels = data_lines[0].split(',')[1:]
    line_labels = [line.split(',')[0] for line in data_lines[1:]]
    data = [list(map(int, line.split(',')[1:])) for line in data_lines[1:]]
    return data_labels, data, line_labels

data_labels, data, line_labels = parse_data(data_str)
N = len(data_labels)
angles = np.linspace(0, 2 * np.pi, N + 1, endpoint=True)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

colors = ['b', 'r', 'g', 'y', 'm']
for idx, row in enumerate(data):
    row.append(row[0])
    ax.plot(angles, np.array(row), color=colors[idx], label=line_labels[idx])
    ax.fill(angles, np.array(row), color=colors[idx], alpha=0.25)

    radius = np.full_like(angles, (idx+1) * max(max(data)) / len(data))
    ax.plot(angles, radius, color='gray', linestyle='dotted')

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=10, wrap=True)
ax.set_rlim(0, max(max(data)))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
ax.set_title("Seasonal Yield of Crops in Agriculture", size=20, color='black', position=(0.5, 1.1))

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/142_2023122292141.png')
plt.clf()
