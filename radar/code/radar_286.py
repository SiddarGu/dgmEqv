import matplotlib.pyplot as plt
import numpy as np

# Data Conversion
raw_data = [['Category','Baseball','Basketball','Soccer','Tennis'],
            ['Popularity',78,85,90,70],
            ['Attendance',70,80,75,65],
            ['Revenue',65,68,72,62],
            ['Player Salary',80,85,79,80],
            ['Media Coverage',82,90,75,70]]

data_labels = raw_data[0][1:]
data = [row[1:] for row in raw_data[1:]]
line_labels = [row[0] for row in raw_data[1:]]

# Create Figure and Subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Compute angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plotting Data and Gridlines
for i, row in enumerate(data):
    row.append(row[0]) # closing the plot
    ax.plot(angles, row, label=line_labels[i])
    ax.fill(angles, row, alpha=0.1)
    gridline = np.full_like(angles, (i+1) * max(max(data)) / len(data))
    ax.plot(angles, gridline, color='gray', linestyle='--')

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True) 
ax.set_rlim(0, max(max(data)))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Removing circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Adding title
plt.title("Analysis of Different Sports in Sports and Entertainment sector", size=20)

# Save Figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/98_2023122292141.png")
plt.cla() # clear the figure
