import matplotlib.pyplot as plt

# restructuring the data
categories = ['Fast Food Joint', 'Casual Dining', 'Fine Dining', 'Pubs & bars', 'Café & Bakeries']
data = [[2, 8, 10, 12, 15], [10, 15, 20, 25, 30], [20, 35, 45, 55, 65], [7, 10, 15, 18, 25], [5, 7, 10, 12, 15]] 
outliers = [[], [5, 35], [85], [2, 30], [1, 20]]

# create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# plot data
ax.boxplot(data, whis=1.5, vert=False, patch_artist=True)

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ro')

# labels and title
plt.yticks(range(1, len(categories) + 1), categories)
plt.xlabel('Serving Time (Minutes)')
plt.title('Serving Time Distribution in Different Types of Restaurants (2021)')

# background grid and axes
plt.grid()
ax.set_axisbelow(True)

# save chart
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/148_202312270030.png')

# clear chart
plt.clf()
