
# import libraries
import matplotlib.pyplot as plt
import numpy as np

# restructure data
data = [[5000, 10000, 15000, 20000, 25000],
        [4500, 8000, 14000, 18000, 22000],
        [7000, 11000, 16000, 21000, 26000],
        [4000, 9000, 13000, 17000, 21000],
        [5500, 10000, 15000, 20000, 25000]]

outlier = [[], [30000], [500, 35000], [27000], [32000]]
line_labels = ['Project A', 'Project B', 'Project C', 'Project D', 'Project E']

# plot data
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

# add outlier
for i, d in enumerate(outlier):
    if len(d) != 0:
        ax.plot([i + 1] * len(d), d, 'o')

# draw background grids
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

# set labels
ax.set_xlabel('Engineering Project')
ax.set_xticklabels(line_labels)

ax.set_ylabel('Cost (USD)')
ax.set_title('Cost Distribution of Engineering Projects in 2020')

# resize image
plt.tight_layout()

# save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/23_202312270030.png')

# clear image state
plt.cla()
plt.clf()
plt.close()