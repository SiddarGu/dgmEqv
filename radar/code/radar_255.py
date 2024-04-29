import matplotlib.pyplot as plt
import numpy as np

# Data transformation
data_string = "Aspect,Court A,Court B,Court C,Court D/n Case Efficiency,55,60,65,70/n Judicial Fairness,85,80,85,90/n Legal Complexity,65,70,75,80/n Case Clearance,70,75,70,80/n Courtroom Accessibility,60,65,70,75"
data_list = [row.split(',') for row in data_string.replace('/n', '\n').split('\n')]

data_labels = data_list[0][1:]
data = np.array([list(map(int, row[1:])) for row in data_list[1:]])
line_labels = [row[0] for row in data_list[1:]]

# Create figure
plt.figure(figsize=(8, 8))
ax = plt.subplot(polar=True)

# Plot data
for idx, row in enumerate(data):
    angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
    data_line = np.append(row, row[0]) # close the loop
    ax.plot(angles, data_line, label=line_labels[idx], alpha=.6)

    # Gridlines
    radius = np.full_like(angles, (idx+1) * data.max() / len(data))
    ax.plot(angles, radius, color='grey', linestyle='dotted', linewidth=0.6)

# Add labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True, fontsize=10)

# Set limits and gridlines
ax.set_rlim(0, 100)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, data_labels, loc="upper right")

# Title and savefig
plt.title('Comparative Analysis of Court Performance')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/90_2023122292141.png', dpi=300)

# Clear the current state
plt.clf()
