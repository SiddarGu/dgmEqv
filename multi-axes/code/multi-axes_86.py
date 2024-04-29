import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Transformed data into variables
data_labels = ["Donation Amount (Thousands of Dollars)", "Number of Volunteers", "Events Held/Year"]
line_labels = ["Community Services", "Health Services", "Educational Programs", "Environmental Conservation", "Disaster Relief", "Animal Welfare", "Cultural Preservation", "International Aid", "Advocacy Groups", "Research and Development"]
data = np.array([
    [1503, 240, 24],
    [2424, 150, 16],
    [1795, 320, 38],
    [965, 210, 46],
    [2208, 550, 12],
    [738, 270, 25],
    [1670, 190, 29],
    [1520, 600, 10],
    [1280, 235, 37],
    [2125, 410, 19]
])

# Create figure and subplot
fig = plt.figure(figsize=(22, 10))
ax1 = fig.add_subplot(111)

# Plot column 0: Bar chart
bar_width = 0.25
positions = np.arange(len(line_labels))
ax1.bar(positions, data[:, 0], width=bar_width, color='b', alpha=0.7, label=data_labels[0])
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_xticks(positions)
ax1.set_xticklabels(line_labels, rotation=45, ha='right', wrap=True)

# Plot column 1: Scatter chart
ax2 = ax1.twinx()
ax2.scatter(positions, data[:, 1], color='r', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Plot column 2: Line chart
ax3 = ax1.twinx()  # Create a new axes with shared x-axis
ax3.plot(positions, data[:, 2], color='g', marker='o', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='g')
ax3.tick_params(axis='y', labelcolor='g')

# Position ax3's spine to separate different y-axes
ax3.spines['right'].set_position(('outward', 60))

# Set up AutoLocator for all axes
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

# Set the grid and legend
ax1.grid(True)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='center right')

# Set the title and layout
plt.title('Impact Assessment of Charity and Nonprofit Sectors on Social Welfare')
plt.tight_layout()

# Save image
save_path = "/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/52_2023122291723.png"
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()