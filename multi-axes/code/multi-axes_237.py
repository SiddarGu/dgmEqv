import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# data
data_str = "Category,Production Capacity (Units),Sales (Units),Revenue (Millions of Dollars),Average Selling Price (Dollars)\nCars,10000,8000,400,5000\nElectronics,5000,4500,400,8000\nAppliances,8000,6000,300,5000\nFurniture,7000,5500,350,6000\nMachinery,9000,7000,450,6500\nChemicals,6000,5000,350,7000\nTextiles,4000,3500,200,5000\nFood and Beverages,12000,10000,450,4500\nPharmaceuticals,3000,2500,200,8000\nPlastics,7000,6500,300,5000"

# transform the data and split it into three variables
data_str = data_str.splitlines()
data_labels = data_str[0].split(",")[1:]
line_labels = [item.split(",")[0] for item in data_str[1:]]
data = np.array([list(map(int, item.split(",")[1:])) for item in data_str[1:]])

# plot types
plot_types = ["bar", "line", "line", "fill"]

# figure
fig = plt.figure(figsize=(15, 10))

# plot
ax = [fig.add_subplot(111)]
ax[0].bar(line_labels, data[:, 0], color='b', alpha=0.75, width=0.4)
ax[0].set_ylabel(data_labels[0], color='b')

for i in range(1, len(data_labels)):
    ax.append(ax[0].twinx())
    ax[i].spines['right'].set_position(('outward', 60*(i-1)))
    plot_type = plot_types[i]
    if plot_type == "line":
        ax[i].plot(line_labels, data[:, i], color=f'C{i+1}')
        ax[i].set_ylabel(data_labels[i], color=f'C{i+1}')
    elif plot_type == 'bar':
        ax[i].bar(line_labels, data[:, i], color='g', alpha=0.75, width=0.4)
        ax[i].set_ylabel(data_labels[i], color='g')
    else:
        ax[i].fill_between(line_labels, data[:, i], color='y', alpha=0.5)
        ax[i].set_ylabel(data_labels[i], color='y')
    ax[i].yaxis.set_major_locator(AutoLocator())
    ax[i].legend([data_labels[i]], loc='upper right')

plt.title('Manufacturing and Production Analysis: Production, Sales, Revenue, and Pricing Comparison')
fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/284_202312311430.png")
plt.clf()
