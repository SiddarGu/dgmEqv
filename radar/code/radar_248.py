import numpy as np
import matplotlib.pyplot as plt

# Given data
data_str = """Policy,Year 1,Year 2,Year 3,Year 4
Public Infrastructure (Score),70,75,80,85
Education Funding (Million $),80,85,90,95
Healthcare Program (Score),75,80,85,90
Crime Rate (%),26,24,22,20
Unemployment Rate (%),6,5.5,5,4.5"""

data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
data = [list(map(float, line.split(',')[1:])) for line in data_lines[1:]]
line_labels = [line.split(',')[0] for line in data_lines[1:]]

# Plot initialization
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)

# Plotting data and gridlines
max_val = max([max(row) for row in data])
for idx, row in enumerate(data):
    row.append(row[0])
    ax.plot(angles, row, linewidth=1, label=line_labels[idx])
    gridline_radius = np.full_like(angles, (idx + 1) * max_val / len(data))
    ax.plot(angles, gridline_radius, color='gray', linestyle='--', linewidth=0.5)

# Adjusting plot
ax.set_rlim(0, max_val)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Plotting legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Title
plt.title('Government and Public Policy Performance Evaluation', size=20, color='black', y=1.1)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/173_2023122292141.png')
plt.clf()
