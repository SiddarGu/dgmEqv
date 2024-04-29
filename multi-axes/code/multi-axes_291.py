import matplotlib.pyplot as plt
import numpy as np

data = np.array([[385,15,4,289],[385,13,6,290],[378,14,5,298],[380,12,7,300],[400,11,8,303],[405,9,9,305],[410,7,12,310],[414,6,11,312],[405,8,10,308],[400,10,9,306],[392,12,7,300],[394,14,6,296]])

data_labels = ['Electrical Energy Produced (TWh)', 'Gas Consumption (BCM)', 'Average Price per kWh in cents', 'Hydro Power (TWh)']
line_labels = ['January','February','March','April','May','June','July','August','September','October','November','December']

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:, 0], label=data_labels[0])

ax2 = ax1.twinx()
ax2.bar(line_labels, data[:, 1], color='r', alpha=0.7, label=data_labels[1])

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], color='m', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))

ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:, 3], alpha=0.5, label=data_labels[3])
ax4.spines['right'].set_position(('outward', 120))

ax1.set_xlabel('Month')
ax1.set_ylabel(data_labels[0])
ax2.set_ylabel(data_labels[1])
ax3.set_ylabel(data_labels[2])
ax4.set_ylabel(data_labels[3])

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.title('Evaluation of Energy Production and Monitoring')
plt.grid(True)
plt.show()

fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/153_202312310108.png')
plt.close(fig)
