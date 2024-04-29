import matplotlib.pyplot as plt
import numpy as np

# restructure the data
data = [["Burger", 300, 500, 700, 900, 1100, []],
        ["Pizza", 200, 450, 650, 850, 1050, [1200,1300]],
        ["Sushi", 150, 300, 450, 600, 750, [900,1000]],
        ["Salad", 50, 100, 150, 200, 300, [400,500]],
        ["Pasta", 250, 400, 550, 700, 850, [950,1000]]]

statistics = [item[1:6] for item in data]
outliers = [item[6] for item in data]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

# box plot
bplot = ax.boxplot(statistics, vert=False, patch_artist=True, notch=True, whis=1.5)

# set properties
colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'plum']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# add grid
ax.yaxis.grid(True)
ax.xaxis.grid(True)

# set labels
plt.yticks(np.arange(1, len(data) + 1), [item[0] for item in data], rotation=0)
plt.xlabel('Calorie Count')
plt.ylabel('Food Item')

# set title
plt.title('Calorie Distribution of Different Food Items in Restaurants (2022)')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/77_202312270030.png')
plt.close()
