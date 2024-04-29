import numpy as np
import matplotlib.pyplot as plt

data = [[6, 8, 12, 14, 18], [7, 10, 13, 16, 20, 25], [10, 12, 14, 16, 20, 18, 22], [5, 7, 9, 13, 18, 20, 25], [7, 10, 12, 15, 18, 19, 24]] 
labels = ['iPhone', 'Samsung', 'Huawei', 'Xiaomi', 'Oppo']

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.boxplot(np.array([data[i][:5] for i in range(5)]).T, labels=labels)

outliers_x = []
outliers_y = []

for i, l in enumerate(labels):
    d = data[i]
    outliers = d[5:] if len(d) > 5 else []
    for outlier in outliers:
        outliers_x.append(i + 1)
        outliers_y.append(outlier)

ax.plot(outliers_x, outliers_y, 'ro', markersize=7, label='Outlier')

ax.set_title('Battery Life Distribution of Tech Devices in 2021')
ax.set_ylabel('Battery Life (Hours)')
ax.set_xlabel('Tech Device')
ax.legend()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/8_202312251044.png')
plt.close()