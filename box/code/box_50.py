
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6))
ax = plt.subplot()
data = [[10,50,100,200,300], [20,75,125,250,400,1000], [30,90,140,250,450,20,500], [25,80,120,200,350], [15,60,110,180,300,1000]]
outliers = [data[i][5:] if len(data[i]) > 5 else [] for i in range(len(data))]
labels = ['Organization A','Organization B','Organization C','Organization D','Organization E']
ax.boxplot(np.array([data[i][:5] for i in range(5)]).T, labels=labels)
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i+1] * len(outlier), outlier, 'ro', alpha=0.6)
ax.set_title('Donations Distribution in Nonprofit Organizations in 2020')
ax.set_xlabel('Nonprofit Organization')
ax.set_ylabel('Donations (Dollars)')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/14.png')
plt.clf()