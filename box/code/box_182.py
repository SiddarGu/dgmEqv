

import matplotlib.pyplot as plt
import numpy as np

# restructure the data into two 2D lists
data = [[50,100,150,200,250],
        [75,125,175,225,275],
        [60,110,160,210,260],
        [40,90,140,190,240],
        [20,70,120,170,220]]
outliers = [[], [320], [0.1,400], [300], [320]]

# plot the data with the type of box plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5, patch_artist=True, labels=['Rice', 'Wheat', 'Maize', 'Soybean', 'Millet'])
ax.set_title('Crop Yield Distribution in Agriculture and Food Production (2021)')
ax.set_ylabel('Yield (Kg)')

# plot the outliers manually
for i, outlier in enumerate(outliers):
    if len(outlier):
        x = np.repeat(i + 1, len(outlier))
        ax.plot(x, outlier, marker='o', color='black', linestyle='')

# drawing techniques such as background grids
ax.grid(True, axis='y')

# automatically resize the image by tight_layout()
plt.tight_layout()

# savefig()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/12_202312270030.png')

# clear the current image state
plt.clf()