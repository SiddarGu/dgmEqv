import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data = np.array([[2010, 24, 2490, 2430],
                 [2011, 25, 2620, 2570],
                 [2012, 26, 2730, 2670],
                 [2013, 27, 2840, 2790],
                 [2014, 28, 2970, 2910],
                 [2015, 29, 3130, 3070],
                 [2016, 30, 3290, 3220],
                 [2017, 31, 3450, 3380],
                 [2018, 32, 3640, 3560],
                 [2019, 33, 3840, 3750],
                 [2020, 34, 4050, 3950]])

data_labels = ['Number of Vehicles (Millions)', 
               'Fuel Consumption (Millions of Liters)', 
               'Average Distance Traveled (Millions of Kilometers)']

line_labels = data[:,0]

fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,1], label=data_labels[0], color='k')
ax1.set_ylabel(data_labels[0], color='k')
ax1.yaxis.set_major_locator(ticker.AutoLocator())

ax2 = ax1.twinx()
ax2.fill_between(line_labels, data[:,2], color='g',alpha=0.5,label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(line_labels, data[:,3], label=data_labels[2], color='b')
ax3.set_ylabel(data_labels[2], color='b')

plt.title("Transportation and Logistics: Vehicle Usage and Fuel Consumption Over a Decade")

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/124_202312310108.png')
plt.close()
