import matplotlib.pyplot as plt

# Data
data = [
  ["Environmental Policy", 10, 30, 50, 70, 90, []],
  ["Education Policy", 18, 38, 58, 78, 100, [115]],
  ["Health Policy", 20, 40, 60, 80, 120, [150]],
  ["Fiscal Policy", 25, 45, 75, 95, 130, [7, 140]],
  ["Social Policy", 15, 35, 65, 85, 110, [125, 135]]
]

# Extracting distribution and outlier data, and labels as separate lists
labels = [item[0] for item in data]
distribution_data = [item[1:-1] for item in data]
outlier_data = [item[-1] for item in data]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

# Creating box plots
bplot = ax.boxplot(distribution_data, vert=True, patch_artist=True, labels=labels, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'purple', 'orange']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Plotting outliers
for i, outliers in enumerate(outlier_data):
    if outliers:
        ax.plot([i + 1] * len(outliers), outliers, "ro")

ax.set_xlabel('Policy Area')
ax.set_ylabel('Decision Time (Days)')
ax.set_title('Decision Time Distribution in Different Policy Areas (2019-2021)')

ax.grid(True)
ax.margins(0.05)
ax.set_xticklabels(labels, rotation=30, ha='right')

# Saving using given path
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/238_202312310058.png')
plt.clf()
