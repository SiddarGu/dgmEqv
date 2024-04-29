
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Restructure data into 2D lists
data = [[2, 3, 4, 5, 6], [2.5, 4, 5.5, 7, 9], [1, 2, 3, 4, 5], [1.5, 2.5, 3.5, 4.5, 6], [3, 4.5, 6, 7.5, 9]]
outliers = [[], [10], [6, 7], [7.5, 8.5], [2]]

# Plot the data
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.set_title('Entertainment Duration Distribution in 2020')
ax.set_ylabel('Duration (Hours)')

labels = ['Movies', 'TV Series', 'Music', 'Online Games', 'Live Events']
ax.boxplot(data, whis=1.5, labels=labels)

# Draw outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.full(len(outlier), i+1), outlier, 'r^')

# Draw background grids
ax.grid(axis='y', alpha=0.75)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/28_202312270030.png')

# Clear current image state
plt.clf()