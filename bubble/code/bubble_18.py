
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data_labels = ['Mortality Rate (Per Million)', 'Treatment Success Rate (%)', 'Recovery Rate (%)', 'Cost of Treatment (Thousand $)']
data = np.array([[600, 70, 40, 1000],
                 [400, 80, 50, 2000],
                 [300, 90, 60, 3000],
                 [200, 60, 30, 4000],
                 [100, 75, 20, 5000],
                 [50, 85, 25, 1000]])
line_labels = ['Cancer', 'Heart Disease', 'Diabetes', 'Liver Disease', 'Stroke', 'Flu']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

cmap = get_cmap('jet')
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2]) * 100, c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), label=line_labels[i] + f' {data[i, 2]}')

ax.legend(title=data_labels[3])

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3])
ax.set_title('Healthcare Outcomes and Costs for Common Diseases')

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/50_2023122270050.png')
plt.clf()