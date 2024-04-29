

import matplotlib.pyplot as plt
import numpy as np

data = [[10,25,35,50,100],
        [30,45,60,75,150],
        [20,35,50,75,125],
        [15,30,45,60,95],
        [25,40,55,70,110]]
outliers = [[], [200], [15,175], [180], [190]]

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot()
ax.boxplot(np.array(data).T)
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')
ax.set_title('Price Variation in Different Retailers in 2021')
ax.set_ylabel('Price (USD)')
ax.set_xticklabels(["Retailer A", "Retailer B", "Retailer C", "Retailer D", "Retailer E"], rotation=90, wrap=True)

ax.grid(axis='y')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/3_202312270030.png')

plt.clf()