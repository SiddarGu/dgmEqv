import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np

# The input string is converted into two lists and a numpy array
data_labels = ["Median Price (USD)", "Total Houses Sold", "Service Cost (USD)"]
line_labels = [str(x) for x in range(2010, 2021)]
data = np.array([[172500, 321900, 4739],
                 [166100, 331400, 4830],
                 [176600, 368000, 4972],
                 [197900, 428000, 5105],
                 [208300, 439000, 5267],
                 [223900, 501000, 5430],
                 [235500, 560000, 5600],
                 [245200, 617000, 5775],
                 [257400, 620000, 5940],
                 [270400, 683000, 6120],
                 [284600, 690000, 6315]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# A line chart is plotted against median price
lns1 = ax1.plot(line_labels, data[:, 0], label=data_labels[0], color='b')

ax2 = ax1.twinx()
# A bar chart is plotted against total houses sold
lns2 = ax2.bar(line_labels, data[:, 1], label=data_labels[1], color='r', alpha=0.6)

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))  # to place a new y-axis at a specific position
# An area chart is plotted against service cost
lns3 = ax3.fill_between(line_labels, 0, data[:, 2], label=data_labels[2], color='g', alpha=0.5) 

lns = lns1+lns2.patches+[lns3]  # list to put all the legends together
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)

ax1.set_xlabel("Year")
ax1.set_ylabel(data_labels[0])
ax2.set_ylabel(data_labels[1])
ax3.set_ylabel(data_labels[2])
ax1.yaxis.label.set_color(lns1[0].get_color())
ax2.yaxis.label.set_color(lns2.patches[0].get_facecolor())
ax3.yaxis.label.set_color(lns3.get_facecolor())
plt.title('Real Estate Market Analysis 2010-2020: Price, Sales, and Service Cost')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/67_2023122292141.png', dpi=300)
plt.cla()
