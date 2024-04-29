
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

labels = ['Home Network', 'Mobile Network', 'Office Network', 'School Network', 'Hotspot Network']
data = [[6.5, 10.4, 15.2, 20.1, 25.0],
        [7.2, 11.7, 17.2, 22.7, 28.0],
        [7.8, 12.3, 18.1, 23.6, 29.2],
        [6.1, 9.7, 14.4, 19.1, 23.8],
        [6.9, 10.6, 15.8, 20.9, 25.6]]
outliers = [[], [36.9], [2.3, 35.6, 40.1], [31.0, 38.6], [34.4]]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Network Speed Distribution in Different Locations (2021)')
ax.set_ylabel('Speed (KB/s)')
ax.set_xticklabels(labels, rotation=45, ha='right', wrap=True)
ax.boxplot(data, whis=1.5)
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.grid(which='major', axis='y', color='0.75', linestyle='--')
for i, outlier in enumerate(outliers):
        if len(outlier) > 0:
                ax.plot(np.repeat(i+1, len(outlier)), outlier, 'ro')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/2_202312251608.png')
plt.clf()