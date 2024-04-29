
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = ["Manufacturing Cost (Million $)", "Unit Price (Dollars)", "Sales Volume (Units)", "Quality (Score)"]
data = np.array([[2000, 35000, 20000, 9], 
                 [1000, 200, 50000, 7],
                 [3000, 1000, 10000, 8],
                 [1500, 50, 100000, 10],
                 [800, 100, 40000, 8]])
line_labels = ["Automobiles", "Electronics", "Furniture", "Textiles", "Shoes"]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

norm_size = (data[:,2] - np.min(data[:,2])) / (np.max(data[:,2]) - np.min(data[:,2])) * (5000 - 600) + 600
norm_color = (data[:,3] - np.min(data[:,3])) / (np.max(data[:,3]) - np.min(data[:,3]))

for i in range(len(line_labels)):
    ax.scatter(data[i, 0], data[i, 1], s=norm_size[i], c=cm.jet(norm_color[i]), label=None)
    ax.scatter([], [], s=20, c=cm.jet(norm_color[i]), label=line_labels[i]+" "+str(data[i,2]))

ax.legend(title=data_labels[2], bbox_to_anchor=(1, 1))
sm = cm.ScalarMappable(cmap=cm.jet, norm=plt.Normalize(np.min(data[:,3]), np.max(data[:,3])))
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label(data_labels[3], rotation=90)

ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title("Cost-Benefit Analysis of Manufacturing and Productio")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/36_2023122270050.png")
plt.clf()