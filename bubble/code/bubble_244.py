import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

data_str = "Product,Production Volume (Million Units),Factory Footprint (Million Square Feet),Profit Margin (%),Environmental Impact (Score)\n Cars,70,200,15,7\n Smartphones,500,100,30,5\n Laptops,200,80,20,6\n Appliances,100,60,25,8\n Furniture,150,40,22,9\n Toys,600,30,18,4"
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [l.split(',')[0] for l in data_lines[1:]]
data_lines = [line.split(',')[1:] for line in data_lines[1:]]

data = np.array([[float(val) for val in line] for line in data_lines])

norm = mpl.colors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = plt.cm.viridis
figure = plt.figure(figsize=(10, 10))
ax = figure.add_subplot(111)

for i, line_label in enumerate(line_labels):
    color = cmap(norm(data[i, 3]))
    size = 600 + 4400 * ((data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()))
    ax.scatter(data[i, 0], data[i, 1], color=color, s=size, label=None)
    ax.scatter([], [], color=color, s=20, label=line_label + f' {data[i, 2]}')

ax.legend(title=data_labels[2])
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
figure.colorbar(sm, label=data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Impact of Different Product Manufacture on Profit and Environment')
ax.grid(True)

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/63_202312301731.png')

plt.clf()
