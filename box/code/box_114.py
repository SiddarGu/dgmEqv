import matplotlib.pyplot as plt

# data
categories = ['Electronics', 'Clothing', 'Home and Kitchen', 'Health and Beauty', 'Toys and Games']
data = [[2.2, 7.5, 10.0, 12.5, 16.0], [3.0, 5.7, 8.2, 10.7, 13.2], [3.5, 6.8, 9.3, 11.8, 14.3], 
        [2.0, 6.1, 8.6, 11.1, 15.1], [1.5, 5.6, 7.0, 8.4, 10.0]]
outliers = [[], [20.6], [0.02, 22.9, 23.6], [4.6, 18.5], [12.8]]

# plot settings
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

bp = ax.boxplot(data, labels=categories, patch_artist=True, notch=True, vert=1, whis=1.5)
plt.setp(bp['boxes'], color='blue')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "rx")

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',alpha=0.5)
ax.set_axisbelow(True)
ax.set_title('E-commerce Sales Distribution in Product Categories (2021)')
ax.set_ylabel('Sales (Million $)')
plt.xticks(rotation=45)

# save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/233_202312310058.png')
plt.clf()
