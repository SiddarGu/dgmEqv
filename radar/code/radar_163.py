import matplotlib.pyplot as plt
import numpy as np

# Transforming the given data into variables
data_labels = ["Processing Speed (GHz)", "Battery Life (Hours)", "RAM (GB)", "Internal Storage (GB)", "Connectivity Range (m)"]
data = np.array([[2.5, 2.7, 2.4, 2.1, 1.8],
                [5, 7, 10, 8, 12],
                [16, 8, 4, 2, 1],
                [5.12, 2.56, 1.28, 6.4, 3.2],
                [20, 30, 40, 50, 10]])

line_labels = ["Aspect", "Desktop", "Laptop", "Smartphone", "Tablet", "Smart Watch"]

# Plotting the radar chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Adding a close-loop plot of data lines for each row
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Setting evenly spaced angles for axes
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plotting each row as a separate line with different colors
colors = ['b', 'g', 'r', 'c', 'm', 'y']
for i, row in enumerate(data):
    ax.plot(angles, row, label=line_labels[i+1], color=colors[i], marker='o')

# Plotting axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjusting radial limits to accommodate the maximum of data
ax.set_ylim(0, data.max())
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Adding legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc="upper right")

# Adding title and grid
ax.set_title("Technological Device Performance Evaluation")

# Resizing image and saving
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/181_202312310100.png")

# Clearing current image state
plt.clf()