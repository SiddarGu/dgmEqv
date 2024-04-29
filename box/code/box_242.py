

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
data = [[5, 15, 25, 35, 50], [10, 20, 30, 40, 60], [7, 17, 27, 37, 55], [12, 22, 32, 42, 65], [8, 18, 28, 38, 48]]
outliers = [[], [100], [2, 80], [75], [60, 70]]

# Plot the graph
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
bp = ax.boxplot(data, whis=1.5, patch_artist=True, medianprops={'color':'red'})

# Set boxplot color
for patch, color in zip(bp['boxes'], ['deepskyblue', 'royalblue', 'navy', 'blue', 'dodgerblue']):
    patch.set_facecolor(color)

# Plot the outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, 'o', color='black')

# Set grid
ax.yaxis.grid(True, linestyle='--', which='major', color='black', alpha=0.25)
ax.set_axisbelow(True)

# Set labels
ax.set_xticklabels(['Country A', 'Country B', 'Country C', 'Country D', 'Country E'])
ax.set_title('Carbon Footprint Distribution in Countries (2021)')
ax.set_ylabel('Tons')

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/15_202312251608.png')

# Clear the current image state
plt.clf()