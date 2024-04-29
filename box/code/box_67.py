import matplotlib.pyplot as plt
import numpy as np

# Data
departments = ["Accounting", "IT", "Marketing", "HR", "Sales"]
data = [[22, 25, 30, 33, 38], [23, 27, 32, 34, 38], [24, 28, 32, 36, 40], [25, 29, 34, 37, 41], [26, 30, 33, 37, 41]]
outliers = [[], [40], [41, 43], [45, 47], [23, 49]]

# Figure and axis
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Boxplot
bp = ax.boxplot(data, vert=False, widths=0.6, patch_artist=True, notch=True, bootstrap=5000, showmeans=False)

# Outliers
for i, outlier in enumerate(outliers):
    if outlier:
        # Ensuring the outliers align with the correct boxplot
        ax.plot(outlier, [i + 1] * len(outlier), "ro", markersize=8)

# Labels
ax.set_yticklabels(departments)
ax.set_xlabel('Employee Age')
ax.set_ylabel('Department')

# Grid and title
ax.grid(True)
ax.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.7)
ax.set_title('Employee Age Distribution Across Different Departments')

# save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/51_202312270030.png')

# Clear the current axes.
plt.cla() 
