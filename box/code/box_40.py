
import matplotlib.pyplot as plt
import numpy as np

data = [[100, 300, 500, 700, 900], 
        [200, 400, 600, 800, 1000], 
        [150, 350, 550, 750, 950], 
        [250, 450, 650, 850, 1050], 
        [110, 310, 510, 710, 910]]

outliers = [[], [1500], [100, 1700], [1350, 1800], [1600]]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()
ax.boxplot(data, whis=1.5, showmeans=True, labels=['Wheat', 'Corn', 'Rice', 'Soybeans', 'Barley'])
plt.title('Crop Yield Distribution in Agriculture and Food Production (2021)', fontsize=14)
plt.ylabel('Yield (Kg/Ha)', fontsize=12)

for i, outlier in enumerate(outliers):
    if outlier:
        x_coord = [i + 1] * len(outlier)
        ax.plot(x_coord, outlier, "ro")

ax.grid(axis='y', alpha=0.5)

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/39_202312251608.png')

plt.clf()