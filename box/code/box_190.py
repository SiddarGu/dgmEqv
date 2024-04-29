
import matplotlib.pyplot as plt
import numpy as np

data = [[100, 300, 500, 700, 1000], [150, 400, 600, 800, 1200, 1400], [200, 450, 650, 850, 1100, 250, 1300], [50, 200, 400, 600, 800, 700, 900], [75, 250, 400, 550, 700, 900]]
outliers = [data[i][5:] if len(data[i]) > 5 else [] for i in range(len(data))]
#create figure
fig = plt.figure(figsize = (15, 8))

#box plot
ax1 = fig.add_subplot(111)
ax1.set_title('Pollution Quantity Distribution in Environment and Sustainability (2021)')
ax1.boxplot(np.array([data[i][:5] for i in range(5)]).T, labels=['Air Pollution', 'Water Pollution', 'Soil Pollution', 'Noise Pollution', 'Light Pollution'], showmeans=True, meanline=True, patch_artist=True)
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax1.plot([i+1] * len(outlier), outlier, 'ro', alpha=0.6)
#set labels
ax1.set_xlabel('Pollution Type', fontsize=15)
ax1.set_ylabel('Quantity (KG)', fontsize=15)

#adjust layout
plt.tight_layout()

#save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/10.png')

#clear figure
plt.clf()