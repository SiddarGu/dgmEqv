import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import numpy as np

data_str = 'Platform,Active Users (Billion),Average Time Spent (Hours),Ad Revenue (Billion $),Engagement Score (/100)/n Facebook,2.8,1.5,84,65/n Instagram,1.3,1,20,70/n Twitter,0.33,0.3,3.5,55/n LinkedIn,0.76,0.7,2.5,60/n YouTube,2,2.1,15.1,75/n Snapchat,0.49,1,1.8,64'
data_lines = data_str.split('/n ')
data_labels = data_lines[0].split(',')[1:]
data = np.array([line.split(',')[1:] for line in data_lines[1:]]).astype(float)
line_labels = [line.split(',')[0] + str(data[i, 2]) for i, line in enumerate(data_lines[1:])]

fig, ax = plt.subplots(figsize=(12,10))

colors = Normalize(min(data[:, 3]), max(data[:, 3]))
colormap = cm.get_cmap('viridis')
sizemap = Normalize(min(data[:, 2]), max(data[:, 2]))

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], label=None, c=colormap(colors(data[i, 3])), s=600 + 4400 * sizemap(data[i, 2]))
    ax.scatter([], [], label=line_label, c=colormap(colors(data[i, 3])), s=20)

plt.colorbar(ScalarMappable(norm=colors, cmap=colormap), ax=ax).set_label(data_labels[3])

ax.legend(title=data_labels[2], loc='upper left')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('User Engagement and Ad Revenue on Different Social Media Platforms')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/278_202312310045.png')
plt.clf()
