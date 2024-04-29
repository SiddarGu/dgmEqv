import matplotlib.pyplot as plt

# Data
data = [['Hotel A', [1, 2, 3, 4, 5], []],
        ['Hotel B', [2, 3, 4, 5, 6], [7, 8]],
        ['Hotel C', [1, 2, 3, 4, 5], [0.5, 6, 7]],
        ['Hotel D', [1, 2, 3, 7, 10], [0.8, 11]],
        ['Hotel E', [3, 4, 5, 6, 7], [15]]]

# Restructure data and extract labels
labels = [i[0] for i in data]
boxplot_data = [i[1] for i in data]
outliers = [i[2] for i in data]

# Chart
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Boxplot
bplot = ax.boxplot(boxplot_data, vert=True, patch_artist=True, labels=labels, whis=1.5)

# Iterate over outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Chart styles
colors = ['pink', 'lightblue', 'lightgreen', 'purple', 'yellow']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
    
ax.yaxis.grid(True)
ax.xaxis.grid(False)

plt.title("Guest Staying Night Distribution in Hotels (2022)")
plt.ylabel("Stay Nights")
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
fig.tight_layout()

# Save
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/204_202312310058.png")

# Clear 
plt.clf()
