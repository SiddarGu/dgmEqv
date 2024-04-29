
import matplotlib.pyplot as plt
import numpy as np

# Transform data
y_values = ["Math Scores", "English Scores", "Science Scores"]
x_values = ["5th", "6th", "7th", "8th", "9th"]
data = np.array([[75, 80, 90], [80, 85, 95], [85, 90, 95], [90, 85, 95], [95, 90, 95]])

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.3, 0.3, data[:, i], color = '#00a2ae', alpha = 0.7)

# Set X, Y labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)

# Set title
ax.set_title('Academic Performance in Math, English, and Science by Grade Level')

# Resize and save
fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/34_202312251044.png')

# Clear figure state
plt.clf()