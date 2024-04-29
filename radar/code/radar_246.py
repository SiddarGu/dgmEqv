import matplotlib.pyplot as plt
import numpy as np

# Original data
raw_data = [
    ["Category", "Q1", "Q2", "Q3", "Q4"],
    ["Athletic Performance", 60, 70, 80, 90],
    ["Audience Size", 70, 75, 80, 85],
    ["Sponsorship", 75, 80, 85, 90],
    ["Revenue", 80, 85, 90, 95],
    ["Media Coverage", 65, 70, 75, 80]
]

# Preparing data
data_labels = raw_data[0][1:]
data = [row[1:] for row in raw_data[1:]]
line_labels = [row[0] for row in raw_data[1:]]

# Creating radar chart
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, polar=True)

# Plotting data
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
for idx, (row, color) in enumerate(zip(data, colors)):
    data_row_extended = row + [row[0]]  # for close-loop plotting
    ax.plot(angles, data_row_extended, color=color, linewidth=2, label=line_labels[idx])
    ax.fill(angles, data_row_extended, color=color, alpha=0.25)
    ax.plot(angles, np.full_like(angles, (idx+1) * max([item for sublist in data for item in sublist]) / len(data)), color='black', linestyle='dashed')

# Finalize chart
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_rlim(0, 100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
plt.tight_layout()
plt.title('Sports and Entertainment Performance Review')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/30_2023122292141.png')
plt.close(fig)
