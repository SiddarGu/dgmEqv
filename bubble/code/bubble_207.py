import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib import pyplot
from numpy import array
import re
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data_str = "Legal Area,Cases Handled (Thousands),Success Rate (%),Public Satisfaction (%),Impact (Score)/n Criminal Law,1500,85,80,90/n Civil Law,2200,80,75,85/n Corporate Law,1800,90,88,92/n Intellectual Property Law,1600,92,85,87/n Environmental Law,1400,75,70,80/n Constitutional Law,1300,88,76,86/n Labor Law,1100,82,77,83"
data_rows = re.split(r'/n', data_str)
data_labels = data_rows[0].split(',')[1:]
line_labels = [r.split(',')[0] + ' ' + r.split(',')[2] for r in data_rows[1:]]
data = np.array([list(map(int, r.split(',')[1:])) for r in data_rows[1:]])

fig, ax = plt.subplots(figsize=(10, 10))

norm = Normalize(vmin=data[:, 3].min() - 10, vmax=data[:, 3].max())
cmap = get_cmap("Greens")
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])
    
ax.legend(title=data_labels[2], loc='upper left')
sm = ScalarMappable(norm=norm, cmap='Greens')
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])
ax.grid(True)
plt.title("Statistic Data of Different Legal Areas in 2023", fontsize=14, pad=20)
plt.xlabel(data_labels[0], fontsize=12)
plt.ylabel(data_labels[1], fontsize=12)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/226_202312310045.png")
plt.cla()
plt.clf()
