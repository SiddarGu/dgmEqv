import matplotlib.pyplot as plt

# Data setup
categories = ["Personal Injury", "Criminal Defense", "Bankruptcy", "Business Law", "Employment Law"]
data = [[45, 90, 115, 135, 150], [60, 85, 95, 105, 120], [30, 75, 95, 115, 140], [50, 70, 85, 100, 115], [40, 80, 100, 120, 145]]
outliers = [[200], [150], [], [30, 45], [170]]

# Create figure and add sub plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Box plot with custom properties
bplot = ax.boxplot(data, patch_artist=True, notch=True, vert=1, whis=1.5)

# Set colors for each box
colors = ['pink', 'lightblue', 'lightgreen', 'yellow', 'purple']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

# Set x-axis labels and title
ax.set_xticklabels(categories, rotation=15)
plt.title('Processing Time Distribution in Different Case Types in 2022')
plt.ylabel('Processing Time (Days)')

# Add grid
plt.grid(True)

# Save and clear
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/202_202312310058.png')
plt.clf()
