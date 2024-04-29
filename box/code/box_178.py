
import matplotlib.pyplot as plt
import numpy as np

data = [[50,200,400,800,1200], [100,300,500,1000,1500], [20,50,100,150,300], [25,60,120,180,250], [10,30,80,120,200]]
outliers = [[], [3000], [400], [500,750], [400,800]]
line_labels = ['Painting', 'Sculpture', 'Pottery', 'Drawing', 'Mixed Media']
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)
ax.set_title('Value Distribution of Artworks in the Market (2020)')
ax.set_xticklabels(line_labels)
ax.set_ylabel('Price (USD)')

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'o', color='red')

ax.grid(True, ls='--', lw=.5)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/37_202312270030.png')
plt.clf()