import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase

data_str = 'Company,Revenue (Billion $),Operating Margin (%),Market Capitalization (Billion $),Dividend Yield (%)\n Apple,274.5,24.5,2234.7,0.6\n Amazon,386.1,5.5,1720.4,0\n Google,182.5,21,1545.9,0\n Microsoft,143.0,37.4,2123.8,0.9\n Facebook,85.9,37.9,942.1,0\n Tesla,31.5,2.3,834.2,0\n Alibaba,72.5,12.1,654.9,0\n Johnson & Johnson,82.6,21.1,442.5,2.6\n Walmart,559.2,3.3,408.0,1.6\n Procter & Gamble,71.3,20.4,349.2,2.3'
data_lines = data_str.split('\n')

# extract labels
data_labels = data_lines[0].split(',')

# extract data
data = []
line_labels = []
for line in data_lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0] + parts[2])
    data.append([float(p) for p in parts[1:]])
data = np.array(data)

normalized_data = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
normalized_color = Normalize()(data[:, 3])
normalized_size = Normalize()(data[:, 2]) * (5000 - 600) + 600

cmap = cm.get_cmap('viridis')

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=normalized_size[i], c=cmap(normalized_color[i]), label=None)
    ax.scatter([], [], s=20, c=cmap(normalized_color[i]), label=line_labels[i])

ax.legend(title=data_labels[2], loc='upper right')
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
cbar.set_label(data_labels[3])

ax.grid(True)
plt.title('Key Financial Metrics of Major Global Companies in 2023', fontsize=14)
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/182_202312310045.png')
plt.close(fig)
