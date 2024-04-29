import matplotlib.pyplot as plt
import numpy as np

# Defining attributes and their scores
data_labels=['Hydropower', 'Solar', 'Wind', 'Nuclear']
line_labels = ['Energy Production', 'Efficiency', 'Cost Effectiveness', 'Environmental Impact', 'Supply Stability']
data = np.array([[85, 90, 95, 100],
                 [75, 80, 85, 90],
                 [70, 75, 80, 85],
                 [60, 65, 70, 75],
                 [95, 90, 85, 80]])

# Number of variables 
num_vars = len(data_labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

# Repeat the first value to close the circular graph
data = np.concatenate((data, data[:,[0]]), axis=1)
angles = np.concatenate((angles,[angles[0]]))

# Create figure
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for idx, (title, values) in enumerate(zip(line_labels, data)):
    color = plt.cm.hsv(idx/float(len(data_labels)))
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, label=title)
    ax.plot(angles, np.full_like(angles, (idx+1) * np.amax(data) / len(data)), 
            color='silver', 
            linestyle='dashed')

# Axis decoration
ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels, rotation=45, fontsize=13)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.set_title('Evaluation of Different Energy Sources in Utilities Sector', size=16, color='darkred', y=1.1)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/140_2023122292141.png')
plt.clf()
