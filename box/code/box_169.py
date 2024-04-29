import matplotlib.pyplot as plt

# Prepare the data
data = {
    "Wheat": [[1.0, 3.5, 6.0, 8.5, 11.0], []],
    "Rice": [[1.2, 2.5, 4.0, 6.5, 9.0], [15.0]],
    "Corn": [[1.5, 4.1, 6.7, 9.3, 12.0], [0.6, 14.5]],
    "Soybean": [[1.1, 3.2, 5.3, 7.4, 9.5], [1.5]],
    "Cotton": [[0.8, 2.4, 4.0, 6.0, 8.0], [12.9]],
}

# Restructure the data
yield_data, outliers = list(zip(*data.values()))
labels = data.keys()

# Create figure and subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Create box plot
bps = ax.boxplot(yield_data, whis=1.5, vert=False, patch_artist=True, labels=labels)

colors = ['lightblue', 'lightgreen', 'lightpink', 'yellow', 'lightgrey']
for patch, color in zip(bps['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ro')

# Set title and labels
ax.set_xlabel('Yield (Tonnes)')
ax.set_title('Yield Distribution of Major Crops in Agricultural Production (2020)')
plt.grid(alpha=0.4)

# Save the plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/96_202312270030.png')

# Clear the figure
plt.clf()
