import matplotlib.pyplot as plt

# Data
labels = ['Rice', 'Wheat', 'Maize', 'Soybean', 'Potato']
stats = [[2, 8, 13, 18, 25], [3, 7, 12, 17, 22], [1, 5, 10, 15, 20], [2, 6, 11, 16, 23], [4, 9, 14, 19, 24]]
outliers = [[], [1,30], [0.8, 25.5], [2.7, 24], [3.5, 27]]

# Create figure and boxplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
plt.grid(True)
ax.mirrored=True

# Boxplot
ax.boxplot(stats, labels=labels, whis=1.5, vert=False)

# Plot outliers manually
for i, outlier in enumerate(outliers):
    ax.plot(outlier, [i + 1] * len(outlier), "x")

# Axis labels
ax.set_xlabel('Yield (Tonnes)')
ax.set_title('Crop Yield Distribution in Agriculture and Food Production (2021)')

# Saving the plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/133_202312270030.png')

# Clear the current figure
plt.clf()
