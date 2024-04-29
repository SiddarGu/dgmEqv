import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

data_str = "Platform,Monthly Active Users (Millions),Average Time Spent per Day (Minutes),Revenue (Billion $),Security Score (Out of 10)\n Facebook,2700,58,70,8\n YouTube,2000,40,15,7\n Instagram,1000,28,10,9\n Twitter,330,31,3,8\n LinkedIn,310,17,2,10\n Snapchat,255,26,1,7"
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = []
data = []

for line in data_lines[1:]:
    line_parts = line.split(',')
    line_labels.append(line_parts[0] + line_parts[2])
    data.append(line_parts[1:])

data = np.array(data, dtype=float)

fig, ax = plt.subplots(figsize=(16, 8))

size = (data[:,2]/data[:,2].max()) * 5000 + 600
colors = mcolors.Normalize()(data[:,3])

scatter = ax.scatter(data[:, 0], data[:, 1], c=colors, cmap='viridis', sizes=size, alpha=0.6, label=None)

for i in range(len(data)):
    ax.scatter([], [], label=line_labels[i], c='k')

ax.legend(title=data_labels[2])

cbar = fig.colorbar(mappable=plt.cm.ScalarMappable(norm=mcolors.Normalize(), cmap='viridis'), ax=ax)
cbar.set_label(data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

fig.tight_layout()
plt.title('User Activity and Revenue in Social Media Platforms 2023')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/306_202312310045.png')
plt.clf()
