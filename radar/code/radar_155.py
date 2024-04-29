import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ["Facebook", "Instagram", "Twitter", "LinkedIn", "Pinterest", "Youtube"]
line_labels = ["Active Users (Millions)", "Average Session Duration (Minutes)", "Daily Postings (Millions)", "Bounce Rate (%)", "Daily New Signups (Thousands)"]
data = np.array([
    [12, 64, 23, 37, 29, 14],
    [15, 10, 8, 9, 6, 20],
    [45, 50, 70, 20, 35, 50],
    [30, 35, 45, 40, 25, 20],
    [50, 60, 25, 35, 30, 80]
])

# Create figure and plot radar chart
fig = plt.figure(figsize=(10, 10))
axes = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ['b', 'g', 'r', 'c', 'm', 'y']
for i, row in enumerate(data):
    axes.plot(angles, row, color=colors[i], linewidth=2, label=line_labels[i])

# Set axis labels
axes.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust radial limits
axes.set_ylim(0, np.max(data) + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
axes.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Add legend
handles, labels = axes.get_legend_handles_labels()
plt.legend(handles, line_labels, loc='upper right')

# Add gridlines
plt.grid(True)

# Set title
plt.title("Social Media Engagement and Web Metrics Analysis")

# Adjust image size and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/51_202312302350.png')

# Clear current image state
plt.clf()