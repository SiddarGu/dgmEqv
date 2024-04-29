
import matplotlib.pyplot as plt
import numpy as np

# restructure data
data_list = [[20, 50, 80, 100, 120], [15, 35, 60, 85, 105], [25, 60, 90, 110, 135], [10, 25, 50, 75, 100], [15, 40, 65, 85, 105]]
outlier_list = [[], [130], [0.5, 150], [105], [130]]

# draw box plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.boxplot(data_list, whis=1.5)
ax.set_title('Budget Distribution of US Government Departments in 2021')
ax.set_ylabel('Budget (Million USD)')
ax.set_xticklabels(['Department of Justice', 'Department of Education', 'Department of Defense', 'Department of Health and Human Services', 'Department of Energy'], rotation=45, wrap=True)
for i, outlier in enumerate(outlier_list):
    if len(outlier):
        ax.plot(np.full(len(outlier), i + 1), outlier, 'ro', alpha=0.6)
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/27_202312251608.png')
plt.clf()