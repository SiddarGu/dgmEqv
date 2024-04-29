import matplotlib.pyplot as plt
import numpy as np

data = [["Air Transport", 1, 5, 8, 12, 20, []],
        ["Land Transport", 2, 6, 9, 13, 22, [1,30]],
        ["Sea Transport", 3, 7, 10, 15, 25, [1,35]],
        ["Rail Transport", 1.5, 5.5, 9.5, 13.5, 22.5, [0.5,27]],
        ["Pipeline Transport", 1.2, 5.2, 8.2, 12.2, 19.2, []]]

categories = [item[0] for item in data]
values = [item[1:6] for item in data]
outliers = [item[6] for item in data]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.boxplot(values, notch=True, widths=0.4, vert=False, whis=1.5, 
           patch_artist=True, boxprops=dict(facecolor="C0"))

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

ax.set_yticklabels(categories)
ax.set_xlabel('Time (Hours)')
ax.set_title('Transport Duration Distribution in Different Transport Types (2020)')
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/95_202312270030.png', format='png')
plt.close(fig)
