import matplotlib.pyplot as plt
import numpy as np

# data transformation
data_labels = ["Production Quantity (Units)", "Production Cost (Dollars)", "Average Production Time (Hours)"]
line_labels = ['Furniture', 'Automobiles', 'Machinery', 'Electronics', 'Plastics', 'Textiles', 'Chemicals', 'Metals', 'Food and Beverage', 'Pharmaceuticals']
data = np.array([
    [5000,25000,10],
    [10000,750000,50],
    [2000,500000,20],
    [15000,5000000,30],
    [8000,300000,15],
    [12000,600000,25],
    [3000,2000000,40],
    [6000,1000000,35],
    [10000,800000,30],
    [4000,1500000,45]
])

plt.figure(figsize=(30,25))
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:,0], color='b', alpha=0.5, align='center', label=data_labels[0])
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('blue')
ax1.tick_params(axis='y', colors='blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'go-', label=data_labels[1])
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('green')
ax2.tick_params(axis='y', colors='green')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='r', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='r')
ax3.yaxis.label.set_color('red')
ax3.tick_params(axis='y', colors='red')

plt.grid(True)
plt.autoscale(enable=True, axis='both', tight=True)
plt.title('Manufacturing and Production Analysis: Quantity, Cost, and Time')

ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/287_202312311430.png')
plt.clf()
