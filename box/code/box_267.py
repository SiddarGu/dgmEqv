
import matplotlib.pyplot as plt
import numpy as np

data = [[20,50,90,130,170],
        [15,45,80,120,150],
        [25,60,95,135,175],
        [30,70,110,140,180],
        [10,35,65,90,120]]
outliers = [[], [210], [2.5], [200,220], [190]]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)
ax.set_title('Task Completion Time Distribution in Science and Engineering Disciplines (2020)', fontsize=14)
ax.set_ylabel('Time (Seconds)', fontsize=12)
ax.set_xticklabels(['Physics', 'Computer Science', 'Chemistry', 'Engineering', 'Mathematics'], fontsize=12, rotation=45, ha='right', wrap=True)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, 'ro')

ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/13_202312251608.png')
plt.clf()