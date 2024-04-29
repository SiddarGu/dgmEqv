
import matplotlib.pyplot as plt
import numpy as np

data = [[0, 100, 250, 500, 1000], 
        [50, 200, 400, 600, 800, 1500], 
        [10, 100, 150, 300, 500, 20, 30], 
        [20, 200, 400, 600, 800, 1000, 1100], 
        [100, 500, 750, 900, 1200, 20, 30]]

outliers = [[], [1500], [20, 30], [1000, 1100], [20, 30]]

fig, ax = plt.subplots(figsize=(12, 8))

ax.boxplot([data[i][:5] for i in range(5)])

for i, outlier in enumerate(outliers):
    if outlier:
        x = [i + 1] * len(outlier)
        ax.plot(x, outlier, 'o')

ax.set_title('Government Expenditure Distribution in Public Policy in 2021')
ax.set_ylabel('Cost (USD)')
ax.set_xticklabels(['Taxation', 'Social Welfare', 'Education', 'Healthcare', 'Defense'], rotation=45, ha='right', wrap=True)
ax.grid()

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/3_202312251315.png')
plt.clf()