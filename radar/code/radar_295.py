import matplotlib.pyplot as plt
import numpy as np

# Manipulate data
data = '''Services,Hospital A,Hospital B,Hospital C,Hospital D
Outpatient Services,90,85,80,75
Inpatient Services,85,80,75,70
Emergency Services,80,85,90,95
Diagnostic and Lab Services,75,70,65,60
Nursing and Residential Care,90,95,80,85'''

# Parse data string into a data list
data_list = [i.split(',') for i in data.split('\n')]

# Extract labels and data
data_labels = data_list[0][1:]
line_labels = [i[0] for i in data_list[1:]]
data = np.array([list(map(int, i[1:])) for i in data_list[1:]])

# Create a radar chart
num_vars = len(data_labels)
angles = np.linspace(0, 2 * np.pi, num_vars + 1, endpoint=True)

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
for i, row in enumerate(data):
    # Loop closing
    row = np.concatenate((row, [row[0]]))
    # Plot data and gridlines
    ax.plot(angles, row, color='C{}'.format(i), label=line_labels[i])
    ax.fill(angles, row, color='C{}'.format(i), alpha=0.25)
    ax.plot(angles, np.full_like(angles, (i+1)*data.max()/num_vars),
            color='C{}'.format(i), linestyle='dashed', marker='o')

# Set the axes and labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, labels=data_labels, wrap=True)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=-90)

ax.set_rlim(bottom=0, top=data.max()+(data.max()/10))
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
plt.title('Health Services Performance Comparison', size=20, color='blue', y=1.1)

# Save and display the figure
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/28_2023122292141.png')

# Clear the figure
plt.clf()
