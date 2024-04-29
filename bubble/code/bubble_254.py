import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data_raw = 'Engineering Field,Grants Received (Million $),Number of Research (Units),Number of Patents Registered,Gender Diversity (Female Percentage)\n Civil Engineering,200,150,60,30\n Computer Engineering,400,200,110,15\n Mechanical Engineering,300,180,90,20\n Electrical Engineering,350,170,100,17\n Chemical Engineering,250,160,80,33\n Aerospace Engineering,300,140,70,10\n Environmental Engineering,180,130,50,40'
lines = data_raw.split("\n")

data_labels = lines[0].split(',')[1:]
data = np.array([line.split(',')[1:] for line in lines[1:]], dtype=float)
line_labels = [f"{line.split(',')[0]} ({int(data[i, 2])})" for i, line in enumerate(lines[1:])]

fig, ax = plt.subplots(figsize=(10, 6))

colors = cm.viridis(Normalize()(data[:, 3]))
bubble_sizes = Normalize()(data[:, 2]) * (5000 - 600) + 600

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], c=[colors[i]], s=bubble_sizes[i], label=None, alpha=0.6)
    ax.scatter([], [], c='k', alpha=0.6, s=20, label=line_labels[i])

ax.legend(title=data_labels[2], loc='upper left')

sm = cm.ScalarMappable(cmap=cm.viridis, norm=plt.Normalize(vmin=0, vmax=max(data[:, 3])))
sm.set_array([])
fig.colorbar(sm, label=data_labels[3], pad=0.01)

ax.grid(True)

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

plt.title('Overview of Funding, Research, Patent and Gender Diversity in Various Engineering Fields', wrap=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/186_202312310045.png')
plt.clf()
