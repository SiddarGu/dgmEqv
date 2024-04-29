import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

# text data
txt = 'Organization,Donations (Million $),Volunteers (Thousand),Programs Offered,Impact Score\n' \
      'Red Cross,1500,200,50,85\n' 'United Way,1000,150,60,75\n' \
      'Save the Children,800,100,40,80\n' 'Feeding America,1200,180,70,90\n' \
      'World Wildlife Fund,900,120,30,95\n' 'Habitat for Humanity,700,80,25,70'

# parse the text data
lines = txt.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels, data = [], []
for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0] + ' ' + parts[2])
    data.append(list(map(int, parts[1:])))
data = np.array(data)

# scatter plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111)
cmap = plt.get_cmap('viridis')
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(mappable=sm, ax=ax, label=data_labels[3])

for i, line_label in enumerate(line_labels):
    size = (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min())
    ax.scatter(data[i, 0], data[i, 1], label=None, c=cmap(norm(data[i, 3])), s=600 + size * 4400)
    ax.scatter([], [], color=cmap(norm(data[i, 3])), label=line_label, s=20)

ax.legend(title=data_labels[2], loc='upper left')

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Impact of Nonprofit Organizations in Charity Work')
plt.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/Full/bubble/png_train/bubble_294.png')
plt.clf()
