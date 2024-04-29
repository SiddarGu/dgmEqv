import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# transform data into the required format
lines = '''Pharmaceuticals,150,2950,4500
Electronics,550,5290,8000
Automotive,720,6750,12500
Food,1000,2340,6500
Plastics,580,3780,3500
Cosmetics,165,2450,6000
Paper,730,1120,4000
Domestic appliances,1020,4500,6770
Furniture,480,2910,5000
Clothes,680,3460,8500'''.split('\n')

line_labels = [l.split(',')[0] for l in lines]
data = np.array([list(map(int, l.split(',')[1:])) for l in lines])
data_labels = ['Units Produced (Thousands)', 'Total Sale Value (Million Dollars)', 'Number of Employees']

# plot initialization
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax1.grid(True)

# plot data
p1 = ax1.bar(line_labels, data[:,0], color='b', label=data_labels[0])
ax2 = ax1.twinx()
p2 = ax2.plot(line_labels, data[:,1], color='r', label=data_labels[1])
ax3 = ax1.twinx()
p3 = ax3.fill_between(line_labels, data[:,2], color='g', alpha=0.5, label=data_labels[2])
ax4 = ax1.twinx()
p4 = ax4.scatter(line_labels, data[:,1], color='y', label=data_labels[1])

# setting the positions and colors of the y axes to avoid confusion
ax3.spines['right'].set_position(('outward', 60)) 
ax4.spines['right'].set_position(('outward', 120)) 
ax3.yaxis.label.set_color(p3.get_facecolor())
ax4.yaxis.label.set_color(p4.get_facecolor())

# set y-axis labels and use autolocator
ax1.set_ylabel(data_labels[0])
ax1.yaxis.set_major_locator(AutoLocator())
ax2.set_ylabel(data_labels[1])
ax2.yaxis.set_major_locator(AutoLocator())
ax3.set_ylabel(data_labels[2])
ax3.yaxis.set_major_locator(AutoLocator())
ax4.set_ylabel(data_labels[1])
ax4.yaxis.set_major_locator(AutoLocator())

# set legend
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

# set title
plt.title('Manufacturing and Production: Product Data Comparative Analysis')

# adjusting layout and save figure
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/116_202312310108.png')

# clear the current figure
plt.clf()
