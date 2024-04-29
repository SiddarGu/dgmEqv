import matplotlib.pyplot as plt

# Data
categories = ['Urban', 'Rural', 'Forest', 'Coastal', 'Mountain']
statistics = [[5, 11, 15, 21, 28], [1, 8, 12, 18, 25], [0, 7, 10, 15, 21], [6, 13, 18, 23, 30], [-5, 0, 4, 10, 15]]
outliers = [[31], [29], [24, 28], [4, 32], [18]]

# Create the figure
fig, ax = plt.subplots(figsize=(10, 8))

# Create the box plot
bp = ax.boxplot(statistics, widths=0.4, patch_artist=True, notch=True, medianprops={'linewidth': 2})
plt.setp(bp['boxes'], facecolor='lightblue')
plt.setp(bp['whiskers'], color='darkblue', linestyle='-.')

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "o", markersize=5)

# Add grid
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Set labels
ax.set_xticklabels(categories, rotation=15)
ax.set_ylabel("Temperature (°C)")

# Mirror axes
ax.yaxis.tick_left()
ax.xaxis.tick_bottom()
ax.xaxis.set_tick_params(width=1)
ax.yaxis.set_tick_params(width=1)

# Set title
plt.title('Temperature Distribution in Different Environments (2022)')

#Fix layout and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/210_202312310058.png')

#Clear the plot
plt.clf()
