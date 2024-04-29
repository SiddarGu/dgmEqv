import matplotlib.pyplot as plt
import numpy as np

# define data, box and outliers data
box_data=[[2,4,7,9,12],[1,3,5,6,9],[3,5,6,8,11],[2,4,6,8,10],[1,4,6,7,9]]
outliers_data=[[],[14,18],[16,19],[],[13,20]]
category_labels = ['National Security', 'Healthcare', 'Economy', 'Education', 'Immigration']

# Create figure before plotting
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

# Box plot
bp = ax.boxplot(box_data,vert=True,patch_artist=True,labels=category_labels,whis=1.5)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#0081c2']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Outliers
for i, outlier in enumerate(outliers_data):
    if outlier: # check if outlier list is not empty
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# Axis labels and title
ax.set_xlabel('Policy Area')
ax.set_ylabel('Debate Time (Hours)')
plt.title('Debate Time Distribution across Policy Areas in Government (2021)')
ax.set_xticklabels(category_labels, rotation=45, ha='right')

# Saving plot
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/83_202312270030.png", bbox_inches='tight')

# Clear the current figure
plt.clf()
