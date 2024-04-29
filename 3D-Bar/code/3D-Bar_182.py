import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"],
    "New Housing Permits Issued": [990, 950, 920, 890, 860],
    "Home Sales Completed": [800, 780, 760, 720, 700],
    "Median Home Price ($000)": [900, 870, 840, 820, 800]
}

# Number of bars per group and bar width
num_bars = len(data["City"])
bar_width = 0.2

# X positions for the groups
x_pos = np.arange(num_bars)

# Create 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting each data series
ax.bar3d(x_pos, np.zeros(num_bars), np.zeros(num_bars), bar_width, bar_width, data["New Housing Permits Issued"], color='b')
ax.bar3d(x_pos, np.ones(num_bars) * bar_width, np.zeros(num_bars), bar_width, bar_width, data["Home Sales Completed"], color='g')
ax.bar3d(x_pos, np.ones(num_bars) * bar_width * 2, np.zeros(num_bars), bar_width, bar_width, data["Median Home Price ($000)"], color='r')

# Setting labels and title
ax.set_xticks(x_pos + bar_width)
ax.set_xticklabels(data["City"])
ax.set_xlabel('City')
ax.set_yticks(np.arange(3) * 0.2)
ax.set_yticklabels(list(data.keys())[1:], ha='left')
ax.set_zlabel('Values')
ax.set_title('Real Estate Market Summary for Major U.S. Cities')

# Setting chart title and legend
ax.set_title('Real Estate Market Summary for Major U.S. Cities')
ax.legend()

ax.view_init(elev=20., azim=-35)
fig.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/Full/3D-Bar/png_train/3D-Bar_182.png')

# clear figure
plt.clf()