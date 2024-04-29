
import matplotlib.pyplot as plt
import numpy as np

data = [[0.5, 2.2, 3.8, 5.3, 7.5],
        [1.0, 2.5, 4.2, 5.8, 7.2],
        [1.2, 3.2, 4.7, 6.2, 8.0],
        [0.4, 2.0, 3.4, 4.9, 6.6],
        [0.6, 2.4, 3.9, 5.5, 7.1]]
outlier = [[],
                [9.1],
                [0.3, 9.1, 9.6],
                [8.1, 9.1],
                [8.6]]
categories = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Coal']

fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(6)

for i, (category, box_data) in enumerate(zip(categories, data)):
        ax.boxplot(box_data, whis=1.5, labels=[category], positions=[i + 1])
        if outlier[i]:
                ax.plot(np.repeat(i + 1, len(outlier[i])), outlier[i], 'ro')

ax.set_title('Energy Output Distribution in Different Energy Sources (2020)')
ax.set_ylabel('Energy Output (kWh)')
ax.set_xticklabels(categories)
ax.grid(axis='y')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/5_202312251520.png')
plt.clf()