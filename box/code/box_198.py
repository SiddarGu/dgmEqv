import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY

data = [["Public Health Agency", 5, 25, 50, 75, 100, []],
        ["Education Department", 15, 30, 60, 90, 120, [3, 140]],
        ["Defense Department", 20, 40, 70, 100, 130, [0.5, 150]],
        ["Social Services Department", 10, 35, 55, 75, 95, [1, 105, 115]],
        ["Transportation Department", 8, 28, 48, 68, 88, [96]]]

labels = [i[0] for i in data]
box_data = [i[1:6] for i in data]
outliers = [i[6] for i in data]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

bplot = ax.boxplot(box_data, vert=False, patch_artist=True, notch=True, labels=labels, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'purple']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'x')

ax.set_xlabel('Decision Time (Days)')
ax.set_title('Decision Time Distribution in Government Agencies (2021)')
ax.xaxis.grid(True)
ax.yaxis.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/75_202312270030.png')
plt.clf()
