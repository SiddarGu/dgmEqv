import matplotlib.pyplot as plt
import numpy as np

# Data for the box plot
subjects = ["Philosophy", "History", "Linguistics", "Literature", "Sociology"]
data = [[4, 9, 14, 20, 27], [3, 7, 12, 17, 23], [5, 11, 16, 22, 28], [6, 10, 14, 19, 24], [5, 9, 13, 18, 24]]
outliers = [[2, 32], [1, 25], [30, 35], [3, 29], [3, 28]]

# Create figure and axis
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Create boxplot
bp = ax.boxplot(data, patch_artist=True, whis=1.5)

# Set colors for each box
colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    ax.plot([i + 1] * len(outlier), outlier, 'x')

# Set labels and title
ax.set_xticklabels(subjects, rotation=45)
ax.set_ylabel('Study Time (Hours)')
ax.set_title('Study Time Distribution in Humanities Subjects (2021)')

# Show grid
ax.yaxis.grid(True)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/188_202312310058.png')

# Clear the figure
plt.clf()

