
import matplotlib.pyplot as plt
import numpy as np

# transform data
data_labels = ['Carbon Footprint (lbs/sqft)', 'Energy Efficiency (kWh/sqft)', 'Water Usage (Gallons/sqft)', 'Recycling Rate (%)']
line_labels = ['Construction', 'Transportation', 'Manufacturing', 'Agriculture', 'Consumption', 'Waste Management']
data = np.array([[1300, 200, 1000, 500, 900, 800], [90, 45, 110, 90, 100, 80], [11, 10, 20, 15, 25, 30], [80, 70, 60, 50, 40, 30]])

# setup chart
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# plot data
ax1.bar(line_labels, data[0, :], color='g', alpha=0.5, label=data_labels[0])
ax2 = ax1.twinx()
ax2.plot(line_labels, data[1, :], color='b', marker='o', linestyle='dashed', label=data_labels[1])
ax3 = ax1.twinx()
ax3.plot(line_labels, data[2, :], color='r', marker='o', linestyle='dashed', label=data_labels[2])
ax4 = ax1.twinx()
ax4.plot(line_labels, data[3, :], color='y', marker='o', linestyle='dashed', label=data_labels[3])

# adjust axis
ax1.set_ylim(0, 1500)
ax2.set_ylim(0, 120)
ax3.set_ylim(0, 35)
ax4.set_ylim(0, 100)
ax3.spines['right'].set_position(('axes', 1.1))
ax4.spines['right'].set_position(('axes', 1.2))

# label axes
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='g')
ax2.set_ylabel(data_labels[1], color='b')
ax3.set_ylabel(data_labels[2], color='r')
ax4.set_ylabel(data_labels[3], color='y')

# add title and legend
plt.title('Environmental Impact of Different Sectors')
plt.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95))

# adjust subplot layout
plt.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/5_2023122270030.png')

# clear figure
plt.clf()