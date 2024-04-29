import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Data Preparation
data = '''Category,Number of Users (Millions),Internet Speed (Mbps),Number of Devices (Millions),Average Monthly Data Usage (GB),Revenue (Billions of Dollars)
Social Media,250,50,400,10,10
Streaming Services,150,100,300,30,20
E-commerce,200,40,250,20,15
Telecommunications,300,30,350,5,30
Online Gaming,100,10,200,50,5
Cloud Computing,50,200,150,100,25
Digital Advertising,350,20,500,15,40
Mobile Apps,400,60,600,25,50
Cybersecurity,50,100,100,5,20
Artificial Intelligence,50,150,100,10,15'''
lines = data.split("\n")
data_labels = lines[0].split(",")[1:]
plot_types = ["bar", "line", "scatter", "area", "line", "bar"]
line_labels = [line.split(",")[0] for line in lines[1:]]
data_values = [list(map(float, line.split(",")[1:])) for line in lines[1:]]
data_array = np.array(data_values).T
colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'r', 'g', 'b']

# Plotting
fig = plt.figure(figsize=(15, 10))
x = np.arange(len(line_labels))
ax = fig.add_subplot(111)
ax.set_xlabel('Category')
ax.set_ylabel(data_labels[0], color=colors[0])
ax.bar(x-0.3, data_array[0], color=colors[0], width=0.2, label=data_labels[0])

axes = [ax]
for i, (type, array) in enumerate(zip(plot_types[1:], data_array[1:])):
    ax_new = ax.twinx()
    axes.append(ax_new)
    if type == "bar":
        ax_new.bar(x+(i+1)*0.2 - 0.3, array, color=colors[i+1], alpha=0.5, width=0.2, label=data_labels[i+1])
    elif type == "line":
        ax_new.plot(x, array, color=colors[i+1], label=data_labels[i+1])
    elif type == "scatter":
        ax_new.scatter(x, array, color=colors[i+1], label=data_labels[i+1])
    elif type == "area":
        ax_new.fill_between(x, array, color=colors[i+1], alpha=0.3, label=data_labels[i+1])

for i, ax_new in enumerate(axes[1:]):
    ax_new.set_ylabel(data_labels[i], color=colors[i])
    ax_new.spines['right'].set_position(('outward', i*60))
    ax_new.yaxis.set_major_locator(AutoLocator())
    ax_new.legend(loc="upper left", bbox_to_anchor=(1, 1 - 0.1 * i))

ax.set_title('Technology and the Internet Industry Analysis: User Base, Connectivity, and Revenue')
ax.set_xticks(x)
ax.set_xticklabels(line_labels, rotation=45)

fig.tight_layout()
plt.grid(True)

plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/320_202312311430.png")
plt.show()
plt.clf()
