
import matplotlib.pyplot as plt
import numpy as np

data = [[4, 10, 15, 20, 30], [3, 7, 11, 17, 28], [2, 5, 9, 13, 22], [6, 11, 16, 21, 35], [5, 9, 14, 19, 24]]
outliers = [[], [35], [27, 40], [2, 3], [39]]

fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot()
ax.boxplot(data, whis=1.5)

labels = ['Flu', 'Cold', 'Allergies', 'Pneumonia', 'Bronchitis']
ax.set_xticklabels(labels, fontsize=14)
ax.set_ylabel('Recovery Time (Days)', fontsize=14)
ax.set_title('Recovery Time Distribution For Common Diseases in 2020', fontsize=16)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, 'r.', markersize=10)

ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/47_202312251608.png')

plt.clf()