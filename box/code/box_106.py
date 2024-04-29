import matplotlib.pyplot as plt
import numpy as np

# Raw data
data=[
    ["Europe", 7, 10, 14, 18, 26, []],
    ["North America", 0, 7, 10, 15, 25, [32,35]],
    ["Asia", 12, 21 ,26 ,31, 38, []],
    ["Africa", 20, 24, 27, 32, 38, [42]],
    ["Australia", 15, 18, 24, 30, 39, [45]]
]

regions = [region[0] for region in data]

# Separate numerical data and outliers into two 2D lists
all_data = [region[1:-1] for region in data]
all_outliers = [region[-1] for region in data]

fig = plt.figure(figsize=(12,8))  # Create a figure
ax = fig.add_subplot(111)  # Add the plotting axes

# Create boxplot
bp = ax.boxplot(all_data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Put regions as y-tick labels
ax.set_yticklabels(regions)

# Iteratively plot the outliers
for i, outlier in enumerate(all_outliers):
    if outlier:  # If the outliers list is not empty
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# Set labels and title
ax.set_ylabel('Region')
ax.set_title('Annual Temperature Distribution Among Continents (2020)')

# Draw background grid and mirroring the axes
ax.grid(True)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/67_202312270030.png")

plt.clf()  # Clear the current image state
