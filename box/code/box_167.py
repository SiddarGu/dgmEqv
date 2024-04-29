import matplotlib.pyplot as plt

# Data
data = [
    ["New York", 150, 250, 350, 450, 600, []],
    ["Los Angeles", 130, 230, 330, 430, 550, [700]],
    ["Chicago", 100, 200, 300, 400, 500, []],
    ["Miami", 120, 220, 320, 420, 540, [650]],
    ["Boston", 140, 240, 340, 440, 560, [10, 15]],
]

# Restructure data
data_stats = [d[1:6] for d in data]
data_outliers = [d[6] for d in data]
labels = [d[0] for d in data]

# Create plot
fig, ax = plt.subplots(figsize=(10, 5))
bp = ax.boxplot(data_stats, whis=1.5, patch_artist=True, notch=True)

# Customizing boxplot colors
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers manually
for i, outlier in enumerate(data_outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Labels, title, and grid
plt.xticks(range(1, len(labels) + 1), labels, rotation=45)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.ylabel("Price in Thousands")
plt.title("House Price Distribution in Major US Cities (2020)")

# save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/225_202312310058.png')

# clear figure
plt.clf()
