import matplotlib.pyplot as plt
import numpy as np

data_str = """Field,Test A,Test B,Test C,Test D
Accuracy,65,70,75,80
Precision,85,90,95,100
Recall,75,80,85,90
F1 Score,80,85,90,95
Efficiency,70,75,80,85"""

# Parse the data
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [list(map(int, line.split(',')[1:])) for line in data_lines[1:]]

# Create radar chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels, wrap=True)

for i, row in enumerate(data):
    row.append(row[0])  # for close-loop plotting
    ax.plot(angles, row, label=line_labels[i])
    gridlines_radius = np.full_like(angles, (i + 1) * max(max(data)) / len(data))
    ax.plot(angles, gridlines_radius, color='lightgray')

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=180)

# Make space for and rotate legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

ax.set_title('Radar Chart for Model Performance in Science and Engineering', size=16, color='black', y=1.1)
plt.tight_layout()

# Save the plot as a png image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/147_2023122292141.png')

plt.clf()
