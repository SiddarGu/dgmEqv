
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data_labels = ["User Engagement (Score)", "Ad Revenue (Million $)", "Content Quality (Score)", "User Growth (Million)"]
data = np.array([[90,30,8,2.3], [85,35,7,1.8], [80,25,9,1.2], [75,20,7,1.1], [70,15,10,0.7]])
line_labels = ["YouTube", "Facebook", "Instagram", "Twitter", "TikTok"]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

norm = Normalize(vmin=min(data[:,3]), vmax=max(data[:,3]))
cmap = get_cmap("jet")

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=600 + 5000*(data[i, 2]-min(data[:,2]))/(max(data[:,2])-min(data[:,2])), c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), label=line_labels[i] + f' {data[i, 2]}')

ax.legend(title=data_labels[2])
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label(data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(linestyle="--")
ax.set_title("Social Media Performance in 2021 - User Engagement and Ad Revenue")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/10_2023122261440.png")
plt.clf()