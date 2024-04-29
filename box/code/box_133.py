
import matplotlib.pyplot as plt
import numpy as np

data = [[45, 60, 75, 90, 105], [35, 45, 55, 65, 75], [40, 55, 70, 85, 100], [40, 45, 50, 60, 75], [20, 30, 40, 50, 60]]
outliers = [[], [90], [110], [90, 100], []]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

labels = ['Management', 'Analyst', 'Engineer', 'Sales', 'Support']
bp = ax.boxplot(data, labels=labels, whis=1.5, showmeans=True, meanline=True)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro', alpha=0.6)

ax.grid(linestyle='dashed')
ax.set_ylabel('Hours (Weekly)')
ax.set_title("Working Hours Range for Different Employee Roles in Human Resources and Employee Management")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/47_202312270030.png')

plt.clf()