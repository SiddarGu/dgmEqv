from textwrap import wrap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib import colors

data_str = 'Apple,2300,260,55,100 Microsoft,1700,165,40,70 Amazon,1500,350,20,110 Alphabet,1450,180,30,60 Facebook,900,80,25,40 Tesla,800,40,5,25'
data_str = data_str.split()
data_str = [i.split(',') for i in data_str]
data_labels = ['Market Cap (Billion $)', 'Revenue (Billion $)', 'Profit (Billion $)', 'Debt (Billion $)']
line_labels = [i[0]+data_str[0][2] for i in data_str]
data = np.array([i[1:] for i in data_str], dtype=float)

fig, ax = plt.subplots(figsize=(12,6))

colors = Normalize(data[:,3].min(), data[:,3].max())
colormap = get_cmap('viridis')
size_scale = Normalize(data[:,2].min(), data[:,2].max())

for i in range(0, len(data)):
    ax.scatter(data[i, 0], data[i, 1], c=[colormap(colors(data[i,3]))], s=600+(size_scale(data[i,2])*5000), label=None)
    ax.scatter([], [], c=[colormap(colors(data[i,3]))], s=20, label=list(map('\n'.join, map(lambda line: wrap(line, 30), line_labels)))[i])

ax.legend(title=data_labels[2], loc='upper left')

mappable = plt.cm.ScalarMappable(norm=colors, cmap=colormap)
cbar = plt.colorbar(mappable, ax=ax)
cbar.ax.set_title(data_labels[3])

ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: '${:,.0f}B'.format(x)))
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '${:,.0f}B'.format(x)))

plt.title("Financial Performance of Tech Giants")
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.tight_layout()
plt.grid(visible=True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/339_202312311429.png')
plt.clf()
