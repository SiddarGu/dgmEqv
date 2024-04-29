
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

#restructure the data
products = ['Clothing', 'Electronics', 'Furniture', 'Toys', 'Appliances']
min_time = [5,4,10,6,7]
q1_time = [15,12,20,18,17]
median_time = [25,20,30,24,27]
q3_time = [35,30,40,32,37]
max_time = [45,40,50,40,47]
outliers = [[], [50], [6,7], [60], [48]]

# set figure
fig = plt.figure(figsize=(18,8))
ax = fig.add_subplot(111)

#plot the data
ax.boxplot(np.array([min_time,q1_time,median_time,q3_time,max_time]),
            notch=True,
            patch_artist=True,
            boxprops=dict(facecolor='coral', color='black'),
            capprops=dict(color='black', linewidth=2),
            whiskerprops=dict(color='black', linewidth=2),
            flierprops=dict(markerfacecolor='red', markersize=12))

#iterate through the outliers
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.ones(len(outlier)) * (i+1), outlier, 'ro', alpha=0.6)

#add background grids
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Set x-axis
ax.set_xticklabels(products, rotation=45, ha='right', wrap=True)
ax.set_xlabel('Product Type')

# Set y-axis
ax.set_ylabel('Production Time (Hours)')

# Set title
ax.set_title('Production Time Distribution of Different Products in 2021')

#Resize image
plt.tight_layout()

#Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/8_202312251315.png')

#clear the current image state
plt.clf()