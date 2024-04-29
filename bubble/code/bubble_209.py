

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import matplotlib.cm as cm

data_labels = ['Donations (Million $)', 'Volunteer Hours (Millions)',
               'Impact (Score)', 'Regional Reach (Score)']
data = np.array([[200, 10, 8, 10], [170, 8, 9, 7], [180, 12, 7, 6],
                 [150, 7, 9, 8], [100, 4, 8, 8], [80, 2, 10, 5]])
line_labels = ['Red Cross', 'UNICEF', 'World Vision', 'Save the Children',
               'Greenpeace', 'Doctors Without Borders']

colors = data[:, 3]
sizes = data[:, 2]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

cmap = cm.get_cmap('RdYlGn')
norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
for i in range(len(data)):
    colors = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i] * 1000,
               color=colors, label=None)
    ax.scatter([], [], s=20, color=colors, label=line_labels[i]+ ' ' + str(data[i, 2]))

ax.legend(title=data_labels[2])

# cmap
cmap = ScalarMappable(norm=Normalize(vmin=np.min(colors), vmax=np.max(colors)),
                      cmap='RdYlGn')
cmap.set_array([])
plt.colorbar(cmap, ax=ax, label=data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Measuring the Impact of Nonprofit Organizations on Society')

# grid
ax.grid()

# adjust image
plt.tight_layout()

# save
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/45_2023122270050.png')

# clear
plt.clf()