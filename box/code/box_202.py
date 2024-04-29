import matplotlib.pyplot as plt

# data
categories = ['Wheat', 'Rice', 'Corn', 'Soybeans', 'Sugarcane', 'Coffee']
data = [[3, 5, 7, 10, 13], [4, 6.5, 8.5, 11, 14], [2, 4, 6, 9, 12], [1, 2.5, 4, 5.5, 7], [80, 100, 120, 140, 160], [0.5, 1.0, 2.0, 3.0, 3.5]]
outliers = [[], [20], [1, 16], [10], [200], [5]]

# create figure
fig = plt.figure(figsize=(12, 8))

# add subplot
ax = fig.add_subplot(111)

# box plot
bplot = ax.boxplot(data, vert=True, patch_artist=True, labels=categories, whis=1.5)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF', '#FF0000']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'x')

# set axes labels
ax.set_xlabel('Crop')
ax.set_ylabel('Yield (Ton/ha)')

# set grid
ax.yaxis.grid(True)
ax.xaxis.grid(True)

# set title
ax.set_title('Yield Distribution of Key Crops in 2022')

# save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/229_202312310058.png')

# clear
plt.clf()
