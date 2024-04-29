
import matplotlib.pyplot as plt
import numpy as np

housing_type = ["Apartment", "Townhouse", "House", "Villa", "Mansion"]
min_price = [200, 300, 400, 500, 800]
Q1_price = [500, 600, 700, 800, 1200]
median_price = [650, 800, 900, 1000, 1500]
Q3_price = [800, 1000, 1100, 1200, 1800]
max_price = [1000, 1300, 1500, 1700, 2500]
outlier_price = [[], [2500], [200, 1700], [2000], [3000, 4000]]

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)
ax.set_title('Price Distribution of Different Housing Types in Australia (2020)')
ax.boxplot(
    np.array([min_price, Q1_price, median_price, Q3_price, max_price]), 
    labels=housing_type, 
    showmeans=True, 
    flierprops=dict(marker='o', markerfacecolor='red', markersize=12, linestyle='none')
)
for i, outlier in enumerate(outlier_price):
    if len(outlier) > 0:
        ax.plot([i+1] * len(outlier), outlier, 'ro', alpha=0.6)
ax.set_xticklabels(housing_type, rotation=45, ha='right', wrap=True)
ax.grid()
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/13.png")
plt.clf()