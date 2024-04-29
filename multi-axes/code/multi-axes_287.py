import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np

# transforming the data
data_string = """Item,Inventory Stock Levels,Unit Price ($),Average Daily Sales,Theft Losses
TVs,1500,400,15,2
Laptops,2000,800,20,3
Smartphones,5000,600,35,5
Video Games,3000,60,25,4
Headphones,4000,100,30,6
Printers,1200,120,10,1
Tablets,2500,250,18,3
Speakers,1800,80,12,2
Smart Watches,2200,330,14,3
Digital Cameras,1500,300,8,2"""
rows = data_string.split("\n")
data_labels = rows[0].split(",")[1:]
line_labels = [row.split(",")[0] for row in rows[1:]]
data = np.array([list(map(int,row.split(",")[1:])) for row in rows[1:]])

# creating the figure and setting its size
fig = plt.figure(figsize=[25,10])
ax1 = fig.add_subplot(111)

# ploting the data 
ax1.bar(line_labels, data[:,0], label=data_labels[0], color='r', alpha=0.5)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('red')
ax1.tick_params(axis='y', colors='red')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], label=data_labels[1], color='b')
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', colors='blue')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], label=data_labels[2], color='green')
ax3.set_ylabel(data_labels[2])
ax3.spines['right'].set_position(('outward', 60))      
ax3.yaxis.label.set_color('green')
ax3.tick_params(axis='y', colors='green')

ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], 0, label=data_labels[3], color='purple', alpha=0.3)
ax4.set_ylabel(data_labels[3])
ax4.spines['right'].set_position(('outward', 120))   
ax4.yaxis.label.set_color('purple')
ax4.tick_params(axis='y', colors='purple')

plt.title('Inventory, Pricing, and Sales Performance Analysis in Retail and E-commerce')
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)

plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax3.yaxis.set_minor_locator(AutoMinorLocator())
ax4.yaxis.set_minor_locator(AutoMinorLocator())

fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/139_202312310108.png", format='png', dpi=300)
plt.clf()
