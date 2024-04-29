
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
data = {
    'Department Store': [20, 50, 80, 110, 150],
    'Shopping Mall': [15, 40, 65, 90, 120],
    'Grocery Store': [10, 30, 50, 70, 100],
    'Online Store': [5, 25, 45, 65, 85],
    'Discount Store': [25, 60, 75, 90, 105]
}

# Plot the data
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(111)
ax.set_title('Product Price Distribution in Various Retail Stores (2021)')
ax.grid()

bp = ax.boxplot(data.values())
labels = data.keys()
ax.set_ylabel('Price (USD)')
ax.set_xticklabels(labels, rotation=45, ha='right', wrap=True)

# Plot the outliers
outliers_dict = {
    'Department Store': [],
    'Shopping Mall': [200],
    'Grocery Store': [150, 300],
    'Online Store': [95, 110],
    'Discount Store': [120, 150]
}
x = 0
for label in labels:
    outliers = outliers_dict[label]
    if len(outliers) > 0:
        for outlier in outliers:
            ax.plot(x + 1, outlier, marker='o', color='red', ms=4.5)
    x += 1

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/box/png_val/box_7.png')
plt.clf()