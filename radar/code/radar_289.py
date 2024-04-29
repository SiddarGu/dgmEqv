import matplotlib.pyplot as plt
import numpy as np

raw_data = """Area of Law,Family Law,Criminal Law,Employment Law,Contract Law,Environmental Law
Case Success Rate,72,78,81,65,86
Client Satisfaction,85,82,89,77,90
Legal Complexity,70,90,75,80,85
Cost Efficiency,75,70,80,78,82
Time Efficiency,80,77,84,79,85"""

# parsing raw data into lines
lines = raw_data.split("\n")

# splitting each line into items
lines = [line.split(",") for line in lines]

# extracting labels and data
data_labels = lines[0][1:]
lines = lines[1:]
line_labels = [line[0] for line in lines]
data = [line[1:] for line in lines]

# Convert to float for numerical operations
data = np.array(data, dtype=float)
num_var = len(data_labels)

# Prepare canvas of the plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_var, endpoint=False).tolist()

# Ensure the plot is a closed loop
angles += angles[:1]

# Iterate over each row of data and plot it on the radar chart
data = np.concatenate((data, data[:, [0]]), axis=1)
for idx, (val, color) in enumerate(zip(data, plt.cm.Set2(np.linspace(0, 1, num_var)))):
    ax.fill(angles, val, color=color, alpha=0.25)
    ax.plot(angles, val, color=color, linewidth=2, label=line_labels[idx])

# Configure radial gridlines and labels
ax.set_yticklabels([])
ax.set_theta_offset(np.pi / 2)  # The starting point is on top
ax.set_theta_direction(-1)  # clockwise rotation
ax.set_thetagrids(np.degrees(angles[:-1]), data_labels)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Configure legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", bbox_to_anchor=(1.15, 1.1))

# Set title
plt.title('Law and Legal Affairs Performance Evaluation', size=20, color='black', y=1.1)

# Save plot
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/56_2023122292141.png")

# Clear the figure for future plots
plt.clf()
