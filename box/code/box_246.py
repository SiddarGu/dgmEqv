import matplotlib.pyplot as plt

# Reshape the data into 2D lists
labels = ['Provider A', 'Provider B', 'Provider C', 'Provider D', 'Provider E']
categories = [[100, 250, 400, 550, 700], [200, 300, 500, 700, 900], [150, 350, 550, 750, 950], [250, 450, 650, 850, 1050], [300, 500, 700, 900, 1100]]
outliers = [[], [1200], [40, 1360], [1, 2, 3], [1250]]

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Boxplot
bplot = ax.boxplot(categories, vert=True, patch_artist=True, notch=True, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'red', 'purple']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

# Add a y-axis label
ax.set_ylabel('Energy Usage (kWh)')

# Mirror axes
ax.yaxis.tick_left()
ax.xaxis.tick_bottom()
ax.xaxis.set_tick_params(width=1)
ax.yaxis.set_tick_params(width=1)

# Set grid
plt.grid()

# Set x-axis labels and rotate them
ax.set_xticklabels(labels, rotation=15, wrap=True)

# Set title
ax.set_title('Energy Usage Distribution among Utility Providers (2021)')

# Save file
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/123_202312270030.png')

# Clear the current figure
plt.clf()
