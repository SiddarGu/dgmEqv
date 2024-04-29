import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Parsing the provided data
data = """Engineering Discipline,Min Project Duration (Months),Q1 Project Duration (Months),Median Project Duration (Months),Q3 Project Duration (Months),Max Project Duration (Months),Outlier Project Duration (Months)/n Chemical Engineering,4,8,12,16,20,[]/n Civil Engineering,5,9,13,17,22,[2,25]/n Mechanical Engineering,6,10,14,17,21,[3,24]/n Electrical Engineering,3,7,11,15,19,[26]/n Aerospace Engineering,4,8,14,19,23,[1,27]"""
data = [i.split(",") for i in data.split("/n")]
header = data.pop(0)
categories = [i[0] for i in data]
box_data = [[int(j) for j in i[1:6]] for i in data]

# Parsing outliers correctly, taking care to handle empty lists
outliers = []
for i in data:
    outlier_data = i[6].strip('[]')
    if outlier_data:
        outliers.append([int(x) for x in outlier_data.split(',')])
    else:
        outliers.append([])

# Creating the boxplot
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(box_data, vert=True, patch_artist=True, notch=True)

# Customize the boxplot colors
colors = ['pink', 'lightblue', 'lightgreen', 'red', 'purple']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add outliers
for i, outlier in enumerate(outliers):
    if outlier:
        x = [i + 1] * len(outlier)
        ax.plot(x, outlier, 'ro', markersize=5)

# Add grid, labels, and title
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_ylabel('Project Duration (Months)')
ax.set_title('Project Duration Distribution in Various Engineering Disciplines (2022)')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/198_202312310058.png')
plt.clf()
