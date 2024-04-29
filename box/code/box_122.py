import matplotlib.pyplot as plt

# Data
product_type = ['Vehicle', 'Furniture', 'Apparel', 'Electronics', 'Food']
production_time_stats = [[8, 16, 24, 34, 40], [5, 10, 15, 20, 25], [3, 6, 9, 12, 15], [10, 20, 30, 40, 50], [2, 4, 6, 8, 10]]
outliers = [[80], [], [20, 24], [8, 80], [12, 14]] 

# Create figure and subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Box plot
bplot = ax.boxplot(production_time_stats, notch=True, patch_artist=True, whis=1.5, showfliers=False)

# Customizing box colors
colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow', 'lightgrey']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers manually
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

# Setting grid, labels, and titles
ax.yaxis.grid(True)
ax.set_xticks([y + 1 for y in range(len(product_type))])
ax.set_xticklabels(product_type, rotation=90)
plt.title('Production Time Distribution Across Manufacturing Sectors (2022)')
plt.ylabel('Production Time (Hours)')

plt.tight_layout()  # Resize image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/214_202312310058.png')  # Save image
plt.clf()  # Clear current image state
