
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12,8))

data = [[2,4,6,8,10],
        [3,5,7,9,12,14],
        [1,3,5,7,9,11,13],
        [4,7,10,13,16,18],
        [2,5,7,9,12,14,17]]
outliers = [data[i][5:] if len(data[i]) > 5 else [] for i in range(len(data))]
labels = ["Painting","Music","Sculpture","Dance","Theater"]

plt.boxplot(np.array([data[i][:5] for i in range(5)]).T,labels=labels,showmeans=True,meanline=True,showfliers=False)
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        plt.plot([i+1] * len(outlier), outlier, 'go', alpha=0.3, markersize=8)
plt.title("Performance Duration Distribution in Arts and Culture (2020)")
plt.xticks(rotation=45, ha='right', wrap=True)
plt.ylabel('Duration (Hours)')
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/box/png_val/box_26.png")
plt.clf()