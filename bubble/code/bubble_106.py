import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

text = """Platform,Daily Active Users (Million),Revenue (Billion USD),Time Spent Daily (Minutes),Privacy Rating (Score)
Facebook,1790,85.2,38,7
Instagram,500,20.1,28,8
Twitter,330,3.7,31,8
Snapchat,229,2.5,26,9
YouTube,2000,15.1,40,8
WhatsApp,1750,5.0,35,8
LinkedIn,310,3.8,10,9"""

lines = text.split('\n')
data_labels = lines[0].split(',')[1:]
data = np.array([line.split(',')[1:] for line in lines[1:]], dtype=float)
line_labels = [line.split(',')[0] + ' ' + str(d[2]) for line, d in zip(lines[1:], data)]


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
figure, ax = plt.subplots()
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

# Plotting each data point with consistent color
for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], alpha=0.6, edgecolors="w", linewidth=1, label=None)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])


cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3])
ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('User Activity and Business Performance on Social Media Platforms 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/236_202312310045.png')
plt.close(fig)
