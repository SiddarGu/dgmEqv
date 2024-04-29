import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

#initialize data
data_labels = ['Total Shipment (in Tons)', 'Total Revenue (in million dollars)', 'Fuel Consumption (in thousand gallons)']
data = np.array([[5000,120,4500],[4800,115,4300],[5300,130,4700],[5150,128,4500],[5600,145,4900],[5900,150,5150],[5000,125,4500],[4800,120,4300],[5700,140,5200],[5900,148,5400],[6000,150,5600],[6500,170,5800]])
line_labels = ['January','February','March','April','May','June','July','August','September','October','November','December']

# Plotting
fig = plt.figure(figsize=(23,10))

# plot line chart for 'Total Shipment (in Tons)'
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,0], color='b', linewidth=2)
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params('y', colors='b')
ax1.yaxis.set_major_locator(AutoLocator())

# plot another line chart for 'Total Revenue (in million dollars)'
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g', linewidth=2)
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params('y', colors='g')
ax2.yaxis.set_major_locator(AutoLocator())

# plot bar chart for 'Fuel Consumption (in thousand gallons)'
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60)) 
ax3.bar(line_labels, data[:,2], color='r', alpha=0.3, align='center', width=0.5)
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params('y', colors='r')
ax3.yaxis.set_major_locator(AutoLocator())

# show legends
ax1.legend(loc="upper left", prop={'size':10}, bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
ax2.legend(loc="upper left", prop={'size':10}, bbox_to_anchor=(0,0.9), bbox_transform=ax2.transAxes)
ax3.legend(loc="upper left", prop={'size':10}, bbox_to_anchor=(0,0.8), bbox_transform=ax3.transAxes)

# set title
plt.title('Monthly Analysis of Shipment, Revenue and Fuel Consumption in the Logistics Sector')

# grid
ax1.grid()

# Finishing, saving and showing plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/250_202312311051.png')
plt.clf()
