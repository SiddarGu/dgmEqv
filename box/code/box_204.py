
import matplotlib.pyplot as plt
import numpy as np

# Restructure data
data_labels = ["Automated Production", "Industrial Manufacturing", "Mass Production", "Custom Manufacturing", "Hand Crafting"]
data_min = [3, 4, 2, 5, 6]
data_q1 = [5, 6, 4, 7, 8]
data_median = [7, 8, 6, 9, 10]
data_q3 = [9, 10, 8, 11, 12]
data_max = [12, 14, 10, 14, 16]
data_outlier = [[], [20], [8.5, 15], [19], [17]]

# Plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.boxplot([data_min, data_q1, data_median, data_q3, data_max], labels=data_labels)

# Plot outliers
for i, outlier in enumerate(data_outlier):
    if outlier:
        ax.plot([i] * len(outlier), outlier, "ro")

# Add grids
ax.yaxis.grid(True, linestyle="--", which="major", color="gray", alpha=0.5)

# Add labels
ax.set_title("Production Time Distribution in Manufacturing Types (2020)")
ax.set_ylabel("Time (Hours)")
ax.set_xticklabels(data_labels, rotation=30, ha="right", wrap=True)

# Resize image
plt.tight_layout()

# Save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/2_202312251315.png")

# Clear image
plt.clf()