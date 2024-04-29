import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Generation (GW)", "Revenue ($bn)", "Average Price (cents/kWh)"]
line_labels = ["Coal", "Natural Gas", "Nuclear", "Hydroelectric", "Wind", "Solar", "Geothermal", "Biomass", "Other Renewable"]
data = np.array(
    [
        [530, 50, 9.5],
        [1025, 105, 10.3],
        [800, 80, 10],
        [300, 30, 10],
        [205, 20, 9.7],
        [105, 10, 9.4],
        [25, 2.5, 10],
        [55, 5.5, 10],
        [65, 6.5, 10]
    ]
)

fig = plt.figure(figsize=(25,10))
ax1 = fig.add_subplot(111)

ax1.plot(range(len(line_labels)), data[:,0], label=data_labels[0], color='b')
ax1.set_ylabel(data_labels[0], color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')

ax2 = ax1.twinx()
ax2.bar(np.arange(len(line_labels)) - 0.2, data[:,1], width=0.4, alpha=0.7, label=data_labels[1], color='r')
ax2.set_ylabel(data_labels[1], color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')

ax3 = ax1.twinx()
ax3.scatter(range(len(line_labels)), data[:,2], label=data_labels[2], color='g')
ax3.spines['right'].set_position(('outward', 60)) 
ax3.set_ylabel(data_labels[2], color='g')
for tl in ax3.get_yticklabels():
    tl.set_color('g')

ax1.set_xticks(range(len(line_labels)))
ax1.set_xticklabels(line_labels, rotation=45)

plt.grid()
plt.autoscale()

plt.title('Energy Generation, Revenue and Pricing by Source')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/231_202312311051.png')
plt.clf()
