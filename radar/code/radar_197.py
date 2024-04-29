import numpy as np
import matplotlib.pyplot as plt

# Original data
data_string = '''Field,Magnetism,Structural Strength,Thermal Conductivity,Acoustic Absorption
Material A,78,82,60,70
Material B,80,85,65,75
Material C,75,80,70,80
Material D,90,95,70,60
Material E,85,90,80,90'''

# Parse data
data_lines = data_string.split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [list(map(int, line.split(',')[1:])) for line in data_lines[1:]]

# Create radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180 / np.pi, data_labels, wrap=True)

for i, row in enumerate(data):
    row.append(row[0])
    ax.plot(angles, row, label=line_labels[i])
    gridline_radius = np.full_like(angles, (i + 1) * max(max(data)) / len(data))
    ax.plot(angles, gridline_radius, color='gray', linestyle='--')

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
ax.set_ylim(0, max(max(data)))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.2, 1))

plt.title('Comparative Analysis of Engineering Materials', size=20, color='black', style='normal', loc='center', pad=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/36_2023122292141.png')
plt.clf()
