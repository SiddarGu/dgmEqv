import matplotlib.pyplot as plt
import numpy as np

# Transforming the data
data_labels = ['Number of Vehicles', 'Total Distance Travelled (Miles)', 'Average Fuel Efficiency (Miles per Gallon)', 'Average Speed (Miles per Hour)']
line_labels = ['Trucking', 'Shipping', 'Rail Transport', 'Air Transport', 'Courier Services', 'Warehousing', 'Freight', 'Passenger Transport', 'Taxi Services', 'Logistics Services']
data = np.array([[500, 350000, 8, 55],
                 [120, 450000, 12, 45],
                 [80, 600000, 20, 65],
                 [60, 250000, 25, 550],
                 [250, 200000, 18, 35],
                 [40, 100000, 0, 0],
                 [350, 300000, 10, 50],
                 [200, 150000, 15, 60],
                 [150, 100000, 20, 30],
                 [100, 400000, 0, 0]])

# Creating figure
fig = plt.figure(figsize=[23,15])
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b', alpha=0.6, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='r', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='g', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))   
ax3.set_ylabel(data_labels[2], color='g')
ax4 = ax1.twinx()
ax4.scatter(line_labels, data[:,3], color='purple', label=data_labels[3])
ax4.spines['right'].set_position(('outward', 120))   
ax4.set_ylabel(data_labels[3], color='purple')

# Labels and legends
fig.suptitle('Analysis of Transportation Modes: Vehicles, Distance, Efficiency, and Speed')
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.grid()
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/289_202312311430.png")
plt.clf()
