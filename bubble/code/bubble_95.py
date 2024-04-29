import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

data_labels = ['Annual Revenue (Million $)', 'Number of Beneficiaries (Thousands)', 
               'Operational Costs (Percentage of Revenue)', 'Donor Satisfaction (Score out of 10)']
data = np.array([
    [3000, 50, 25, 9],
    [2000, 40, 20, 8],
    [2500, 60, 30, 9],
    [1500, 70, 15, 10],
    [1000, 30, 20, 7],
    [800, 20, 10, 10],
    [500, 15, 30, 8]
])
line_labels = ['Red Cross', 'Salvation Army', 'UNICEF', 'World Food Programme', 
               'World Vision', 'Doctors Without Borders', 'Oxfam']

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)

cmap = plt.get_cmap("viridis")
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
for i in range(data.shape[0]):
    line_label = line_labels[i] + " " + str(data[i, 2])
    ax.scatter(data[i, 0], data[i, 1], cmap=cmap, s=(600 + (data[i, 2] / data[:, 2].max()) * 4400), c=data[i, 3], norm=norm, label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(linestyle='--', alpha=0.6)

normalizer = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
scalarmappaple = ScalarMappable(norm=normalizer, cmap=cmap)
plt.colorbar(scalarmappaple, ax=ax, label=data_labels[3])

plt.title('Operational Efficiency and Impact of Major Charities and Nonprofit Organizations 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/152_202312310045.png')
plt.clf()
