import matplotlib.pyplot as plt
import numpy as np


data_labels = ['Philosophy', 'Psychology', 'Sociology', 'Anthropology']
line_labels = ['Critical Thinking', 'Communication Skill', 'Research Ability', 'Ethical Understanding', 'Cultural Awareness']
data = [[85, 80, 90, 83],
        [90, 92, 88, 86],
        [88, 85, 92, 90],
        [95, 90, 94, 96],
        [80, 85, 88, 92]]

data = [np.concatenate((d, [d[0]])) for d in data]  # Append the first element to end to close the loop
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
max_val = np.max(data)
num_vars = len(data_labels)
angles = np.linspace(0, 2 * np.pi, num_vars + 1, endpoint=True)

for idx, row in enumerate(data):
    ax.plot(angles, row, label=line_labels[idx])  
    ax.fill(angles, row, alpha=0.25) 
    r = np.full_like(angles, (idx+1) * max_val / len(line_labels))  
    ax.plot(angles, r, color='silver', linestyle='dotted')
    
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
ax.set_ylim([0, max_val])
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=180)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

plt.title('Skills Assessment in Social Sciences and Humanities', size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/165_2023122292141.png', format='png')
plt.clf()
