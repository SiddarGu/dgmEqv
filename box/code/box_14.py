
import matplotlib.pyplot as plt
import numpy as np

data =[[30, 60, 90, 120, 150],
            [25, 50, 80, 110, 140, 200],
            [20, 40, 70, 100, 130, 5, 40],
            [10, 35, 60, 85, 110, 180],
            [15, 45, 75, 105, 135, 160]]
outliers = [data[i][5:] if len(data[i]) > 5 else [] for i in range(len(data))]
# Create and set up the figure
plt.figure(figsize=(10, 8))
ax = plt.subplot()
# Set figure title
plt.title("Funding Distribution in School Districts in 2021")
# Set x-axis label
ax.set_xlabel("School Districts")
# Set y-axis label
ax.set_ylabel("Funding (Million)")
# Plot data as boxplot
ax.boxplot(np.array([data[i][:5] for i in range(5)]).T,
           labels=["District A", "District B", "District C", "District D", "District E"])
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i+1] * len(outlier), outlier, 'ro', alpha=0.6)
# Automatically resize the image
plt.tight_layout()
# Save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/9.png")
# Clear the current image state
plt.clf()