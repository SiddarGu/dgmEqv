
import matplotlib.pyplot as plt
import numpy as np

data =[[135000,155000,175000,195000,215000],
       [110000,120000,130000,140000,150000],
       [95000,105000,115000,125000,135000],
       [120000,130000,145000,155000,165000],
       [200000,220000,230000,240000,250000]]
outliers = [[], [350000], [14000,90000], [180000], []]

# Set up figure
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot()

# Plot boxplots
ax.boxplot(data, whis=1.5, showmeans=True, showfliers=False, patch_artist=True)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        x_outlier = [i + 1] * len(outlier)
        ax.plot(x_outlier, outlier, "o", color="black")

# Set labels
labels = ["Single Family Home", "Apartment", "Condo", "Townhouse", "Vacation Home"]
ax.set_xticklabels(labels, rotation=30, va="top", ha="right", wrap=True)
ax.set_ylabel("Property Price (USD)")

# Set background grid
ax.grid(linestyle="--", alpha=0.7)
ax.set_title("Property Price Distribution in the Real Estate Market in 2020")

# Set layout
plt.tight_layout()

# Save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/3_202312251608.png")

# Clear figure state
plt.clf()