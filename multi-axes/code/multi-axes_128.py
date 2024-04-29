import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import AutoLocator


# Transofrm data to variables
data_labels = ["Number of Internet Users (Millions)", 
               "E-commerce Sales (Billions)", 
               "Average Internet Speed (Mbps)"]

line_labels = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

data = np.array([
    [2035, 572, 4.6],
    [2201, 690, 5.3],
    [2423, 830, 6.2],
    [2591, 1012, 7.3],
    [2792, 1245, 8.4],
    [2995, 1498, 10.2],
    [3223, 1805, 12.1],
    [3458, 2155, 14.9],
    [3715, 2562, 17.8],
    [3966, 3008, 20.5]
])


# Initialise the size of the figure
plt.figure(figsize=(20,10))

ax1 = plt.subplot(111)

ax1.plot(line_labels, data[:,0], color='b', label=data_labels[0])
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('b')
ax1.tick_params(axis='y', colors='b')
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:,1], color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('g')
ax2.tick_params(axis='y', colors='g')
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.bar(line_labels, data[:,2], color='r', label=data_labels[2], alpha=0.5, align='center')
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2])
ax3.yaxis.label.set_color('r')
ax3.tick_params(axis='y', colors='r')
ax3.yaxis.set_major_locator(AutoLocator())

fig = plt.gcf()
fig.suptitle('Evolution of Internet Usage, Speed and E-commerce Sales 2010-2019')
plt.subplots_adjust(right=0.75)

fig.legend([ax1, ax2, ax3],
           labels=data_labels,
           loc="center right",
           borderaxespad=0.5,
           title="Metrics"
           )

# Save and display the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/95_2023122292141.png", dpi=300)
plt.tight_layout()
plt.show()
plt.clf()
