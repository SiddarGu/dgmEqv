import matplotlib.pyplot as plt
import numpy as np

# Restructured data
data = [['Organization A', [100, 300, 500, 700, 900], []],
        ['Organization B', [150, 350, 550, 750, 950], [1200]],
        ['Organization C', [200, 400, 600, 800, 1000], [1250, 1300]],
        ['Organization D', [125, 325, 525, 725, 925], [1100, 1150]],
        ['Organization E', [175, 375, 575, 775, 975], [1200, 1250]]]

labels = [item[0] for item in data]
boxes = [item[1] for item in data]
outliers = [item[2] for item in data]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

# Create box plots
bp = ax.boxplot(boxes, whis=1.5)

# Plot outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

# Set the style
ax.set_title('Donation Amount Distribution in Charity and Nonprofit Organizations (2021)')
ax.set_ylabel('Donation ($)')
ax.set_xticklabels(labels, rotation=45)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Save the figure
plt.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/167_202312310058.png')

# Clear the current image state
plt.clf()
