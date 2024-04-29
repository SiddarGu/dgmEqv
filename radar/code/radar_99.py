import numpy as np
import matplotlib.pyplot as plt

# Transform data into variables
data_labels = ["Factory A", "Factory B", "Factory C", "Factory D", "Factory E"]
line_labels = ["Raw Material Procurement (%)", "Production Efficiency (%)", "Quality Control (%)", "Inventory Management (%)",
               "Distribution Efficiency (%)"]
data = np.array([[85, 80, 75, 80, 85],
                 [90, 85, 85, 90, 95],
                 [95, 85, 80, 80, 80],
                 [80, 75, 70, 80, 85],
                 [70, 75, 80, 85, 80]])

# Create figure and specify polar axes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, polar=True)

# Set angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Append the first numerical element of each row to the end
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Iterate over each row to plot the data lines
colors = ['red', 'blue', 'green', 'orange', 'purple']
for i, label in enumerate(line_labels):
    ax.plot(angles, data[i], label=label, color=colors[i])
    ax.fill(angles, data[i], alpha=0.25)

# Set axis labels and radial limits
ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels)
ax.set_rlabel_position(0)
ax.set_rmax(np.max(data))
ax.set_ylim(0, np.max(data))

# Set axis labels with rotation
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, rotation=30)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Create legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="best")

# Set background grids
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set title
fig.suptitle("Performance Evaluation in Manufacturing and Production", fontsize=14, fontweight='bold')

# Auto resize image and save
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/164_202312310100.png', dpi=300)

# Clear current image state
plt.clf()