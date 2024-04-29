
import matplotlib.pyplot as plt
import numpy as np

data = [[100,200,400,600,800],
        [500,750,1000,1250,1500,1700],
        [1000,2000,3000,4000,5000,20,45],
        [2500,3500,4500,5500,6500,7000,8000],
        [50,100,150,200,250,320]]
outliers = [data[i][5:] if len(data[i]) > 5 else [] for i in range(len(data))]
plt.figure(figsize=(16,8))
ax = plt.subplot()
ax.boxplot(np.array([data[i][:5] for i in range(5)]).T, labels=['Twitter', 'Instagram', 'YouTube', 'Facebook', 'LinkedIn'],
            showfliers=False,
            patch_artist=True)
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i+1] * len(outlier), outlier, 'go', alpha=0.3, markersize=8)
ax.set_title('User Count Distribution for Social Media Platforms in 2021')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/17_202312251044.png')
plt.clf()