import matplotlib.pyplot as plt
import numpy as np

# data transformation
data_str = 'Category,Jan,Feb,Mar,Apr,May,Jun/n Online Sales,85,80,86,90,95,100/n In-Store Sales,70,72,73,75,78,82/n Customer Returns,30,28,26,24,23,20/n New Customers,50,55,60,65,70,75/n Website Traffic,90,85,80,78,78,80/n Inventory Turnover,70,76,82,88,90,95'
data_lst = [i.split(",") for i in data_str.split("/n")]
data_labels = data_lst[0][1:]
data = [list(map(int, row[1:])) for row in data_lst[1:]]
line_labels = [row[0] for row in data_lst[1:]]

# plotting
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, max(max(row) for row in data))

for i, d in enumerate(data):
    cdata = d + [d[0]]
    ax.plot(angles, cdata, label=line_labels[i])
    ax.fill(angles, np.full_like(angles, (i+1)*max(max(row) for row in data)/len(data)), color='gray', alpha=0.1)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=120)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
ax.set_title("Retail and E-commerce Performance - First Half of the Year")
plt.tight_layout()

# saving
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/146_2023122292141.png")

# clearing
plt.clf()
