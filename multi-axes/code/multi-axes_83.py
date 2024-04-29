import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# parse the data
raw_data = """Product,Production Quantity (Tons),Revenue (Millions),Number of Units Sold
Beer,1500000,4300,792
Wine,800000,6700,1100345
Whiskey,700000,5000,890876
Vodka,650000,3800,810654
Brandy,600000,2900,700999
Rum,550000,2700,680432
Tequila,500000,1800,600821
Lager,450000,1700,590231
Stout,400000,1300,500900
Gin,350000,830,450764
Liqueurs,300000,720,400345"""
lines = raw_data.split('\n')
data_labels = lines[0].split(',')
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([list(map(int, line.split(',')[1:])) for line in lines[1:]])

# plot data
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b', label=data_labels[1])
ax1.set_ylabel(data_labels[1], color='b')
ax1.tick_params('y', colors='b')
ax1.yaxis.set_major_locator(AutoLocator())
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', label=data_labels[2])
ax2.set_ylabel(data_labels[2], color='r')
ax2.tick_params('y', colors='r')
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='g', label=data_labels[3])
ax3.set_ylabel(data_labels[3], color='g')
ax3.tick_params('y', colors='g')
ax3.spines['right'].set_position(('outward', 60))
ax3.yaxis.set_major_locator(AutoLocator())

# handle legend
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles3, labels3 = ax3.get_legend_handles_labels()
plt.legend(handles1+handles2+handles3, labels1+labels2+labels3, loc='upper left')

# handle title and save
plt.title('Comprehensive Food and Beverage Production and Sales Analysis')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/245_202312311051.png')
plt.close(fig)
