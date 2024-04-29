
import matplotlib.pyplot as plt
import numpy as np

# restructure data
category = ['Particulate Matter', 'Carbon Monoxide', 'Nitrogen Oxide', 'Volatile Organic Compounds', 'Sulphur Dioxide']
min_data = [50, 20, 60, 15, 30]
q1_data = [90, 50, 120, 60, 70]
median_data = [150, 90, 180, 100, 110]
q3_data = [200, 130, 240, 140, 160]
max_data = [300, 180, 320, 200, 210]
outliers_data = [[], [250], [400], [250, 350], [320, 400]]

# create figure
fig = plt.figure(figsize=(15,7))

# plot data
# transform data into 2D list
box_data = np.array([min_data, q1_data, median_data, q3_data, max_data])
ax = fig.add_subplot(1, 1, 1)
ax.boxplot(box_data)
ax.set_xticklabels(category)
ax.set_title('Pollution Concentration Distribution in the Environment (2020)')
ax.set_ylabel('Concentration (ppm)')

# plot outliers
for i, outlier in enumerate(outliers_data):
    if len(outlier) > 0:
        for outlier_value in outlier:
            ax.plot([i + 1], [outlier_value], marker='o', color='red')

# set background grid
ax.yaxis.grid(True)
ax.xaxis.grid(True)

# resize image
plt.tight_layout()
# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/5_202312251315.png')

# clear figure
plt.clf()