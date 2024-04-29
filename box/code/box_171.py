
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[2.0, 2.5, 3.0, 3.5, 4.0], [2.2, 2.8, 3.2, 3.8, 4.5], [2.5, 3.0, 3.6, 4.2, 4.9], [1.8, 2.4, 2.9, 3.4, 4.0], [1.5, 2.2, 2.7, 3.2, 3.6]]
outliers = [[], [1.2], [1.3, 2.0], [4.6, 5.0], [4.3]]
line_labels = ['Bachelor Degree', 'Master Degree', 'Doctoral Degree', 'Professional Degree', 'Certificate']
# Plot the data with the type of box plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Box plotting of each category
ax.boxplot(data, whis=1.5)

# Plot outliers manually
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro', alpha=0.6)

# Drawing techniques such as background grids
ax.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xticklabels(line_labels)

# Set y-axis title
ax.set_ylabel('GPA (Scale 0-4)')

# Set title of the figure
ax.set_title('GPA Distribution of Different Education Types in 2021')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/20_202312270030.png')
plt.clf()