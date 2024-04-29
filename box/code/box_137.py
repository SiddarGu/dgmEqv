
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Single Family Home' : [100000, 200000, 300000, 400000, 500000],
    'Condominium' : [150000, 250000, 350000, 450000, 550000, 700000],
    'Multi-Family Home' : [110000, 220000, 330000, 440000, 550000, 60000, 80000],
    'Townhouse' : [90000, 180000, 270000, 360000, 450000, 75000],
    'Vacant Lot' : [80000, 160000, 240000, 320000, 400000, 500000]
}

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)

labels = list(data.keys())

ax.boxplot([data[label][:5] for label in labels], labels=labels, showmeans=True, meanline=True, meanprops=dict(linestyle='--', linewidth=1.5))

for label in labels:
    outliers = [value if len(data[label]) > 5 else [] for value in data[label][5:]]
    if outliers:
        for outlier in outliers:
            ax.plot([labels.index(label)+1], [outlier], marker='o', color='#e7298a', markersize=5)

plt.title('Property Price Distribution in Real Estate and Housing Market in 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/7_202312251044.png')
plt.close()