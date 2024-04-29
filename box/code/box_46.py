

import matplotlib.pyplot as plt
import numpy as np

data_list = [[100, 250, 400, 550, 700],
             [150, 250, 400, 550, 650],
             [50, 200, 350, 500, 600],
             [75, 200, 350, 475, 600],
             [25, 100, 225, 350, 400]]
outlier_list = [[], [800], [10, 30], [700], [500]]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

ax.boxplot(data_list, whis=1.5)

ax.set_title('Compressive Strength Distribution of Materials in Engineering (2021)')
ax.set_xlabel('Material')
ax.set_ylabel('Strength (KPa)')
ax.set_xticklabels(['Steel', 'Concrete', 'Aluminum', 'Copper', 'Plastic'])

for i, outlier in enumerate(outlier_list):
    if outlier:
        ax.plot(np.full(len(outlier), i+1), outlier, 'ro', alpha=0.5)

ax.grid()

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/35_202312270030.png')
plt.clf()