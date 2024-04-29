import numpy as np
import matplotlib.pyplot as plt

# Data input and transformation
data_string="Crops,Q1,Q2,Q3,Q4\n Wheat,60,65,70,75\n Corn,65,70,75,80\n Rice,70,75,80,85\n Soybean,75,80,85,90\n Vegetable,80,85,90,95"
data_lines = data_string.split("\n")
data_labels = data_lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in data_lines[1:]]
data = np.array([list(map(int, line.split(",")[1:])) for line in data_lines[1:]])

# Plot creation
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(polar=True)

# Radial variables creation
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.append(data, data[:, [0]], axis=1)
data_max = np.max(data)

# Plotting data and gridlines
for i, row in enumerate(data):
    ax.plot(angles, row, label=line_labels[i])
    radius = np.full_like(angles, (i+1) * data_max / len(data))
    ax.plot(angles, radius, color='gray', linestyle='dashed')

# Configuring and plotting axis labels and limits
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_ylim(0, data_max)

# Disabling circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Plotting legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Setting title, resizing and saving
fig.suptitle("Agriculture and Food Production Overview")
fig.tight_layout()
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/79_2023122292141.png")

# Clearing figure
plt.clf()
