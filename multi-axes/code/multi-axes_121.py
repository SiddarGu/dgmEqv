import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

data_string = "New York,35562,9821,275600,654/n Los Angeles,28974,7183,248300,803/n Chicago,26781,5437,204200,638/n Houston,31654,7232,228700,589/n Phoenix,34556,7124,206500,721/n Philadelphia,29427,5481,186800,706/n San Antonio,30563,4828,157900,595/n San Diego,29815,6791,227400,792/n Dallas,31295,6429,205600,678/n San Jose,28694,8592,299800,897"
data_string = data_string.replace("/n", "\n")
data_list = [row.split(",") for row in data_string.split("\n")]
data_labels = ["Total Houses", "Total Sales ($m)", "Average Price ($)", "Houses Sold"]
line_labels = [row[0] for row in data_list]
data = np.array([list(map(int, row[1:])) for row in data_list])

colors = ['r', 'g', 'b', 'y']

plt.figure(figsize=(20, 10))
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:,0], color=colors[0], alpha=0.6, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color=colors[0])
ax1.tick_params(axis='y', labelcolor=colors[0])
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color=colors[1], label=data_labels[1])
ax2.set_ylabel(data_labels[1], color=colors[1])
ax2.tick_params(axis='y', labelcolor=colors[1])
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color=colors[2], label=data_labels[2])
ax3.set_ylabel(data_labels[2], color=colors[2])
ax3.spines["right"].set_position(("axes", 1.2))
ax3.tick_params(axis='y', labelcolor=colors[2])
ax3.yaxis.set_major_locator(AutoLocator())

ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], color=colors[3], alpha=0.3, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color=colors[3])
ax4.spines["right"].set_position(("axes", 1.4))
ax4.tick_params(axis='y', labelcolor=colors[3])
ax4.yaxis.set_major_locator(AutoLocator())

fig = plt.gcf()
fig.suptitle("Current State of the Real Estate and Housing Market in Major Cities", fontsize=20)

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

fig.tight_layout()
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/161_202312310108.png")

plt.cla()
plt.clf()
