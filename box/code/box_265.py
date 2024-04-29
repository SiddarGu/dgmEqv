import matplotlib.pyplot as plt
import numpy as np

# Data
crop_data = [['Wheat',70,85,90,95,100,[]], ['Rice',100,110,120,130,150,[80,180]], ['Corn',60,70,80,90,110,[150]], ['Soybean',80,90,100,110,130,[70,140]], ['Sugar Cane',270,280,300,320,360,[400]]]

# Restructure Data
box_data = [item[1:6] for item in crop_data]
outliers_data = [item[6] for item in crop_data]
labels = [item[0] for item in crop_data]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

bp = ax.boxplot(box_data, patch_artist=True, notch=True, vert=1, whis=1.5)
colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#FF0000']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

for i, outliers in enumerate(outliers_data):
    if outliers:
        ax.plot([i + 1] * len(outliers), outliers, "x")

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.7)
ax.set_axisbelow(True)
ax.set_title('Growth Time Distribution for Key Agriculture Crops in 2021')
ax.set_xlabel('Crop')
ax.set_ylabel('Growth Time (Days)')
plt.setp(ax,xticks=[i + 1 for i,_ in enumerate(labels)],xticklabels=labels)
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/222_202312310058.png')
plt.close(fig)
