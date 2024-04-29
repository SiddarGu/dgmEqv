import matplotlib.pyplot as plt
import numpy as np

# original data
data = [('Maths', 62, 70, 75, 80, 95, []),
        ('English', 68, 73, 78, 84, 95, [50, 100]),
        ('Physics', 64, 70, 73, 78, 94, [52]),
        ('Chemistry', 65, 71, 76, 82, 96, [45, 100]),
        ('Biology', 63, 68, 72, 79, 92, [60, 100])]

# data restructuring
main_data = [[item[1], item[2], item[3], item[4], item[5]] for item in data]
outliers = [item[6] for item in data]
labels = [item[0] for item in data]

# make the figure
plt.figure(figsize=(10,6))
ax = plt.gca()

# box plotting
ax.boxplot(main_data, whis=1.5, vert=False)

# plotting outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")  # 'ro' means red circle

# set grid
ax.grid(True)

# set labels and title
ax.set_yticklabels(labels, fontsize=12)
ax.set_xlabel('Grade', fontsize=12)
plt.title('Grade Distribution in Different Academic Subjects (2022)', fontsize=14)

# resize the image
plt.tight_layout()

# save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/112_202312270030.png')

# clear the figure
plt.clf()
