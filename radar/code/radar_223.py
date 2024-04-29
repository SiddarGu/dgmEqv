import numpy as np
import matplotlib.pyplot as plt
from matplotlib.text import TextPath

# Parse and format data
data = "Category,State A,State B,State C,State D/n Conviction Rates,75,80,85,90/n Legal Literacy,70,80,90,100/n Case Closure Time,85,90,95,100/n Legal Aid Utilization,75,80,85,90/n Law-enforcement Efficiency,80,85,90,95"
data = data.split('/n ')
data_labels = data[0].split(',')[1:]
line_labels = [x.split(',')[0] for x in data[1:]]
data = np.array([list(map(int, x.split(',')[1:])) for x in data[1:]])

num_vars = len(data_labels)

# Compute angle each axis
angles = np.linspace(0, 2 * np.pi, num_vars + 1, endpoint=True).tolist()

fig, ax = plt.subplots(figsize=(8,8), subplot_kw=dict(polar=True))
ax.xaxis.set_tick_params(pad=20)
ax.set_thetagrids(np.degrees(angles[:-1]), labels=data_labels, wrap=True, fontsize=12)

highest_val = np.max(data)

for i, row in enumerate(data):
    color = plt.cm.viridis(i / len(data))
    data_line = np.concatenate((row, [row[0]]))
    angle_line = np.full_like(angles, (i+1) * np.max(data) / len(data))
    ax.plot(angles, data_line, color=color, label=line_labels[i])
    ax.fill(angles, data_line, color=color, alpha=0.25)
    ax.plot(angles, angle_line, color=color, linestyle='dashed')

ax.spines["polar"].set_visible(False)
ax.set_rlim(bottom=0,top=100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

plt.title('Legal Affairs Assessment across Different States', size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/172_2023122292141.png')
plt.clf()
