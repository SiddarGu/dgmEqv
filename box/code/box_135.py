import matplotlib.pyplot as plt

# preparing data
data = [
    ['Facebook', 2, 7, 10, 15, 25, []],
    ['Twitter', 1, 6, 11, 16, 22, [31]],
    ['Instagram', 4, 8, 12, 17, 23, [0.5,30]],
    ['LinkedIn', 3, 7, 12, 17, 24, [2,28]],
    ['YouTube', 2, 7, 13, 18, 25, [29]]
]

# restructure data
platforms = [i[0] for i in data]
stats = [i[1:6] for i in data]
outliers = [i[6] for i in data]

# create figure and add subplot
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# plot box plot
ax.boxplot(stats, whis=1.5)

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ko")

# set axis labels, title and grid
ax.set_xticklabels(platforms, rotation=30, ha='right')
ax.set_ylabel('Session Duration (Minutes)')
ax.set_title('User Session Duration Distribution on Different Social Platforms (2022)')
ax.yaxis.grid(True)
ax.xaxis.grid(True)

# save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/160_202312310058.png')
plt.clf()
