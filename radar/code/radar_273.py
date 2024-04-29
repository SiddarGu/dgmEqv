import numpy as np
import matplotlib.pyplot as plt

# create data
data_labels = ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4']
line_labels = ['Case Success Rate', 'Client Satisfaction', 'Staff Efficiency', 'Regulatory Compliance', 'Cost Management']
data = np.array([[80, 82, 83, 85],
                 [75, 77, 79, 81],
                 [70, 73, 76, 79],
                 [88, 89, 90, 92],
                 [66, 68, 70, 72]])

# create figure
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)
ax.set_title('Law Firm Performance Analysis 2023', size=20, color='black', y=1.1)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# plot data
for index, values in enumerate(data):
    values = np.append(values, values[0])    # closed loop
    ax.plot(angles, values, label=line_labels[index])
    radius = np.full_like(angles, (index+1) * np.max(data) / len(data))
    ax.plot(angles, radius, color='lightgrey', linestyle='dotted')

# remove the circular gridlines
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=180)

# plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right', bbox_to_anchor=(1.1, 1.1))

# set limit
ax.set_ylim(0, 100)

# save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/133_2023122292141.png')
    
# clear figure
plt.clf()
