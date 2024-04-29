
import matplotlib.pyplot as plt
import numpy as np

data = [[30, 35, 40, 45, 50], 
            [25, 30, 35, 40, 45, 60], 
            [20, 25, 30, 35, 40, 50, 70], 
            [35, 40, 45, 50, 55, 60], 
            [40, 45, 50, 55, 60, 70]]

outliers = [data[i][5:] if len(data[i]) > 5 else [] for i in range(len(data))]
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.set_title('Working Hours Distribution by Department in Human Resources and Employee Management')
ax.boxplot(np.array([data[i][:5] for i in range(5)]).T, 
           labels=['Engineering', 'Accounting', 'Management', 'Sales', 'Customer Service'])

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i+1] * len(outlier), outlier, 'go', alpha=0.3, markersize=8)

ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/24.png')
plt.clf()