import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_labels = ['Red Cross', 'UNICEF', 'World Vision', 'Greenpeace', 'Amnesty International']
line_labels = ['Public Trust (Score)', 'Financial Transparency (Score)', 'Volunteer Satisfaction (Score)', 'Impact (Score)', 'Fundraising Efficiency (Score)']
data = np.array([
    [85, 80, 90, 75, 80],
    [90, 85, 80, 75, 90],
    [75, 78, 80, 82, 85],
    [80, 85, 87, 90, 88],
    [70, 72, 74, 75, 80]
])

# Add close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Create figure and plot radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row and plot data lines with different colors
colors = ['blue', 'green', 'red', 'purple', 'orange']
for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], label=line_labels[i])

# Set axis labels and adjust radial limits
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data) + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right', bbox_to_anchor=(1.2, 1))

# Add background grids
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

# Set title and save the chart
plt.title('Charity and Nonprofit Organization Performance Analysis')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/99_202312302350.png')
plt.close(fig)