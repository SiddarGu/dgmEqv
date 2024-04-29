import matplotlib.pyplot as plt

data = [
    ["Facebook", 1.0, 1.5, 2.0, 2.5, 3.0, [0.5, 3.5]],
    ["Twitter", 1.2, 1.7, 2.1, 2.6, 3.1, [0.8, 3.2]],
    ["Instagram", 0.9, 1.4, 2.0, 2.7, 3.8, [3.9, 4.2]],
    ["Snapchat", 0.6, 1.0, 1.3, 1.7, 2.0, [2.7]],
    ["LinkedIn", 0.5, 0.9, 1.2, 1.5, 1.8, [2.0, 2.2]]
]

platforms = [row[0] for row in data]
statistics = [row[1:-1] for row in data]
outliers = [row[-1] for row in data]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.boxplot(statistics, whis=1.5, vert=False)
ax.set_yticklabels(platforms)
ax.set_xlabel('Screen Time (Hours)')
ax.set_title('Social Media Screen-Time Distribution in Hours (2022)')

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i+1] * len(outlier), outlier, "ro")

ax.set_xticks(range(1, len(platforms) + 1), platforms)

ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/111_202312270030.png')

plt.clf()
