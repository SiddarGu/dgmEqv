
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = [[1000, 3000, 5000, 7000, 15000],
        [2000, 4000, 6000, 8000, 14000],
        [1500, 3000, 5000, 7000, 12000],
        [2500, 4500, 6500, 8500, 13000],
        [1000, 3000, 5000, 7000, 11000]]

outliers = [[],
            [20000],
            [0.5, 18000],
            [15500],
            [18000]]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

ax.set_title('Project Cost Distribution in Engineering Fields (2021)')
ax.set_ylabel('Cost (Dollars)')

category = ['Construction', 'Chemical', 'Mechanical', 'Electrical', 'Computer']
ax.boxplot(data, whis=1.5, labels=category)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i + 1] * len(outlier), outlier, 'r*')

sns.set_style('whitegrid')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/18_202312251608.png')
plt.clf()