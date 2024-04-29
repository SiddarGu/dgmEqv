
import matplotlib.pyplot as plt
import numpy as np

y = np.array([[20, 40, 50, 60, 80], [30, 50, 70, 90, 110], [40, 60, 80, 100, 140], [10, 30, 50, 60, 80], [15, 35, 50, 65, 80]])
x_labels = ["Wheat", "Rice", "Corn", "Soybeans", "Oats"]
outliers = [[], [150], [10, 20], [90, 100], [150]]

fig, ax = plt.subplots(figsize=(8, 6))
bplot = ax.boxplot(y.T, vert=True, patch_artist=True)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        plt.plot([i+1] * len(outlier), outlier, 'go', alpha=0.3, markersize=8)

ax.set_title("Yield Distribution of Agriculture Products in 2021")
ax.set_ylabel('Yield (Tonnes)')
ax.set_xticklabels(x_labels, rotation=45, ha="right", wrap=True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/28.png')
plt.clf()