import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Preparing data
data_string = """Category,Revenue (Millions of Dollars),Number of Customers,Number of Orders,Conversion Rate (%)
Apparel,500,15000,5000,33
Electronics,800,12000,4000,25
Beauty and Personal Care,300,20000,6000,30
Home and Kitchen,400,18000,5500,31
Books,200,25000,8000,32
Furniture,600,10000,3500,35
Sports and Outdoors,400,14000,4500,32
Toys and Games,300,16000,5000,31
Automotive,700,9000,3000,33
Grocery,200,30000,10000,33"""
data_rows = data_string.split("\n")[1:]
line_labels = [row.split(",")[0] for row in data_rows]
data = np.array([list(map(int, row.split(",")[1:])) for row in data_rows])
data_labels = data_string.split("\n")[0].split(",")[1:]

# Creating multi-axes chart
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b', alpha=0.6, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', colors='b')
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='r', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params(axis='y', colors='r')
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='g', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))  
ax3.set_ylabel(data_labels[2], color='g')
ax3.tick_params(axis='y', colors='g')
ax3.yaxis.set_major_locator(AutoLocator())

ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], alpha=0.3, color='c', label=data_labels[3])
ax4.spines['right'].set_position(('outward', 120)) 
ax4.set_ylabel(data_labels[3], color='c')
ax4.tick_params(axis='y', colors='c')
ax4.yaxis.set_major_locator(AutoLocator())

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
plt.title("Retail and E-commerce Performance Analysis: Revenue, Customers, Orders, and Conversion Rate")

plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/297_202312311430.png')
plt.clf()
