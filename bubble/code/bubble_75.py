import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.colorbar as mcb
import numpy as np

raw_data = "Company,Fleet Size, Total Deliveries (Millions),Operational Costs (Million $),Customer Satisfaction (%)/n DHL,34000,250,80,90/n FedEx,45000,300,105,92/n UPS,52000,350,120,89/n Amazon,40000,450,150,96/n Maersk,750,40,30,85/n DB Schenker,30000,200,65,88/n C.H. Robinson,24000,150,45,90".split("/n ")

data_labels = raw_data[0].split(',')[1:]
data = np.array([entry.split(',')[1:] for entry in raw_data[1:]], dtype=float)
line_labels = [entry.split(',')[0] + ' ' + str(entry.split(',')[2]) for entry in raw_data[1:]]

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot()
ax.grid(linewidth=0.3)

color_map = plt.get_cmap("viridis")
normalize_color = mcolors.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
converted_colors = normalize_color(data[:, 3])

for i in range(len(data)):
    scatter = ax.scatter(data[i, 0], data[i, 1], c=[color_map(converted_colors[i])], alpha=0.6,
               s=600 + 4400 * (data[i, 2] - np.min(data[:, 2])) / (np.max(data[:, 2]) - np.min(data[:, 2])), label=None)
    ax.scatter([], [], c=[color_map(converted_colors[i])], alpha=0.6, s=20, label=line_labels[i])

ax.set_xlabel(data_labels[0], fontsize=12, rotation=30)
ax.set_ylabel(data_labels[1], fontsize=12)

ax.legend(loc="upper right", title=data_labels[2])

cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3])

plt.title('Logistics Performance Analysis for Major Transportation Companies', fontsize=15)

fig.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/184_202312310045.png')

plt.close()
