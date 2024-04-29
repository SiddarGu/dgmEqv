import matplotlib.pyplot as plt

# restructured data
categories = [['Harvard Law School', 75, 80, 88, 95, 100], ['Yale Law School', 78, 82, 89, 96, 98],
              ['Stanford Law School', 77, 83, 89, 94, 99],
              ['Cambridge Law School', 80, 85, 88, 93, 99], ['Oxford Law School', 76, 80, 86, 91, 98]]
outliers = [['120'], [], ['101'], ['102'], ['103']]

category_names = [category[0] for category in categories]
data = [category[1:] for category in categories]

# converting outliers to numbers
outliers = [[int(j) for j in i] for i in outliers]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# boxplot
bplot = ax.boxplot(data, notch=True, vert=False, patch_artist=True, labels=category_names, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'plum']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# plotting outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

ax.set_xlabel('Pass Rate (%)')
ax.set_ylabel('Law School')
ax.set_title('Law School Examination Pass Rate Distribution (2021)')

ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
fig.autofmt_xdate(rotation=30)
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/85_202312270030.png')
plt.clf()
