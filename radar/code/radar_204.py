import matplotlib.pyplot as plt
import numpy as np

# parse the data
raw_data='Policy Area,Q1,Q2,Q3,Q4/n Education,75,80,85,90/n Healthcare,70,75,80,85/n Transportation,60,65,70,75/n Environment,80,85,90,95/n Security,65,70,75,80'
raw_data = raw_data.split('/n')
line_labels = [item.split(',')[0] for item in raw_data[1:]]
data_labels = raw_data[0].split(',')[1:]
data = np.array([item.split(',')[1:] for item in raw_data[1:]], dtype=int)

# prepare figure and layout
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

# calculate angles and grid lines
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# plot data
for idx, item in enumerate(data):
    ax.plot(angles, np.concatenate([item, item[:1]]), label=line_labels[idx])
    ax.fill(angles, np.concatenate([item, item[:1]]), 'b', alpha=0.1)
    radius = np.full_like(angles, (idx+1) * data.max()/len(data))
    ax.plot(angles, radius, color='grey', ls='--', lw=0.5)
    
# format plot
ax.spines['polar'].set_visible(False)
ax.set_yticklabels([])
ax.yaxis.grid(False)
ax.set_rlim(0, data.max() * 1.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
plt.title('Government Policy Performance Evaluation')

# save and display plot
plt.tight_layout()

path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/134_2023122292141.png'
plt.savefig(path)
plt.cla()
plt.close(fig)
