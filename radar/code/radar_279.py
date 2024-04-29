import matplotlib.pyplot as plt
import numpy as np

# Data
data_labels = ["Precision", "Efficiency", "Reliability", "Scalability", "Maintainability", "Portability"]
data = np.array([[80, 85, 90, 95], [75, 78, 81, 84], [90, 92, 94, 96], [85, 87, 89, 91], [70, 72, 74, 76], [65, 68, 71, 74]])
line_labels = ["Experiment 1", "Experiment 2", "Experiment 3", "Experiment 4"]

# Angles for the radial grid
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)
for i in range(data.shape[1]):
    vals = np.append(data[:, i], data[0, i])  # loop closure
    ax.plot(angles, vals, label=line_labels[i])
    ax.fill(angles, vals, alpha=0.25)

# Grid and labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_ylim(0, np.max(data) + 10)
ax.grid(True)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="upper right")

# Title and saving
plt.title('Engineering Parameters Analysis for Multiple Experiments', pad=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/72_2023122292141.png')
plt.clf()
