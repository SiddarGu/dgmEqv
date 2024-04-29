
import numpy as np
import matplotlib.pyplot as plt

data = [[50, 60, 70, 80, 90],
        [45, 55, 65, 75, 85],
        [40, 50, 60, 70, 80],
        [35, 45, 55, 65, 75],
        [30, 40, 50, 60, 70]]

outliers = [[], [95], [90], [85], [80]]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()

ax.boxplot(data, whis=1.5, labels=['Psychology', 'Sociology', 'Anthropology', 'Economics', 'Philosophy'], showmeans=True)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'r^')

ax.set_title('Grades Distribution in Social Sciences and Humanities in 2021')
ax.set_ylabel('Grades')
ax.grid(axis='y', alpha=0.75)

fig.tight_layout()
fig.savefig(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/21_202312270030.png')
plt.clf()