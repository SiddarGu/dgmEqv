
import matplotlib.pyplot as plt
import numpy as np

# restructure the data into two 2D lists
data = [[1000, 3000, 5000, 7000, 10000], [500, 1500, 3000, 5000, 7000], [500, 1500, 2500, 4000, 6000], [500, 2000, 4000, 6000, 8000], [200, 500, 1000, 1500, 2000]]
outliers = [[], [20000], [50, 150, 10000], [16000], [3000]]

# plot the boxplot
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

# set the whis parameter as 1.5 in ax.boxplot
ax.boxplot(data, whis=1.5)

# manual outliers plotting
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# set title, labels and grid
ax.set_title('Followers Distribution on Different Social Networks in 2020')
ax.set_ylabel('Followers (Number)')
ax.set_xticklabels(['Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok'], fontsize=10, rotation=30)
ax.yaxis.grid(True)

# auto resize
plt.tight_layout()

# save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/17_202312270030.png')

# clear the current image state
plt.clf()