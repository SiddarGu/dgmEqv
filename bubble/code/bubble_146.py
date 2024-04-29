import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Provided Data
data_str = "Company,Market Cap (Billion $),Active Users (Millions),Revenue (Billion $),Innovation (Score)/n Google,1600,1500,161,85/n Amazon,1700,300,386,80/n Facebook,800,2700,85,75/n Microsoft,1800,260,143,90/n Apple,2200,1000,274,95/n Tencent,600,650,70,65/n Alibaba,570,780,72,75"
data_str = data_str.replace('/n ', '/n').split('/n')

data_labels = data_str[0].split(',')[1:]
data = np.array([sub.split(",")[1:] for sub in data_str[1:]], dtype=float)
line_labels = [sub.split(",")[0] + ': ' + str(int(sub.split(",")[2])) for sub in data_str[1:]]

norm = plt.Normalize(data[:, 3].min(), data[:, 3].max())
cmap = get_cmap('viridis')

fig, ax = plt.subplots(figsize=(15, 8))
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], label=None, color=cmap(norm(data[i, 3])), s=600 + 44000 * (data[i, 2] / data.max()), alpha=0.7)
    ax.scatter([], [], color=cmap(norm(data[i, 3])), label=line_label, s=20)

ax.legend(title=data_labels[2])
ax.grid(True)

label = ax.set_title('Market Performance and Innovation of Major Tech Companies')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3])))
sm.set_array([])
fig.colorbar(sm, ax=ax, aspect=50, label=data_labels[3])

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/81_202312301731.png')
plt.clf()
