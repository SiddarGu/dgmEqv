import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np

# Input data
rows = [
    ["Facebook", 2583, 85.96, 10, 3000],
    ["YouTube", 2000, 19.77, 21, 7500],
    ["Instagram", 1500, 24.00, 7, 2500],
    ["Twitter", 187, 3.72, 6, 500],
    ["TikTok", 689, 34.3, 52, 5500],
    ["LinkedIn", 303, 10.0, 17, 1000],
    ["Snapchat", 293, 2.5, 8, 1500],
    ["Pinterest", 459, 1.88, 5, 900],
    ["Reddit", 52, 0.19, 11, 700],
    ["WhatsApp", 2000, 5.5, 18, 0],
    ["WeChat", 1200, 17.5, 9, 0],
    ["Telegram", 550, 0.00, 2, 200]
]

# Transformation of data
line_labels = [row[0] for row in rows]
data_labels = ["Daily Active Users (Millions)", "Annual Revenue (Billions USD)", 
               "Average Session Duration (Minutes)", "Monthly Data Traffic (Petabytes)"]
data = np.array([row[1:] for row in rows])

# Figure initialization
plt.figure(figsize=(25, 10))
ax1 = plt.subplot(111)

# Bar chart for the first column
bar_width = 0.2
bar_positions = np.arange(len(line_labels))
ax1.bar(bar_positions, data[:, 0], width=bar_width, color='b', alpha=0.7, label=data_labels[0])

# Set the primary y-axis properties
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(line_labels, rotation=45, ha='right', wrap=True)

# Line chart for the second column
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'r-', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Scatter chart for the third column
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.07))  # Offset ax3
ax3.scatter(line_labels, data[:, 2], color='g', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='g')
ax3.tick_params(axis='y', labelcolor='g')

# Area chart for the fourth column
ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.14))  # Offset ax4
ax4.fill_between(line_labels, data[:, 3], step='mid', color='purple', alpha=0.5, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='purple')
ax4.tick_params(axis='y', labelcolor='purple')

# Set the locator for y-axes
for ax in [ax1, ax2, ax3, ax4]:
    ax.yaxis.set_major_locator(AutoLocator())

# Legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower right')
ax4.legend(loc='lower left')

# Title
plt.title('Navigating the Digital Landscape: A Comparative Analysis of Social Media Platforms')

# Background grid and layout resizing
ax1.grid(True)
plt.tight_layout()

# Saving the image
save_path = "/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/51_2023122291723.png"
plt.savefig(save_path)

# Clear the current state
plt.clf()
