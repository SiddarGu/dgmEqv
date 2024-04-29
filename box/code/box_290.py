import matplotlib.pyplot as plt
import numpy as np

# set your data
data = [["Chemical Engineering", 20, 40, 55, 70, 85, [100, 110]], 
        ["Civil Engineering", 18, 35, 50, 60, 80, [90, 100]], 
        ["Electrical Engineering", 24, 41, 56, 69, 83, []], 
        ["Mechanical Engineering", 21, 38, 50, 65, 80, [120]], 
        ["Aerospace Engineering", 22, 37, 53, 65, 75, [90, 95]]]

# separate the data into two lists
box_data = [d[1:6] for d in data]
outliers = [d[6] for d in data]

# set up figure and axis
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)

# apply box plot
ax.boxplot(box_data, vert=False, notch=True, patch_artist=True, whis=1.5)
ax.set_yticklabels([d[0] for d in data])

# plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ro')

# set background grid
ax.grid(True)

# set axes properties
ax.set_title("Project Duration Distribution in Engineering Disciplines (2015-2020)")
ax.set_xlabel("Project Duration (Weeks)")
ax.set_ylabel("Engineering Discipline")

# save the figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/132_202312270030.png")

# clear the current figure
plt.clf()
