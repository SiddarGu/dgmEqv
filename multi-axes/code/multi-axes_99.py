import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import pandas as pd

data = [['Advertising',200,1500,1000],
        ['Banking',500,3000,2000],
        ['Insurance',400,2500,1500],
        ['Investment',300,2000,1200],
        ['Real Estate',350,1800,800],
        ['Retail',600,4000,3000],
        ['Technology',800,5000,2500],
        ['Transportation',450,3500,1500],
        ['Utilities',550,3800,2000],
        ['Wholesale',700,4500,3500]]


data_labels = ["Profit (Millions of Dollars)", "Revenue (Millions of Dollars)", "Number of Employees"]
line_labels = ['Advertising','Banking','Insurance','Investment','Real Estate','Retail','Technology','Transportation','Utilities','Wholesale']
data = np.array([i[1:] for i in data])

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:,0], color='b', label=data_labels[0])
ax1.set_ylabel(data_labels[0])
ax1.tick_params(axis='y', colors='b')
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1])
ax2.spines['right'].set_position(('outward', 70))
ax2.tick_params(axis='y', colors='g')
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='r', label=data_labels[2])
ax3.set_ylabel(data_labels[2])
ax3.spines['right'].set_position(('outward', 140))
ax3.tick_params(axis='y', colors='r')
ax3.yaxis.set_major_locator(AutoLocator())

fig.legend(loc='center right', bbox_to_anchor=(0.9, 0.5), bbox_transform=plt.gcf().transFigure)
plt.grid(True)
plt.title("Business and Finance Performance Analysis: Profit, Revenue, and Workforce")
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/283_202312311430.png')
plt.clf()
