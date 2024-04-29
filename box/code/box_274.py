

import matplotlib.pyplot as plt
import numpy as np

#restructure data into two 2D lists
data_list = [[10,50,100,150,200],[15,75,125,175,250],[20,60,110,160,210],[25,55,105,155,205],[30,45,95,145,195]]
outlier_list = [[],[300],[20,400],[10,15],[320]]

#plot data with boxplot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.boxplot(data_list, whis=1.5, showmeans=True, meanline=True, showfliers=False)

#plot outliers manually
for i, outlier in enumerate(outlier_list):
    if len(outlier) > 0:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, 'o', color='red')

#draw background grid and set labels
ax.set_title('Charitable Donation Distribution of Nonprofits in 2021')
ax.set_ylabel('Donations (USD)')
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xticklabels(['Organization A', 'Organization B', 'Organization C', 'Organization D', 'Organization E'], rotation=45, wrap=True)

#resize image before saving
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/14_202312251608.png')

#clear the current image state
plt.clf()