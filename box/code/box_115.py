import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

# Restructure the data:
crop_yield = [["Wheat", [10, 30, 50, 70, 100]], 
              ["Corn", [15, 40, 60, 80, 120]],
              ["Rice", [20, 38, 56, 75, 100]], 
              ["Soybean", [14, 32, 48, 65, 90]], 
              ["Barley", [12, 29, 47, 64, 85]]]
outliers = [[], [3, 150], [2, 4], [], [97, 100]]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
ax.set_title('Crop Yield Distribution in Agricultural Production (2022)')
ax.set_ylabel('Yield (Tons)')

# Boxplot:
bp = ax.boxplot([item[1] for item in crop_yield], whis=1.5, patch_artist=True, meanline=True, showmeans=True, widths=0.6)

# Adding outliers
for i, outlier in enumerate(outliers):
    if outlier:  # if the outlier list is not empty
        ax.plot([i + 1] * len(outlier), outlier, "ro", markersize=4)

# Apply labels
ax.set_xticklabels([item[0] for item in crop_yield], rotation=30, ha='right')

plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/208_202312310058.png')
plt.clf()
