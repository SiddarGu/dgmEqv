import matplotlib.pyplot as plt
import numpy as np

raw_data = 'Aspect,Prototype A,Prototype B,Prototype C,Prototype D/n Efficiency,80,85,90,95/n Durability,70,75,80,85/n Functionality,65,70,75,80/n Innovation,90,95,100,105/n Cost Efficiency,75,80,85,90'
raw_data = raw_data.replace('/n', '\n').split('\n')

data = [list(map(float, row.split(',')[1:])) for row in raw_data[1:]]
data_labels = raw_data[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in raw_data[1:]]

fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
max_val = max(max(row) for row in data)

for i, d in enumerate(data):
    d.append(d[0]) # to close-loop data lines
    ax.plot(angles, d, label=line_labels[i])
    radius = np.full_like(angles, (i + 1) * max_val / len(data))
    ax.plot(angles, radius, color="k", ls=":")
    
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlim(0, max_val)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)    

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="upper right")

plt.title('Engineering Prototypes Performance Analysis', size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/67_2023122292141.png')
plt.clf()
