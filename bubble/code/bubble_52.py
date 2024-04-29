import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import FuncFormatter
import matplotlib.cm as cm

data = "Product,Annual Sales (Billion $),Market Share (%),Customer Satisfaction (Score),Healthiness (Score)/n Cola,300,30,70,30/n Coffee,200,20,80,70/n Beer,150,15,75,40/n Dairy,100,10,90,80/n Meat,50,5,65,60/n Canned Food,20,2,50,50/n Organic Food,180,18,95,100"
rows = data.split("/n")
data = [row.split(",") for row in rows]
data_labels = data.pop(0)[1:]
line_labels = [row[0] for row in data]

data = np.array([[float(val) for val in row[1:]] for row in data])

cmap = plt.get_cmap("RdYlGn")
norm = colors.Normalize(vmin=np.min(data[:,3]), vmax=np.max(data[:,3]))

fig, ax = plt.subplots(figsize=(8, 8))

for i, line_label in enumerate(line_labels):
    size = (data[i, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2])) * (5000 - 600) + 600
    scatter = ax.scatter(data[i, 0], data[i, 1], c=[data[i, 3]], cmap=cmap, norm=norm, s=size, label=None)
    ax.scatter([], [], c='k', alpha=0.5, s=20, label=line_label + f' {data[i, 2]}')

ax.legend(title=data_labels[2])
plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), label=data_labels[3])

ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Analysis of Product Performance in the Food and Beverage Industry 2023')

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/137_202312301731.png")
plt.cla()
plt.clf()
plt.close()
