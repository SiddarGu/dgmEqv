

import matplotlib.pyplot as plt

data = [[2,6,10,14,18],
        [3,7,11,15,19],
        [4,8,12,16,20],
        [1,5,9,13,17],
        [3,7,10,14,18]]
outliers = [[], [22], [1,23], [21], [19,20]]
line_labels = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)
ax.set_title('Delivery Time Distribution in Transport Companies (2021)')
ax.set_xticklabels(line_labels)
ax.set_ylabel('Delivery Time (Hours)')
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')
ax.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/26_202312270030.png')
plt.close(fig)