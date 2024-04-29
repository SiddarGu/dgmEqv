
import numpy as np
import matplotlib.pyplot as plt

# Restructure the data into two 2D lists
data = [[15,45,60,75,90], [30,60,90,120,150], [8,20,30,40,50], [10,25,35,45,60], [20,40,60,80,100]]
outliers = [[], [250], [75,90], [70,80,90], [120]]

# Plot the data
fig = plt.figure(figsize=(12,8))
axes = fig.add_subplot(111)
axes.boxplot(data, widths=0.5, whis=1.5)

# Plot the outliers
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        x = np.repeat(i + 1, len(outlier))
        axes.plot(x, outlier, "bx")

axes.set_xticklabels(["Painting", "Sculpture", "Music", "Dance", "Theater"])
axes.set_title("Performance Duration Distribution in Arts and Culture (2021)")
axes.set_ylabel("Duration (Minutes)")
axes.grid(linestyle='--')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/8_202312270030.png")

# Clear the current image state
plt.clf()