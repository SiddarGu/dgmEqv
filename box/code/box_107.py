import matplotlib.pyplot as plt

# Restructure data
categories = ['Electronics', 'Clothes', 'Health and Beauty', 'Books', 'Home Appliances']
data = [[20, 70, 110, 160, 220], [10, 35, 60, 85, 110], [15, 50, 80, 115, 150], [5, 20, 35, 50, 65], [30, 80, 130, 180, 240]]
outliers = [[500], [], [3, 250], [1, 80], [10, 300]]

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Box Plotting
bp = ax.boxplot(data, whis=1.5, patch_artist=True)

# Colors for each boxplot
colors = ['lightblue', 'lightgreen', 'pink', 'yellow', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Manual outlier plotting
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "o")

# Drawing techniques and Axes mirroring
ax.yaxis.grid(True)
ax.xaxis.grid(True)

# Y-axis label
ax.set_ylabel('Sale Price ($)')

# Title and X-axis labels
plt.title('Sale Price Distribution in Different Product Categories of E-commerce (2021)', wrap=True)
ax.set_xticklabels(categories, rotation=45, ha="right")

# Show the plot
plt.tight_layout()

# Save as png file
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/217_202312310058.png', bbox_inches='tight')
plt.show()

# Clear current image state
plt.clf()
