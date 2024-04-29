
import matplotlib.pyplot as plt
import numpy as np

# restructure the data into two 2D lists
data_list = [[1000, 2000, 5000, 10000, 20000],
             [3000, 6000, 7000, 9000, 15000],
             [2500, 4000, 6000, 8000, 12000],
             [2000, 4000, 5000, 7000, 11000],
             [1500, 3000, 5000, 7000, 10000]]
outlier_list = [[], [17000], [13500, 15000], [13000], [15000]]

# create figure and add subplot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# plot the data with box plot
bp = ax.boxplot(data_list, whis=1.5, patch_artist=True)

# set the x-axis label
ax.set_xticklabels(['Instagram', 'Facebook', 'Twitter', 'LinkedIn', 'TikTok'])

# adjust plotting parameters
for box in bp['boxes']:
    box.set(color='#7570b3', linewidth=2)
    box.set(facecolor='#1b9e77')

for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

# plot the outliers
for i, outlier in enumerate(outlier_list):
    if outlier:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'o', color='#e7298a', alpha=0.6)

# set the y-axis title
ax.set_ylabel('Likes (Count)')

# add background grids
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# set the title of the figure
ax.set_title('Engagement Distribution of Social Media Platforms in 2021')

# automatically resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/46_202312270030.png')

# clear the current image state
plt.clf()