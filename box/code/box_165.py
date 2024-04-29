import matplotlib.pyplot as plt
import numpy as np

# data
categories = ['The Red Lobster', 'Fine Dine', 'Taco Bells', 'Mediterraneana', 'Dragon\'s Cuisine']
box_data = [[10, 20, 30, 40, 45], [15, 25, 35, 45, 55], [12, 22, 32, 42, 52], [20, 30, 40, 50, 60], [18, 28, 38, 48, 58]]
outliers = [[2, 60], [], [5], [], [62, 65]]

fig = plt.figure(figsize=(10, 7))  # create figure
ax = fig.add_subplot(111)  # add subplot

# boxplot
bp_dict = ax.boxplot(box_data,
                     vert=False,
                     patch_artist=True,
                     notch=True,
                     whis=1.5,  # set whis as 1.5
                     widths=0.7,
                     labels=categories)

colors = ['lightblue', 'pink', 'lightgreen', 'yellow', 'orchid']
for patch, color in zip(bp_dict['boxes'], colors):
    patch.set_facecolor(color)

# iterate the outliers
for i, outlier in enumerate(outliers):
    ax.plot(outlier, [i + 1] * len(outlier), 'ko', markersize=3)  # plot outliers

# set grid and mirror axes
ax.grid(True, which='both', color='gray', linewidth=0.5)
ax.set_axisbelow(True)
ax.xaxis.set_tick_params(top=True, direction='inout', which='both')
ax.yaxis.set_tick_params(right=True, direction='inout', which='both')

# set labels
ax.set_xlabel('Meal Preparation Time (Minutes)')
ax.set_title('Meal Preparation Time across Restaurants in the Food and Beverage Industry')

# save the plot
plt.tight_layout()  # resize the image automatically
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/62_202312270030.png', dpi=300)
plt.clf()
