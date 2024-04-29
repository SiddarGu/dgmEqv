
import matplotlib.pyplot as plt
import numpy as np

# Restructure data into two 2D lists 
data = [[30, 40, 45, 50, 55],
        [35, 40, 47, 54, 60],
        [25, 32, 38, 42, 48],
        [40, 45, 52, 60, 65],
        [28, 35, 40, 45, 50]]
outliers = [[], [63], [52, 58], [70], [60]]
line_labels = ['Manager', 'Engineer', 'Accountant', 'Analyst', 'Technician']
# Create figure and plot
fig, ax = plt.subplots(figsize=(8,6))
ax.boxplot(data, whis=1.5)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.full(len(outlier), i+1), outlier, 'o', color='#000000', markersize=4)

# Draw background grid
ax.grid(axis='y', linestyle='--', alpha=0.6)
ax.set_xticklabels(line_labels)

# Set y-axis label
ax.set_ylabel('Hours Worked (Weekly)')

# Set figure title
ax.set_title('Working Hours Distribution of Different Job Titles in 2020')

# Tight layout and save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/21_202312251608.png')

# Clear current image state
plt.clf()