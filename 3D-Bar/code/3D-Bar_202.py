import matplotlib.pyplot as plt
import numpy as np

# Sample data for Research and Innovation in Various Engineering Departments
data = {
    "Department": ["Computer Science", "Mechanical Engineering", "Chemical Engineering", "Electrical Engineering", "Civil Engineering"],
    "Research Projects Approved": [25, 30, 32, 35, 28],
    "Patents Filed": [30, 28, 35, 45, 34],
    "Research Reports Published": [50, 45, 48, 60, 40]
}

# Number of bars per group and bar width
num_bars = len(data["Department"])
bar_width = 0.2

# X positions for the groups
x_pos = np.arange(num_bars)

# Create 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting each data series
ax.bar3d(x_pos, np.zeros(num_bars), np.zeros(num_bars), bar_width, bar_width, data["Research Projects Approved"], color='b')
ax.bar3d(x_pos, np.ones(num_bars) * bar_width, np.zeros(num_bars), bar_width, bar_width, data["Patents Filed"], color='g')
ax.bar3d(x_pos, np.ones(num_bars) * bar_width * 2, np.zeros(num_bars), bar_width, bar_width, data["Research Reports Published"], color='r')

# Setting labels and title
ax.set_xticks(x_pos + bar_width)
ax.set_xticklabels(data["Department"])
ax.set_xlabel('Department')
ax.set_yticks(np.arange(3) * 0.2)
ax.set_yticklabels(list(data.keys())[1:], ha='left')
ax.set_zlabel('Values')
ax.set_title('Research and Innovation in Various Engineering Departments')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/Full/3D-Bar/png_train/3D-Bar_202.png')
plt.clf()