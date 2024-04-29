import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

data_raw = """Google,31,5000,181,9
Facebook,25,3766,86,7
Apple,21,1436,275,10
Amazon,16,3100,386,8
Microsoft,12,1500,143,8
Twitter,8,330,15,6
Alibaba,7,874,72,8
"""
data_lines = data_raw.strip().split("\n")
data_labels = ["Company", "Market Share (%)", "Active Users (Millions)", "Revenue (Billion $)", "Innovation (Score)"]
line_labels = [line.split(",")[0]+" "+str(line.split(",")[2]) for line in data_lines]

data = np.array([list(map(float, line.split(",")[1:])) for line in data_lines])

fig, ax = plt.subplots(figsize=(14,8))
color_map = plt.get_cmap('viridis')
c_norm = mcolors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
scalar_map = cm.ScalarMappable(norm=c_norm, cmap=color_map)
fig.colorbar(scalar_map, label=data_labels[3])

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], label=None, c=scalar_map.to_rgba(data[i, 3]), alpha=0.7,
              s=600 + 4400 * (data[i, 2] - data[:, 2].min()) / np.ptp(data[:, 2]))
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
plt.grid(True)
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
plt.title("Analysis of Major Internet Technology Companies' Market Impact", fontsize=16)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/128_202312301731.png")
plt.clf()
