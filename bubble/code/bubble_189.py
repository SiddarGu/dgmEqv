import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors

data_input = '''Platform,Active Users (Millions), Average Time Spent (Hours/Week), Revenue (Billion $), Average Ad Revenue Per User ($)
Facebook,2745,6.35,70.7,25.2
YouTube,2000,8.5,15.1,7.55
WhatsApp,2000,4.4,5,2.5
Instagram,1300,5.3,20,15.4
Twitter,330,1.3,3.46,10.5
LinkedIn,310,1,2.27,7.32
Snapchat,498,3.5,1.7,3.41'''

lines = data_input.split('\n')
data_labels = lines[0].split(',')[1:]
data = np.array([line.split(',')[1:] for line in lines[1:]], dtype=float)
line_labels = [line.split(',')[0] for line in lines[1:]]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()

cmap = plt.get_cmap('viridis')
c_norm = colors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
scalar_map = plt.cm.ScalarMappable(norm=c_norm, cmap=cmap)

for i, line_label in enumerate(line_labels):
    line_label += ' ' + str(data[i, 2])
    ax.scatter(data[i, 0], data[i, 1], s=600 + 4400 * (data[i, 2]-data[:, 2].min())/(data[:, 2].max()-data[:, 2].min()),
               c=scalar_map.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], c=scalar_map.to_rgba(data[i, 3]), label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
plt.colorbar(scalar_map, label=data_labels[3])

plt.grid(True, which='both')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Popularity and Profitability of Different Social Media Platforms')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/122_202312301731.png')
plt.clf()
